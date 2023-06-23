# 再同一個瀏覽器處理多個域名
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def get_icp_info(page, domain):
    await page.goto(f'https://icp.chinaz.com/home/info?host={domain}')
    await page.wait_for_load_state('networkidle')
    html = await page.content()
    soup = BeautifulSoup(html, 'html.parser')
    biend = soup.find('p', id='license').get_text()
    if biend == '--':
        print(domain,'未備案')
    else:
        companyname = soup.find('p', id='comName').get_text()
        companytyp = soup.find('p', id='typ').get_text()
        print(domain, companytyp,companyname,biend)

async def main():
    domains = ['6785011.com', 'example.com', 'google.com']
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        for domain in domains:
            await get_icp_info(page, domain)
        await browser.close()

asyncio.run(main())


# 多線呈開多個瀏覽器效率加強但會吃cpu
# import asyncio
# from bs4 import BeautifulSoup
# from playwright.async_api import async_playwright


# async def get_icp_info(domain):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         page = await browser.new_page()
#         await page.goto(f'https://icp.chinaz.com/home/info?host={domain}')
#         await page.wait_for_load_state('networkidle')
#         html = await page.content()
#         await browser.close()
#     return html


# async def main():
#     domains = ['6785011.com', 'example.com', 'google.com']
#     tasks = [get_icp_info(domain) for domain in domains]
#     results = await asyncio.gather(*tasks)

#     for domain, html in zip(domains, results):
#         soup = BeautifulSoup(html, 'html.parser')
#         biend = soup.find('p', id='license').get_text()
#         if biend == '--':
#             print(domain, '未備案')
#         else:
#             companyname = soup.find('p', id='comName').get_text()
#             companytyp = soup.find('p', id='typ').get_text()
#             print(domain, companytyp, companyname, biend)


# asyncio.run(main())


# 一般使用方法
# import asyncio
# from playwright.async_api import async_playwright
# from bs4 import BeautifulSoup


# async def get_icp_info(domain):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         page = await browser.new_page()
#         await page.goto(f'https://icp.chinaz.com/home/info?host={domain}')
#         await page.wait_for_load_state('networkidle')
#         html = await page.content()
#         await browser.close()
#     return html


# async def main():
#     domains = ['6785011.com', 'example.com', 'google.com']
#     for domain in domains:
#         html = await get_icp_info(domain)
#         soup = BeautifulSoup(html, 'html.parser')
#         biend = soup.find('p', id='license').get_text()
#         if biend == '--':
#             print(domain,'未備案')
#         else:
#             companyname = soup.find('p', id='comName').get_text()
#             companytyp = soup.find('p', id='typ').get_text()
#             print(domain, companytyp,companyname,biend)


# asyncio.run(main())

