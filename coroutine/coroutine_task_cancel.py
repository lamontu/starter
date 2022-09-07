
import asyncio
import time

async def worker_1():
    await asyncio.sleep(1)
    return 1

async def worker_2():
    await asyncio.sleep(2)
    return 2 / 0

async def worker_3():
    await asyncio.sleep(3)
    return 3

async def main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    await asyncio.sleep(2)
    task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)

begin = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print(f'time = {end - begin}s')

########## 输出 ##########

# [1, ZeroDivisionError('division by zero'), CancelledError()]
# time = 2.00 s