#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Liang Chao"

import os
import time
import json
import logging

from csindexdata import fetch_000832
from jisiludata import fetch_cangbaotu
from scatter_compute import get_greendata
from weight_compute import high_weight

JISILU_URL = 'https://www.jisilu.cn/data/cbnew/scatter_data/'
CSINDEX_URL = 'http://www.csindex.com.cn/zh-CN/indices/index-detail/000832'
HISTORY_PATH = "../data/history/"
RESULT_PATH = "../data/result/"
DEFAULT_NAME = "current.json"
LOG_PATH = "../log.txt"

# 设置日志
def set_log(log_file):
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# 重置文件名
def restore_data(filepath, old_filename):
    # 获取当前时间
    date_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    new_name = str(date_time) + '.json'
    # 重命名
    os.rename(filepath + old_filename, filepath + new_name)

# 保存为 json 格式
def save_to_json(csindex, data, file):
    content = {"csindex": csindex, "data": data}
    with open(file, "w") as f:
        json.dump(content, f, ensure_ascii=False)

def main():
    # 设置日志
    logger = set_log(LOG_PATH)
    try:
        # 把当前的 current.json 文件改名为 日期.json 格式
        restore_data(HISTORY_PATH, DEFAULT_NAME)
        restore_data(RESULT_PATH, DEFAULT_NAME)
    except FileNotFoundError:
        logger.warning("there is no current.json")
    # 从 csindex 拿到最新的 中证转债指数
    csindex_price = fetch_000832(CSINDEX_URL)
    # 从jisiku拿到数据存成新的 current.json 文件, 并返回
    new_data = fetch_cangbaotu(JISILU_URL, HISTORY_PATH + DEFAULT_NAME)
    # 计算藏宝图拟合曲线方程式, 得到符合要求的结果
    result = get_greendata(new_data)
    # 计算权重
    result = high_weight(result)
    # 把结果保存成 json
    save_to_json(csindex_price, result, RESULT_PATH + DEFAULT_NAME)
    logger.info(DEFAULT_NAME + " update success")
    # 权重
    for i in result:
        print(i["code"], i["name"], "总权重:"+str(i["total_weight"]), "价格:"+str(i["w1"]), "价值:"+str(i["w2"]), "收益:"+str(i["w3"]))

if __name__ == '__main__':
    main()
