from flask import Flask
from worker import celery
from celery.result import AsyncResult
from flask import request, jsonify
import logging
import celery.states as states
from utils import check_extension
import os 
import dotenv

dotenv.load_dotenv()

logging.basicConfig(filename="/app/logs/app.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_file():
    file_path = os.environ.get("tenant_dir") + request.files["data_file"].filename
    request.files["data_file"].save(file_path)
    # results = extract_metadata_from_request(request)
    tenant_id = request.form.get("tenant_id")
    print(f"Uploading file {file_path} for tenant {tenant_id}")
    tenant_data_dict = {
        "tenant_id": tenant_id,
        "data": file_path
    }
    if not isinstance(tenant_id, str):
        return jsonify({"error": "tenant_id is required"})

    metadata_update_results = celery.send_task(
        "tasks.ingest_data", 
        args=[tenant_data_dict]
    )

    logging.info(f"Task ID: {metadata_update_results.id}, {metadata_update_results.id}")
    return jsonify({"status": "success", "task_id": metadata_update_results.id})
    

    # results_dict = results.to_dict()

    # metadata_update_results = celery.send_task(
    #     "tasks.ingest_data", 
    #     args=[results_dict]
    # )
    
    # request.files["audio_file"].save(results_dict["file_tmp"])
    # upload_results = celery.send_task(
    #     "tasks.upload_file_to_minio", 
    #     args=[results_dict["file_tmp"]],
    #     kwargs={}
    # )

    # list_task_ids = {
    #     "metadata_update": metadata_update_results.id,
    #     "upload": upload_results.id
    # }
    # logging.info(f"Task ID: {metadata_update_results.id}, {upload_results.id}")
    # return jsonify({"status": "success", "task_id_list": list_task_ids})

@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)