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
'''
t1='\n'.join(list(map(lambda y:(' '.join(list(filter(lambda x:('ea' not in x),y.split())))),(text.replace('better','worse')).split('\n'))))
print(t1)

t2=t1.swapcase()
print(t2)

t3='\n'.join(list(map(lambda y:(' '.join(list(map(lambda x:(''.join(sorted(x))),y.split())))),t2.split('\n'))))
print(t3)
'''

t1=text.replace('better','worse')
print(t1)
del_ea=re.sub(r"[a-zA-Z*]*ea[a-z]*[\s,'.!*]",'',t1)
print(del_ea)
t2=del_ea.swapcase()
print(t2)
t3=re.sub(r'[a-zA-Z][a-zA-Z]*',lambda x:(''.join(sorted(x.group(0)))),t2)
print(t3)