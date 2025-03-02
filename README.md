### Simple Big-Data Platform

This repo is for simple big data platform

### Setup

To build the containers, setup via ```docker-compose.yml``` file via command:

```
docker compose up -d --build
```

### Deployment

All of the deployment is conducted on the Google Cloud Platform with a Virtual Machine on that platform.

### Testing

For testing the deployed service, you can use the scripts test in ```./test_scripts``` folder:

- ```concurrent_test.py```: using for testing concurrent request to the system

- ```simple_req.py```: to test single request

### Note:

Because we use Minio and MongoDB atlas, please follow carefully the ```deployment_guide``` for the setup and updated the value in the ```.env``` in the ```./src/consumers``` folder and in the ```./src``` folder to ensure you can start and reproduce like what I did.

