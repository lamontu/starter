
import os
import psutil
import time

# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def test_list():
    show_memory_info('list initiating')
    begin = time.perf_counter()
    list_1 = [i for i in range(100000000)]
    show_memory_info('after list initiated')
    print(sum(list_1))
    show_memory_info('after sum called')
    end = time.perf_counter()
    print(f'time = {end - begin}')

def test_iterator():
    show_memory_info('iterator initiating')
    begin = time.perf_counter()
    iteratable_1 = iter([i for i in range(100000000)])
    show_memory_info('after iterator initiated')
    print(sum(iteratable_1))
    show_memory_info('after sum called')
    end = time.perf_counter()
    print(f'time = {end - begin}')

def test_generator():
    show_memory_info('generator initiating')
    begin = time.perf_counter()
    generator_1 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(generator_1))
    show_memory_info('after sum called')
    end = time.perf_counter()
    print(f'time = {end - begin}')

test_list()
print('--------')

test_iterator()
print('--------')

test_generator()
print('--------')
