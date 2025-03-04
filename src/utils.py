import os 

def check_extension(path: str):
    return os.path.splitext(path)[1]

