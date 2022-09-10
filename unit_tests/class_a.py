
from utils import sort

def preprocess(arr):
    print(f'preprocess {arr}')
    return arr

def postprocess(arr):
    print(f'posprocess {arr}')
    return arr

class A:
    def work(self, arr):
        arr = preprocess(arr)
        arr = sort(arr)
        arr = postprocess(arr)
        return arr
