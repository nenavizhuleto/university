
import random
import time
from collections import namedtuple

Algorithm = namedtuple("Algorithm", "name sort")

def check_sort(array):
    i = 0
    while i < len(array) - 1:
        if array[i] > array[i + 1]:
            return False
        i += 1

    return True
        

def generate_sorted_array(N):
    return [x for x in range(0, N)]

def generate_reversed_array(N):
    array = [x for x in range(0, N)]    
    array.reverse()
    return array

def generate_random_array(N):
    array = [x for x in range(0, N)]
    random.shuffle(array)
    return array

def execution_time(func, args):
    start = time.time()
    result = func(args)
    exec_time = time.time() - start
    return [result, round(exec_time, 3)]
