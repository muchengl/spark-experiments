import run_utils as utils
import run_data as data
import sys

def submit_spark_tasks():
    # init cvs files
    utils.write_CVS("explain","data/time.csv","time","data_file_name","file_size","spark_mem_cfg","spark_instance")

    for mem in data.executor_memory:
        for data_file in data.task_data_files:
            print("===========================================================")
            
            comment_secs=[
                data.submit_spark_task,
                data.arguments,
                mem,
                data.task_code,
                data.task_data_resource,
                data.hdfs_path,
                data_file
            ]
            comment = utils.build_comment("",comment_secs)
            print("RUN: ",comment)
            
            # Run
            result,time = utils.run_comment_with_time_count(comment)

            print("\n*** OUTPUT BEGIN ***\n", result.stdout)
            print("*** OUTPUT END ***\n")
            # print("ERR:\n", result.stderr)

            print("Time Usage:", time)

            utils.download_log(mem,data_file)

            file_size = utils.get_file_size_hdfs(data.hdfs_path+data_file)
            utils.write_CVS("time","data/time.csv",time,data.hdfs_path+data_file,file_size,mem,"NA")

            print("===========================================================\n")


"""
RUN_EX.py
Log output: ./logs/[server_host]+_+[spark_config]_[file_name].log
"""
if __name__ == "__main__":
    print("*** Init Env ***")
    if utils.init_env()==False:
       sys.exit(1) 

    submit_spark_tasks()
   
    
