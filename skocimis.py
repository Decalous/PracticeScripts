# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:56:23 2022

Solves problem from: https://open.kattis.com/problems/skocimis
@author: Dan
"""

import sys

inp = sys.stdin.readline().split()
for i in range(len(inp)):
    inp[i] = int(inp[i])
diff1 = inp[1] - inp[0]
diff2 = inp[2] - inp[1]
if diff1 > diff2:
    print(diff1 - 1)
else:
    print(diff2 - 1)