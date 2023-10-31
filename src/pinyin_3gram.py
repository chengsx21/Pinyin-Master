"""
这个模块基三元汉字模型, 实现了 viterbi 算法.
"""

import json
from utils import main

with open('pinyin-dict/pinyin_dict.json', 'r', encoding='utf-8') as f:
    pinyin_dict = json.load(f)
with open('frequency-list/sina/sina_3gram.json', 'r', encoding='utf-8') as f:
    word_frequency_dict = json.load(f)
ALPHA = 0.005                                 # 平衡因子, 用于处理三元词语出现为次数为 0 的情况
BETA = 0.2                                    # 平衡因子, 用于处理三元词语出现为次数为 0 的情况
GAMMA = 1 - ALPHA - BETA                      # 平衡因子, 用于处理三元词语出现为次数为 0 的情况

def viterbi(text, k=10):
    """
    输入:
        - text: 待转换的拼音文本, 字符串类型.
        - k: 取前 k 个最大概率的汉字, 整数类型, 默认值为 10.
    输出:
        - 转换后的汉字.
    """
    words = text.strip().split()                  # 将拼音文本按照空格分割成单词列表
    cur_state = [('##', 1)]                       # 初始化 Viterbi 算法的起始状态
    follow_state = []                             # 当前状态可能的状态转移
    for word in words:
        follow_state = []
        for char in pinyin_dict.get(word, []):    # 计算当前汉字的最大概率和对应的前一个汉字, 添加到状态列表中
            probability, prev_character = max((state[1] * (
                GAMMA * word_frequency_dict.get(state[0][-2:] + char, 0) /
                word_frequency_dict.get(state[0][-2:], 1) +
                BETA * word_frequency_dict.get(state[0][-1] + char, 0) /
                word_frequency_dict.get(state[0][-1], 1) +
                ALPHA * word_frequency_dict.get(char, 0) /
                word_frequency_dict.get('#', 0)), state[0])
                for i, state in enumerate(cur_state))
            follow_state.append((prev_character + char, probability))
                                                  # 选取前 k 个最大概率的句子作为下一次 Viterbi 算法的状态
        cur_state = sorted(follow_state, key=lambda x: x[1], reverse=True)[:k]
    return cur_state[0][0][2:]


if __name__ == '__main__':
    main(viterbi)
