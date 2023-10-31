"""
这个模块加载拼音汉字表, 并仅保留出现在一二级汉字表中的汉字.
"""

import json

pinyin_dict = {}
commomly_used_characters = []
# 读入常用拼音汉字表
with open('../../character-list/commonly_used_character_list.txt', 'r', encoding='utf-8') as f:
    line = f.read()
    commomly_used_characters = list(line)
# 读入一二级汉字表, 并筛选出存在于其中的常用汉字
with open('../../character-list/pinyin_character_list.txt','r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            pairs = line.split()
            pinyin = pairs[0]
            for char in pairs[1:]:
                if char in commomly_used_characters:
                    if pinyin in pinyin_dict:
                        pinyin_dict[pinyin].append(char)
                    else:
                        pinyin_dict[pinyin] = [char]
# 结果储存在 pinyin_dict 中
with open('pinyin_dict.json', 'w', encoding='utf-8') as f:
    json.dump(pinyin_dict, f, ensure_ascii=False, indent=4)
    