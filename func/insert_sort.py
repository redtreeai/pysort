# -*- coding: utf-8 -*-
# @Time    : 19-5-20 上午10:33
# @Author  : Redtree
# @File    : insert_sort.py
# @Desc :  直接插入排序

#----直接插入排序----
def dosort(L):
    #遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
    for x in range(1,len(L)):
    #将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
    #range(x-1,-1,-1):从x-1倒序循环到0
        for i in range(x-1,-1,-1):
    #判断：如果符合条件则交换
            if L[i] > L[i+1]:
                temp = L[i+1]
                L[i+1] = L[i]
                L[i] = temp

    return L