import requests


def get_url(url):
    try:
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        session = requests.session()
        r = session.get(url, headers=header, timeout=30)
        print(r.status_code)
        r.raise_for_status()
        print(r.encoding)
        r.encoding = r.apparent_encoding
        print(r.text[1000:2000])
    except:
        return '連線失敗'


url = 'https://www.amazon.cn/dp/B0977YRQNH/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=8CZNGEZND7YHCWFD57CH&pf_rd_t=101&pf_rd_p=26b99604-91ed-4353-89e4-8f851d0f4900&pf_rd_i=116169071'
get_url(url)
