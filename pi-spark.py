import sys
from random import random

from pyspark import SparkContext


if __name__ == "__main__":
    """
        Usage: pi-spark [partitions]
    """
    sc = SparkContext(appName="pySparkPi")
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0

    count = sc.parallelize(range(1, n + 1), partitions).map(f).reduce(lambda x, y: x + y)
    print("Pi is roughly %f" % (4.0 * count / n))

    sc.stop()
