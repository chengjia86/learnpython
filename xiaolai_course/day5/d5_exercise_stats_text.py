#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

text='''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

text=text.lower()
text=text.replace(r"'s",' is')
text=text.replace(r"'re",' are')
text=text.replace(r"n't",' not')
L=re.split(r"[\s\n*.,!-]+",text)
L=L[1:-1]
d={}
for i in L:
    d[i]=L.count(i)
print(d)
L1=sorted(list(zip(d.values(),d.keys())))
for i in L1:
    print('单词{}出现次数为{}'.format(i[1],i[0]))