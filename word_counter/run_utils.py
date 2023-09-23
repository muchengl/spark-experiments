import subprocess
from datetime import datetime
import run_data as data
import os
import shutil
import csv
import hdfs

def build_comment(commend,secs):
    for s in secs:
        if type(s) in (list, tuple) :
            commend = build_comment(commend,s)
        else:
            commend=commend+""+s
    return commend

def run_comment_with_time_count(comment):
    # run task
    t1 = datetime.now()
    result = subprocess.run(comment, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    t2 = datetime.now()
    time_difference = t2 - t1

    return result,time_difference.total_seconds()

def init_env():
    # remove dirs and mkdir
    folder_path = data.local_path_raw
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"RUN: rm {folder_path}")
        except OSError as e:
            print(f"Can't rm {folder_path}: {e}")
            return False
    
    try:
        os.mkdir(folder_path)
        print(f"RUN: mkdir {folder_path}")
    except OSError as e:
        print(f"Can't mkdir {folder_path}: {e}")
        return False
    
    # init data dir
    folder_path = "data"
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"RUN: rm {folder_path}")
        except OSError as e:
            print(f"Can't rm {folder_path}: {e}")
            return False
    
    try:
        os.mkdir(folder_path)
        print(f"RUN: mkdir {folder_path}")
    except OSError as e:
        print(f"Can't mkdir {folder_path}: {e}")
        return False
    
    return True


def log_local_name(server,spark_config,file_name):
    target_file = "/"+server+"_"+spark_config+"_"+file_name+".log"
    target_file = target_file.replace(" ", "")
    return target_file
def download_log(spark_config,file_name):
    for server in data.servers :
        comment_secs=[
            data.scp_comment,
            server,
            data.log_path,
            data.local_path,
            log_local_name(server,spark_config,file_name)
        ]
        comment = build_comment("",comment_secs)
        print("RUN: ",comment)
        result = subprocess.run(comment, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def write_CVS(explain,cvs_file_name,data,file_name,file_size,mem_cfg,instance):
    with open(cvs_file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([explain,file_name,file_size,instance,mem_cfg,data])


def get_file_size_hdfs(path):
    hdfs_client = hdfs.Client(data.hdfs_host)
    file_size = hdfs_client.status(path)['length']
    return file_size
