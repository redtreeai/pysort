# -*- coding: utf-8 -*-
# @Time    : 19-5-20 上午10:34
# @Author  : Redtree
# @File    : insert_shell.py
# @Desc :   希尔排序

#----希尔排序----
def dosort(L):
    #初始化gap值，此处利用序列长度的一般为其赋值
    gap = (int)(len(L)/2)
    #第一层循环：依次改变gap值对列表进行分组
    while (gap >= 1):
    #下面：利用直接插入排序的思想对分组数据进行排序
    #range(gap,len(L)):从gap开始
        for x in range(gap,len(L)):
    #range(x-gap,-1,-gap):从x-gap开始与选定元素开始倒序比较，每个比较元素之间间隔gap
            for i in range(x-gap,-1,-gap):
    #如果该组当中两个元素满足交换条件，则进行交换
                if L[i] > L[i+gap]:
                    temp = L[i+gap]
                    L[i+gap] = L[i]
                    L[i] =temp
    #while循环条件折半
        gap = (int)(gap/2)

    return L