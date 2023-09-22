"""
For Spark Task Submit
Example:
spark-submit --executor-memory 10g [filename]
"""
submit_spark_task = "spark-submit"

arguments = [
    # enable Jvm montior
    " --conf \"spark.executor.extraJavaOptions=-javaagent:/home/grads/l/liu.hz/monitor/jmx/jmx_prometheus_javaagent-0.19.0.jar=3010:/home/grads/l/liu.hz/monitor/jmx/config.yaml",
    
    # enable gc log
    " -Xlog:gc*,gc+ref*,gc+ergo*,gc+heap*,gc+stats*,gc+compaction*,gc+age*:file=/home/grads/l/liu.hz/logs/executor-gc.log -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:-UseCompressedOops\""
    
    # core num
    " --conf spark.executor.cores=8"

    " --executor-memory"
]
executor_memory = [
    " 500m",
    " 700m",
    " 900m",
    " 1g",
    " 3g",
    " 5g",
    " 10g",
    " 20g",  
]
task_code = " ~/dev/spark-experiments/word_counter/word_count.py"
task_data_resource = " hdfs://csce-nguyen-s4.engr.tamu.edu:9000"
hdfs_path = "/spark/word_counter/"

# task_data_files = [
#     "wiki.en.text",
#     "10G.txt",
#     "5G.txt",
#     "4G.txt",
#     "3G.txt",
#     "2G.txt",
#     "1G.txt",
#     "500Mb.txt",
#     "300Mb.txt",
#     "200Mb.txt",
#     "100Mb.txt",
# ]
task_data_files = [
    "wiki.en.text",
    "10G.txt",
    "5G.txt",
    "3G.txt",
    "1G.txt",
    "500Mb.txt",
    "300Mb.txt",
    "100Mb.txt",
    "200Mb.txt",
]


"""
For remote log get
Example: scp username@hostname:/remote/path/to/remote_file /local/path/to/save
"""
scp_comment = "scp"
servers = [
    " liu.hz@csce-nguyen-s5.engr.tamu.edu:",
    " liu.hz@csce-nguyen-s6.engr.tamu.edu:"
]

log_path = "~/logs/executor-gc.log"

local_path_raw = "logs"
local_path = " ./logs"



"""
For HDFS Info
"""
hdfs_host = "http://csce-nguyen-s4.engr.tamu.edu:9870/"
hdfs_user = "liu.hz"


 

