import time
from functools import lru_cache
@lru_cache(maxsize=3)
def somework(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work ")
    somework(3)
    print("Done")
    somework(3)
    print("Done agian")
