# -*- coding: utf-8 -*-

import re

def stats_text_en(text):
    #此处暂时缺省检查参数类型
    text=text.lower()
    text=re.sub(r"[^a-zA-z\s']","",text)
    L1=text.split()
    d1={}
    for i in L1:
        d1[i]=L1.count(i)
    L2=sorted(zip(d1.values(),d1.keys()),reverse=True)
    L2=[x[::-1] for x in L2]
    return L2