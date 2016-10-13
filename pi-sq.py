import sys
from random import random


if __name__ == "__main__":
    """
        Usage: pi-seq [multiplier]
    """
    multiplier = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * multiplier

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0

    hit_list = map(f, range(1, n + 1))
    count = sum(hit_list)

    
    print("Pi is roughly %f" % (4.0 * count / n))
