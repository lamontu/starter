
import requests
import time
import concurrent.futures
import multiprocessing


INPUTS = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]

# INPUTS = [10000000 + x for x in range(20)]

def execute_one(arg):
    print(f'execute for {arg}')
    resp = requests.get(arg)
    # return sum(i * i for i in range(arg))
    
def execute_all_base(args):
    for arg in args:
        execute_one(arg)

def execute_all_process(args):
    context = multiprocessing.get_context('fork')
    with concurrent.futures.ProcessPoolExecutor(mp_context=context) as executor:
        executor.map(execute_one, args)

def execute_all_thread(args):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(execute_one, args)

def execute_all_future(args):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:        
        to_do = []
        for site in args:
            future = executor.submit(execute_one, site)
            to_do.append(future)
        
        for future in concurrent.futures.as_completed(to_do):
            future.result()


begin = time.perf_counter()
execute_all_base(INPUTS)
end = time.perf_counter()
print(f'execute_all_base time = {end - begin} seconds')

begin = time.perf_counter()
execute_all_thread(INPUTS)
end = time.perf_counter()
print(f'execute_all_thread time = {end - begin} seconds')

begin = time.perf_counter()
execute_all_process(INPUTS)
end = time.perf_counter()
print(f'execute_all_process time = {end - begin} seconds')

begin = time.perf_counter()
execute_all_future(INPUTS)
end = time.perf_counter()
print(f'execute_all_future time = {end - begin} seconds')
