#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Liang Chao'

import os
import time
import json

from get_jisiludata import fetch_cangbaotu
from scatter_compute import get_greendata

TARGET_URL = 'https://www.jisilu.cn/data/cbnew/scatter_data/'
HISTORY_PATH = "../history/"
DEFAULT_NAME = "current.json"
RESULT_PATH = "../result/"

# 重置文件名
def restore_data(filepath, old_filename):
    # 获取当前时间
    date_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    new_name = str(date_time) + '.json'
    # 重命名
    os.rename(filepath + old_filename, filepath + new_name)

# 保存为 json 格式
def save_to_json(data, file):
    content = {"data": data}
    with open(file, "w") as f:
        json.dump(content, f, ensure_ascii=False)

def main():
    # 把当前的 current.json 文件改名为 日期.json 格式
    restore_data(HISTORY_PATH, DEFAULT_NAME)
    restore_data(RESULT_PATH, DEFAULT_NAME)
    # 从jisiku拿到数据存成新的 current.json 文件, 并返回
    new_data = fetch_cangbaotu(TARGET_URL, HISTORY_PATH + DEFAULT_NAME)
    # # 计算藏宝图拟合曲线方程式, 得到符合要求的结果
    result = get_greendata(new_data)
    # # 把结果保存成 json
    save_to_json(result, RESULT_PATH + DEFAULT_NAME)
    print(result)

if __name__ == '__main__':
    main()
