"""
这个模块加权合并两个词频表, 生成一个新的词频表.
"""

import json

# 加载文件 1
with open("../sina/sina_3gram.json", "r", encoding='utf-8') as f:
    data1 = json.load(f)

# 加载文件 2
with open("../web_text/web_text_3gram.json", "r", encoding='utf-8') as f:
    data2 = json.load(f)

# 对数据进行加权合并
merged_data = {}
for key in set(data1.keys()) | set(data2.keys()):
    value1 = data1.get(key, 0)
    value2 = data2.get(key, 0)
    merged_data[key] = value1 + value2*4

# 将结果写入新文件
with open("merged_3gram.json", "w", encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)
