import requests
import time
import asyncio

url = 'https://20211005t224603-dot-gweb-mobile-hub-test-my-site.appspot.com/tms/url_info?url=kf8630.com'
loop = asyncio.get_event_loop()

start_time = time.time()


async def send_req(url):
    t = time.time()
    print("Send a request at", t-start_time, "seconds.")

    res = await loop.run_in_executor(None, requests.get, url)

    t = time.time()
    print("Receive a response at", t-start_time, "seconds.")
    print(res)

tasks = []

for i in range(1):
    task = loop.create_task(send_req(url))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
