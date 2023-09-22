import subprocess


"""
For Spark Task Submit
"""
submit_spark_task = "spark-submit"
arguments = [
    "--conf \"spark.executor.extraJavaOptions=-javaagent:/home/grads/l/liu.hz/monitor/jmx/jmx_prometheus_javaagent-0.19.0.jar=3010:/home/grads/l/liu.hz/monitor/jmx/config.yaml\"",
    "--executor-memory 10g"
]
task_code = "~/dev/spark-experiments/word_counter/word_count.py"
task_data_resource = "hdfs://csce-nguyen-s4.engr.tamu.edu:9000/spark/word_counter/wiki.en.text"



def build_commend(commend,secs):
    for s in secs:
        if type(s) in (list, tuple) :
            commend = build_commend(commend,s)
        else:
            commend=commend+" "+s
    return commend


if __name__ == "__main__":

    commend_secs=[
        submit_spark_task,
        arguments,
        task_code,
        task_data_resource
    ]
    commend = build_commend("",commend_secs)

    # run task
    result = subprocess.run(commend, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print("OUTPUT:\n", result.stdout)
    print("ERR:\n", result.stderr)
