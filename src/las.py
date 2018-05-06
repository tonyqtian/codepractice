# -*- encoding: utf-8 -*-

"""
@version: 0.01
@author: Tony Qiu
@contact: tony.qiu@liulishuo.com
@file: las.py
@time: 2018/04/19 午後5:56
"""

def max_ascend_len(ary):
    maxlist = []
    if len(ary) == 0:
        return 0
    start = 0
    end = 0
    for idx in range(1, len(ary)):
        if ary[idx] > ary[idx-1]:
            end = idx
        else:
            maxlist.append(end-start+1)
            end = idx
            start = idx
    return max(maxlist)

a = [2,1,4,3,1,5,6]
print(max_ascend_len(a))