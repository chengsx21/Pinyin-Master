# :trophy: Pinyin Master

## 程序目录结构

```bash
    ├── README.txt
    ├── corpus/
    │   ├── sina_news_gbk/
    │   │   └── ... (课程提供的*.txt语料库)
    │   └── webtext2019zh/
    │       └── web_text_zh_train.json (自己下载的语料库)
    ├── data/
    │   ├── input.txt
    │   ├── output_v0.txt
    │   ├── output_v1.txt
    │   ├── output_v2.txt
    │   ├── output.txt (最终输出)
    │   └── std_output.txt (标准输出)
    └── src/
        ├── frequency-list/
        │   ├── merged/
        │   │   ├── corpus_merge.py (生成混合三元词频表)
        │   │   └── merged_3gram.json
        │   ├── sina/
        │   │   ├── sina_2gram.json
        │   │   ├── sina_2gram.py (生成二元词频表)
        │   │   ├── sina_3gram.json
        │   │   └── sina_3gram.py (生成三元词频表)
        │   └── web_text/
        │       ├── web_text_2gram.json
        │       ├── web_text_2gram.py (生成二元词频表) 
        │       ├── web_text_3gram.json
        │       └── web_text_3gram.py (生成三元词频表)
        ├── pinyin-dict/
        │   ├── pinyin_dict.json
        │   └── pinyin_dict.py
        ├── pinyin_2gram.py (输出在 output_v0.txt \ 二元模型-新浪语料库)
        ├── pinyin_3gram.py (输出在 output_v1.txt \ 三元模型-新浪语料库)
        ├── pinyin_3gram_fix.py (输出在 output_v2.txt \ 三元模型-社区问答语料库)
        ├── pinyin.py (输出在 output.txt \ 三元模型-加权混合语料库)
        └── utils.py
```

## 程序运行方法

### 安装语料库文件

位置为 `corpus/webtext2019zh/`.

### 安装词频表文件

位置见上, 你也可以通过下面的步骤手动生成词频表:

+ 在 `frequency-list/sina/` 下, 依次运行 `sina_2gram.py`, `sina_3gram.py`.
+ 在 `frequency-list/web_text/` 下, 依次运行 `web_text_2gram.py`, `web_text_3gram.py`.
+ 在 `frequency-list/merged/` 下, 依次运行 `corpus_merge.pinyin`.

### 运行程序

+ 运行 `pinyin_2gram.py ../data/input.txt ../data/output_v0.txt`.
+ 运行 `pinyin_3gram.py ../data/input.txt ../data/output_v1.txt`.
+ 运行 `pinyin_3gram_fix.py ../data/input.txt ../data/output_v2.txt`.
+ 运行 `pinyin.py  ../data/input.txt ../data/output.txt`.
+ 观察终端输出的准确率信息, 必要时可以手动修改文件内的参数 `ALPHA`, `BETA`, `GAMMA` 进行准确率的调整.
