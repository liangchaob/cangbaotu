#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Liang Chao"

import json
import requests
from lxml import etree 

# 获得中证可转换债券指数数据
def fetch_000832(target_url):
    # 设置 header
    headers = {
        'cache-control': "no-cache",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Connection': "close"
        }
    # 获得网页
    r = requests.request("GET", target_url, headers=headers)
    e_html = etree.HTML(r.text)
    price_000832 = e_html.xpath('//table[@class="table tc"]/tr[2]/td[1]/text()')[0]
    return round(float(price_000832), 2)