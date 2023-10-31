"""
这个模块读取给定的语料库, 并构建相应的词频表.
"""

import glob
import json
import os
import re
from tqdm import tqdm

# 单字与双字
single_char_dict = {}                              # 建立 {单字: 次数} 的词频表
double_char_dict = {}                              # 建立 {双字: 次数} 的词频表
pattern = re.compile('[^\u4e00-\u9fa5]')           # 匹配所有非汉字的字符
CORPUS_DIR = '../../../corpus/webtext2019zh'       # 语料库存放地址
FILE_PATTERN = 'web_text_zh_train.json'            # 语料库文件

# 遍历所有语料库文件
corpus_files = glob.glob(os.path.join(CORPUS_DIR, FILE_PATTERN))
for corpus_file in corpus_files:
    with open(corpus_file, 'r', encoding='utf-8') as f:
        lines = []
        for i in range(6*(10**5)):
            line = f.readline()
            lines.append(line)
        corpus = " ".join(lines)
        corpus = pattern.sub(' ', corpus)          # 将所有非汉字的字符替换为空格
        corpus = " ".join(corpus.split())          # 去除多余空格
        corpus = list(corpus.replace(" ", " #"))   # 替换为 #
        cache = []                                 # 借助缓存存储当前的二元词组
        for char in tqdm(corpus, desc="正在处理 {}".format(corpus_file)):
            if len(cache) == 2:                    # 缓存中有双字, 则加入双字词频表, 并更新缓存
                WORD = ''.join(cache)
                double_char_dict[WORD] = double_char_dict.get(WORD, 0) + 1
                cache = cache[1:2]
            if char == ' ':                        # 当前字符是空格, 首先清空缓存, 再计算下一个二元词组
                cache = []
            else:                                  # 当前字符是单字, 首先加入单字词频表, 再加入缓存
                if char != '#':
                    single_char_dict['#'] = single_char_dict.get('#', 0) + 1
                    single_char_dict[char] = single_char_dict.get(char, 0) + 1
                cache.append(char)
                                                   # 将词频表进行排序并保存到文件
single_char_dict = dict(sorted(single_char_dict.items(), key=lambda x: x[1], reverse=True))
double_char_dict = dict(sorted(double_char_dict.items(), key=lambda x: x[1], reverse=True))
merged_word_list = {**single_char_dict, **double_char_dict}
with open('web_text_2gram.json', 'w', encoding='utf-8') as f:
    json.dump(merged_word_list, f, ensure_ascii=False, indent=4)
