import requests
from typing import List


def get_proxy_list() -> List[str]:
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
    response = requests.get(url)
    http_proxies = response.text.splitlines()

    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all"
    response = requests.get(url)
    https_proxies = response.text.splitlines()

    all_proxies = http_proxies + https_proxies
    print(f"{len(all_proxies)} proxies found")

    proxy_list = []
    for proxy in all_proxies:
        try:
            response = requests.get(
                "https://www.google.com", proxies={"https": proxy}, timeout=5)
            if response.status_code == 200:
                proxy_list.append(proxy)
            if len(proxy_list) >= 3:
                break
        except:
            pass

    print(f"{len(proxy_list)} proxies are working")
    return proxy_list


proxy_list = get_proxy_list()
print(proxy_list)
