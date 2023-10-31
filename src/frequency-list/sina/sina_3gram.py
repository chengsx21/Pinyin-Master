"""
这个模块读取给定的语料库, 并构建相应的词频表.
"""

import glob
import json
import os
import re
from tqdm import tqdm

# 统计每一个二元组在语料库中出现的次数
with open('sina_2gram.json', 'r', encoding='utf-8') as f:
    double_char_dict = json.load(f)
    top_char_dict = {k: v for k, v in double_char_dict.items() if len(k) == 2}

triple_char_dict = {}                              # 建立 {三字: 次数} 的词频表
pattern = re.compile('[^\u4e00-\u9fa5]')           # 匹配所有非汉字的字符
CORPUS_DIR = '../../../corpus/sina_news_gbk'       # 语料库存放地址
FILE_PATTERN = '2016*.txt'                         # 语料库文件通配符

# 遍历所有语料库文件
corpus_files = glob.glob(os.path.join(CORPUS_DIR, FILE_PATTERN))
for corpus_file in corpus_files:
    with open(corpus_file, 'r', encoding='gbk') as f:
        corpus = pattern.sub(' ', f.read())        # 将所有非汉字的字符替换为空格
        corpus = " ".join(corpus.split())          # 去除多余空格
        corpus = list(corpus.replace(" ", " ##"))   # 替换为 #
        cache = []                                 # 借助缓存存储当前的三元词组
        for char in tqdm(corpus, desc="正在处理 {}".format(corpus_file)):
            if len(cache) == 3:                    # 缓存中有三字, 则查看是否可加入三字词频表, 并更新缓存
                WORD_1 = ''.join(cache[0:2])
                WORD_2 = ''.join(cache[1:3])
                if WORD_1 in top_char_dict or WORD_2 in top_char_dict:
                    WORD = ''.join(cache)
                    triple_char_dict[WORD] = triple_char_dict.get(WORD, 0) + 1
                cache = cache[1:3]
            if char == ' ':                        # 当前字符是空格, 首先清空缓存, 再计算下一个二元词组
                cache = []
            else:                                  # 当前字符是单字, 首先加入单字词频表, 再加入缓存
                cache.append(char)
                                                   # 将词频表保存到文件
    triple_char_dict = dict(sorted(triple_char_dict.items(),
            key=lambda x: x[1], reverse=True)[:5*(10**6)])

merged_word_list = {**double_char_dict, **triple_char_dict}
with open('sina_3gram.json', 'w', encoding='utf-8') as f:
    json.dump(merged_word_list, f, ensure_ascii=False, indent=4)
