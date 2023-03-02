import aiohttp
import asyncio
from typing import List


async def get_proxy_list() -> List[str]:
    async with aiohttp.ClientSession() as session:
        urls = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all"
        ]
        proxy_list = []
        for url in urls:
            async with session.get(url) as response:
                proxies = await response.text()
                proxy_list += proxies.splitlines()
        print(f"{len(proxy_list)} proxies found")
        return proxy_list


async def test_proxy(proxy: str, session: aiohttp.ClientSession) -> bool:
    try:
        async with session.get("https://www.google.com", proxy=f"http://{proxy}", timeout=5) as response:
            if response.status == 200:
                return True
    except:
        pass

    return False


async def test_proxies(proxies: List[str], limit: int = 20) -> List[str]:
    working_proxies = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for proxy in proxies:
            task = asyncio.ensure_future(test_proxy(proxy, session))
            tasks.append(task)
        results = await asyncio.gather(*tasks)

    for proxy, is_working in zip(proxies, results):
        if is_working:
            working_proxies.append(proxy)

        if len(working_proxies) >= limit:
            break

    print(f"{len(working_proxies)} proxies are working")
    return working_proxies[:limit]


async def main():
    proxy_list = await get_proxy_list()
    working_proxies = await test_proxies(proxy_list)
    print(working_proxies)


if __name__ == "__main__":
    asyncio.run(main())
