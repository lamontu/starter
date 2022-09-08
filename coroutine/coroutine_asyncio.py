import time
import asyncio

URL_LIST = ['url_1', 'url_2', 'url_3', 'url_4']
def crawl_page(url):
    print(f'crawling {url}')
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print(f'OK {url}')

def main1(urls):
    for url in urls:
        crawl_page(url)

start = time.perf_counter()
main1(URL_LIST)
end = time.perf_counter()
print(f'time = {end - start}')
print('--------')

async def crawl_page_asnyc(url):
    print(f'crawling {url}')
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print(f'OK {url}')

async def main2(urls):
    for url in urls:
        await crawl_page_asnyc(url)

start = time.perf_counter()
asyncio.run(main2(URL_LIST))
end = time.perf_counter()
print(f'time = {end - start}')
print('--------')

async def main3(urls):
    tasks = [crawl_page_asnyc(url) for url in urls]
    # the for loop will be slower than gather call
    await asyncio.gather(*tasks)
    # for task in tasks:
    #     await task

start = time.perf_counter()
asyncio.run(main3(URL_LIST))
end = time.perf_counter()
print(f'time = {end - start}')
print('--------')

async def main4(urls):
    tasks = [asyncio.create_task(crawl_page_asnyc(url)) for url in urls]
    # the for loop will be same as the gather call
    await asyncio.gather(*tasks)
    # for task in tasks:
    #     await task

start = time.perf_counter()
asyncio.run(main4(URL_LIST))
end = time.perf_counter()
print(f'time = {end - start}')