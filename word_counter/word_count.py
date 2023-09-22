import sys
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":

    filepath = sys.argv[1]
    print("FILE:",filepath)


    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    # hdfs://csce-nguyen-s4.engr.tamu.edu:9000/user/test/wiki.en.text/
    lines = spark.read.text(filepath).rdd.map(lambda r: r[0])

    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    
    output = counts.collect()
    print("number of words in this book: ",len(output))

    # for (word, count) in output:
    #    print("%s: %i" % (word, count))

    spark.stop()
