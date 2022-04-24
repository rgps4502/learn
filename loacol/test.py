import asyncio
import time


async def dosomething(num):
    print('start{}'.format(num))
    await asyncio.sleep(num)
    print('sleep{}'.format(num))


async def main():
    task1 = asyncio.create_task(dosomething(1))
    task2 = asyncio.create_task(dosomething(2))
    task3 = asyncio.create_task(dosomething(5))
    await task1
    await task2
    await task3

if __name__ == '__main__':
    time_start = time.time()
    asyncio.run(main())
    print(time.time() - time_start)
