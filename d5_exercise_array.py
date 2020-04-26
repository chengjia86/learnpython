#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L=list(range(10))
print(L)
L=L[::-1]
print(L)
L=[str(x) for x in L]
print(L)
L=''.join(L)
print(L)
print(L[3:9])
print(L[3:9][::-1])
value=int(L[3:9][::-1])
print(value)
print(bin(value))
print(oct(value))
print(hex(value))