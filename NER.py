#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:Liu Fuxiang time:2019-06-30
#CRFF python接口安装教程https://blog.csdn.net/likianta/article/details/86318565
import os,CRFPP
def load_model(path):
    #import os,CRFPP
    if os.path.exists(path):
        return CRFPP.Tagger('-m {0} -v 3 -n2'.format(path))
    return None


def locationNER(text):
    #tagger = load_model('model')
    tagger=CRFPP.Tagger('-m model -v 3 -n2')
    for c in text:
        tagger.add(c)
    result = []
    tagger.parse()
    #print(tagger.size())
    word = ''
    for i in range(0, tagger.size()):
        for j in range(0, tagger.xsize()):
            ch = tagger.x(i, j)
            print(ch)
            tag = tagger.y2(i)
            print(tag)
            if tag == 'B':
                word = ch
            elif tag == 'M':
                word += ch
            elif tag == 'E':
                word += ch
                result.append(word)
            elif tag == 'S':
                word = ch
                result.append(word)
    return result


text = '香港特别行政区发生了动乱'
print(text, locationNER(text), sep='==> ')
