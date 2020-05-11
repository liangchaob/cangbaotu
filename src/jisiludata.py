# encoding: utf-8
'''
* liangchaob@163.com 
* 2020.5
'''
import json
import requests

# 获得集思录数据
def fetch_cangbaotu(target_url, default_filename):
    # 设置 header
    headers = {
        'cache-control': "no-cache",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Connection': "close"
        }
    # 获得 json
    result = requests.request("GET", target_url, headers=headers).json()
    # 保存 dict 到 json 文件
    with open(default_filename, "w") as f:
        json.dump(result, f, ensure_ascii=False)

    # 返回结果
    return result