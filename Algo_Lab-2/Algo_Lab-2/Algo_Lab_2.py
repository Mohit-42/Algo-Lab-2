import random 
from merge import merge_sort
from insertion import insertion_sort
import time

def run_ins(data):
    start_time= time.time_ns()
    insertion_sort(data)
    end_time=time.time_ns()
    time_taken=end_time- start_time
    return time_taken

def run_mer(data,n):
    start_time1= time.time_ns()
    merge_sort(data,0,n-1)
    end_time1=time.time_ns()
    time_taken1=end_time1- start_time1
    return time_taken1

n=10000
a = list(range(n))
data=[random.randint(1, n) for _ in range(n)]
c=[run_mer(data,n) for i in range (1,5)]
d=max(c)
print(d)

