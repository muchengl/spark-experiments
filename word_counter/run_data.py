"""
For Spark Task Submit
Example:
spark-submit --executor-memory 10g [filename]
"""
submit_spark_task = "spark-submit"
# executor_memory = [
#     " 150g",
#     " 140g",
#     " 130g",
#     " 120g",
#     " 110g",
#     " 100g",
#     " 90g",
#     " 80g",
#     " 70g",
#     " 60g",
#     " 50g",
#     " 45g",
#     " 40g",
#     " 35g",
#     " 30g",
#     " 25g",
#     " 20g",
#     " 15g",
#     " 10g",
#     " 5g",
#     " 4g",
#     " 3g",
#     " 2g",
#     " 1g",
# ]

arguments = [
    # JAVA agent Optional
    " --conf \"spark.executor.extraJavaOptions=-javaagent:/home/grads/l/liu.hz/monitor/jmx/jmx_prometheus_javaagent-0.19.0.jar=3010:/home/grads/l/liu.hz/monitor/jmx/config.yaml\"",
    " --executor-memory"
]
executor_memory = [
    " 150g",
    " 130g",
    " 100g",
    " 80g",
    " 40g",
    " 20g",
    " 10g",
    " 5g",
    " 1g",
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
    "100Mb.txt",
    "200Mb.txt",
    "wiki.en.text",
    "10G.txt",
    "5G.txt",
    "3G.txt",
    "1G.txt",
    "500Mb.txt",
    "300Mb.txt",
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


 

