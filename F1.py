#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:Liu Fuxiang time:2019-06-29
#https://blog.csdn.net/QFire/article/details/81057568
#https://blog.csdn.net/weixin_42441790/article/details/86544964
#CRF++包下载地址https://taku910.github.io/crfpp/#download
#win环境下CRF++的下载与安装https://blog.csdn.net/feng_zhiyu/article/details/80793316

#计算测试集的正确率、召回率、F
def f1(path):
    with open(path) as f:
        all_tag = 0
        loc_tag = 0
        pred_loc_tag = 0
        correct_tag = 0
        correct_loc_tag = 0

        states = ['B', 'M', 'E', 'S']
        for line in f:
            line = line.strip()
            if line == '': continue
            _, r, p = line.split()
            all_tag += 1
            if r == p:
                correct_tag += 1
                if r in states:
                    correct_loc_tag += 1
            if r in states: loc_tag += 1
            if p in states: pred_loc_tag += 1
        #准确率
        loc_P = 1.0 * correct_loc_tag / pred_loc_tag
        #召回率
        loc_R = 1.0 * correct_loc_tag / loc_tag
        print('准确率:{0}\n召回率:{1}\nF1:{2}'.format(loc_P, loc_R, (2 * loc_P * loc_R) / (loc_P + loc_R)))


if __name__ == '__main__':
    f1('test.rst')