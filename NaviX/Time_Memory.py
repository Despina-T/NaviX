import time
import psutil


def time_calc(time_start):
    time_elapsed = round((time.perf_counter() - time_start), 4)
    print('Time needed: ', time_elapsed, 'secs')
    return time_elapsed


def mem_calc():
    process = psutil.Process()
    memory = round(process.memory_info().rss / 1000000, 4)
    print('Memory used: ', memory, 'Mbs')
    return memory

