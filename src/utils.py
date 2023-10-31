"""
这个模块实现了一些通用函数.
"""

import argparse

def read_files(input_file):
    """
    读取输入文件和标准输出文件
    """
    with open(input_file, 'r', encoding='utf-8') as fin:
        input_lines = fin.readlines()
    with open('../data/std_output.txt', 'r', encoding='utf-8') as fout:
        output_lines = fout.readlines()
    return input_lines, output_lines


def calculate_accuracy(func, input_lines, output_lines, output_file):
    """
    计算字正确率和句正确率
    """
    text = ''
    char_total = 0
    character_correct = 0
    sentence_total = 0
    sentence_correct = 0

    for i, sentence in enumerate(input_lines):               # 转换拼音为汉字
        input_pinyin = sentence.strip()
        output_pinyin = func(input_pinyin)
        text += output_pinyin + '\n'
        std_output_pinyin = output_lines[i].strip()

        for j, std_hanzi in enumerate(std_output_pinyin):    # 计算字正确率
            char_total += 1
            if j < len(output_pinyin) and std_hanzi == output_pinyin[j]:
                character_correct += 1

        if std_output_pinyin == output_pinyin:               # 计算句正确率
            sentence_correct += 1
        sentence_total += 1

    with open(output_file, 'w', encoding='utf-8') as fwri:  #
        fwri.write(text)
    return character_correct / char_total, sentence_correct / sentence_total


def main(func):
    """
    进行输入法转换并计算正确率
    """
    # 创建命令行参数解析器, 并添加输入文件参数
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    input_lines, output_lines = read_files(args.input_file)
    character_accuracy, sentence_accuracy = calculate_accuracy(
        func, input_lines, output_lines, args.output_file)
    print(f'单字正确率为: {character_accuracy:.4%}')
    print(f'整句正确率为: {sentence_accuracy:.4%}')
