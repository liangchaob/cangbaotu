# encoding: utf-8
'''
* liangchaob@163.com 
* 2020.5
'''

# 价格权重
def w1(price):
    if price <= 90:
        return 5
    elif price <= 100:
        return 4
    elif price <= 110:
        return 3
    elif price <= 120:
        return 2
    elif price > 120:
        return 1

# 价值权重
def w2(convert_value):
    if convert_value <= 80:
        return 1
    elif convert_value <= 90:
        return 2
    elif convert_value <= 100:
        return 3
    elif convert_value <= 110:
        return 4
    elif convert_value > 110:
        return 5

# 收益权重
def w3(ytm_rt):
    if ytm_rt <= 0:
        return 1
    elif ytm_rt <= 0.5:
        return 2
    elif ytm_rt <= 1:
        return 3
    elif ytm_rt <= 2:
        return 4
    elif ytm_rt > 2:
        return 5

# 等分器
# def func(listTemp, n):
#     for i in range(0, len(listTemp), n):
#         yield listTemp[i:i + n]

def odd(item):
    return item["w1"] > 0 and item["w2"] > 0 and item["w3"] > 0





# 输入数据, 提取三个指标都高的
def high_weight(data):
    # data = data_obj["data"]
    result = []
    # result2 = []
    # 提取data 里的三项指标, 按照权重算出第四指标, 重新组成新的 list
    for kv in data:
        item = {}
        item["code"] = kv["bond_id"]
        item["name"] = kv["bond_nm"]
        item["price"] = float(kv["price"])
        item["convert_value"] = float(kv["convert_value"])
        item["ytm_rt"] = float(kv["ytm_rt"])
        item["w1"] = w1(item["price"])
        item["w2"] = w2(item["convert_value"])
        item["w3"] = w3(item["ytm_rt"])
        item["total_weight"] = item["w1"] + item["w2"] + item["w3"]
        result.append(item)

    data_ordered = sorted(result, key=lambda x : x['total_weight'], reverse=True)

    #     rt = float(kv["ytm_rt"])
    #     result2.append(rt)

    # result2.sort()
    result3 = list(filter(odd, data_ordered))
    # print(result3)
    # temp = func(result3, len(result3)//4)
    # for li in temp:
    #     print(li)

    

    return result3