import os

def safe_create_dir(path):
    try:
        os.mkdir(path)
    except:
        pass
