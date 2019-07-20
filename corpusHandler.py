#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:Liu Fuxiang time:2019-06-29
#https://blog.csdn.net/QFire/article/details/81057568
#https://blog.csdn.net/weixin_42441790/article/details/86544964
#CRF++包下载地址https://taku910.github.io/crfpp/#download
#win环境下CRF++的下载与安装https://blog.csdn.net/feng_zhiyu/article/details/80793316
#对1998年人民日报分词数据集进行数据处理，生成train.txt、test.txt文件，每行的标注转换-->地名
def tag_line(words, mark):
    #对应字数组
    chars = []
    #字数组对应标签
    tags = []
    temp_word = ''  # 用于合并组合词([]中的组合词)
    for word in words:
        # print(word)
        word = word.strip('\t ')#如：迈向/v
        if temp_word == '':
            bracket_pos = word.find('[')  # [ ]ns
            w, h = word.split('/')#w:词；h:词性
            if bracket_pos == -1:#没有'['
                if len(w) == 0: continue
                chars.extend(w)#加入数组
                if h == 'ns':  # 词性为地名
                    #单字词：+S；非单字词：+B(实体首部)、M*(len(w)-2)(实体中部)、E(实体尾部)
                    tags += ['S'] if len(w) == 1 else ['B'] + ['M'] * (len(w) - 2) + ['E']
                else:
                    tags += ['O'] * len(w)
            else:#有'['
                #print(w)
                #获取'['后的词
                w = w[bracket_pos + 1:]
                temp_word += w
        else:
            bracket_pos = word.find(']')
            w, h = word.split('/')
            if bracket_pos == -1:
                temp_word += w
            else:
                #print(w)
                w = temp_word + w
                h = word[bracket_pos + 1:]
                temp_word = ''
                if len(w) == 0: continue
                chars.extend(w)
                if h == 'ns':
                    tags += ['S'] if len(w) == 1 else ['B'] + ['M'] * (len(w) - 2) + ['E']
                else:
                    tags += ['O'] * len(w)
    assert temp_word == ''
    return (chars, tags)


#读取人民日报语料库，抽样20%作为测试集保存到test.txt，剩余作为训练集保存到train.txt
def corpusHandler(corpusPath):
    import os
    root = os.path.dirname(corpusPath)#去掉文件名，返回目录
    with open(corpusPath,encoding='utf-8') as corpus_f, \
            open(os.path.join(root, 'train.txt'), 'w') as train_f, \
            open(os.path.join(root, 'test.txt'), 'w') as test_f:
        pos = 0
        for line in corpus_f:
            line = line.strip('\r\n\t');
            if line == '': continue
            isTest = True if pos % 5 == 0 else False  # 抽样20%作为测试集使用
            words = line.split()[1:]#获取每行第1个及后面元素(去除每行开始时间)
            if len(words) == 0: continue
            #line_chars:名 ；line_tags:对应标签(B/M/S/O)
            line_chars, line_tags = tag_line(words, pos)
            saveObj = test_f if isTest else train_f
            for k, v in enumerate(line_chars):
                saveObj.write(v + '\t' + line_tags[k] + '\n')
            saveObj.write('\n')
            pos += 1


if __name__ == '__main__':
    corpusHandler('./train2.txt')