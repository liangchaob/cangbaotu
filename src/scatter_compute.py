#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Liang Chao"

import operator
import matplotlib.pyplot as plt
import numpy as np

# 数据130截断, 预期正收益, AA 以上
def is_odd(item):
    return float(item["price"]) < 130 and float(item["convert_value"]) < 130 and float(item["ytm_rt"]) > 0 and 'AA' in item["rating_cd"]

# 获得清洗过的数据
def get_cleandata(data):
    data_filtered = list(filter(is_odd, data))
    for item in data_filtered:
        item["convert_value"] = float(item["convert_value"])
        item["price"] = float(item["price"])

    # 排序
    data_ordered = sorted(data_filtered, key=lambda x : x['convert_value'], reverse=True)
    return data_ordered

# 获得曲线函数
def get_line(data):
    # 正股价格
    price = map(lambda x: float(x["price"]), data)
    # 转股价值
    convert_value = map(lambda x: float(x["convert_value"]), data)
    x = np.array(list(convert_value))
    y = np.array(list(price))
    z = np.polyfit(x, y, 2)#用2次多项式拟合
    p = np.poly1d(z)
    print(p) #在屏幕上打印拟合多项式
    return p

# 获得关键 item
def get_keyresult(data):
    key_names = {"bond_id", "bond_nm", "convert_value", "price", "ytm_rt"}
    result = []
    # 提取关键kv
    for item in data:
        new_item = {key: value for key, value in item.items() if key in key_names}
        result.append(new_item)
        
    return result

# 获得绿色区域数据
def get_greendata(data_obj):
    # 获得数据
    data = data_obj["data"]
    # 清洗数据
    data_cleaned = get_cleandata(data)
    # 获取 x y轴 转成函数
    line = get_line(data_cleaned)

    # 绿色区域
    def green_area(item):
        # 中间区域(80-100)
        # in_middle_area = item["convert_value"] > 80 and item["convert_value"] < 100
        # 线下区域
        under_line = line(item["convert_value"]) > item["price"]
        # 同时满足
        return under_line

    # 筛选数据
    result = list(filter(green_area, data_cleaned))
    # 获得关键值
    result = get_keyresult(result)
    return result
