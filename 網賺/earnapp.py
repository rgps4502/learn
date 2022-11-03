import subprocess
import requests
import json

url = "https://earnapp.com/dashboard/api/device_statuses?appid=earnapp_dashboard&version=1.302.96"

payload = json.dumps({
    "list": [
        {
            "uuid": "sdk-node-6f5b6196c5b149e5a12408fb11b9cf74",
            "appid": "node_earnapp.com"
        },
        {
            "uuid": "sdk-node-f34bdce86550484b8f3ef7cf594aa160",
            "appid": "node_earnapp.com"
        }
    ]
})
headers = {
    'authority': 'earnapp.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-TW,zh;q=0.9',
    'content-type': 'application/json',
    'cookie': '_gid=GA1.2.1615302111.1653615077; xsrf-token=czZ4WE0_XfHC1RT0VYdh6IW8; auth=1; auth-method=google; oauth-refresh-token=1%2F%2F0dD6I5Dg-U3m6CgYIARAAGA0SNwF-L9IrrK-nqejYq9Ss5vfz_53UwFJZUf98TWPOMV3FyKMqdO9gI7Joij3IvLhiV-gPWz6R7Yc; oauth-token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjM4ZjM4ODM0NjhmYzY1OWFiYjQ0NzVmMzYzMTNkMjI1ODVjMmQ3Y2EiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI4MzE4MTQyNzE0MjMtOWhxNHVicXRhb2NlcXR2amNyZzVsMmwyMm91Y3BicTEuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI4MzE4MTQyNzE0MjMtOWhxNHVicXRhb2NlcXR2amNyZzVsMmwyMm91Y3BicTEuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTE1NTQ5NDIyMjE3MzAzNDc0MjEiLCJlbWFpbCI6InJncHM0NTAyMUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6Iko5STFLdUg4Q05PdVVmNjZVRVFhTWciLCJuYW1lIjoi5pyI55m9IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BT2gxNEdqQlpMZ0o3d2tjcEc4S1o2YXJjbklVZU1GUjg4RUJoYkc5UUFCRlltaz1zOTYtYyIsImdpdmVuX25hbWUiOiLnmb0iLCJmYW1pbHlfbmFtZSI6IuaciCIsImxvY2FsZSI6InpoLVRXIiwiaWF0IjoxNjUzNzE4MjExLCJleHAiOjE2NTM3MjE4MTF9.H8_HC5nuu5-IB-twh_nrlXsfCKDMl2OTCgYbpFWpHnTArgP1Zdp_OsjNQjbXr4Pj-hrxJA7CInxObXS6-coE3yVyXmccsBAwxEMPNsHqUHfo63Vh65Im72DtXuk6LWssDmRJp4pPQhJx0ablaUOKqEGEeuEVaFgSKom0M9F6eE3hOX1MtLmoBYvWE1L6qHlQGr9OuJ6q0bAu_ArhJeFisi-m5VNTNqEUGI5UpmjioT4AS8T3kYzLU8JrA82CBEuArAE3XOloJEj8cdzxcR-yOlEssB6s_0_SYWnrbPbLWMC2Y6eM30YYWCPXwghYBDuQgwDnFM52tkqYvKgVMnpuEA; _gat_UA-60520689-12=1; _ga_FG23QXLNQP=GS1.1.1653718930.11.1.1653720495.0; _ga=GA1.1.200184155.1653615077',
    'origin': 'https://earnapp.com',
    'referer': 'https://earnapp.com/dashboard',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'xsrf-token': 'czZ4WE0_XfHC1RT0VYdh6IW8'
}

response = requests.request("POST", url, headers=headers, data=payload).json()
print(response)
status_list = []
# 獲取Drive狀態
for res in response['statuses']:
    # print(response['statuses'][res]['online'])
    status_list.append(response['statuses'][res]['online'])
if False in status_list:
    subprocess.getstatusoutput(
        "docker restart $(docker ps -a | awk '{print $10}' |grep earnapp)")[1]
