# -*- coding: utf-8 -*-
# @Time    : 19-5-20 上午10:34
# @Author  : Redtree
# @File    : select_sort.py
# @Desc :  简单选择排序

def dosort(L):
    #依次遍历序列中的每一个元素
    for x in range(0,len(L)):
    #将当前位置的元素定义此轮循环当中的最小值
        minimum = L[x]
        #将该元素与剩下的元素依次比较寻找最小元素
        for i in range(x+1,len(L)):
            if L[i] < minimum:
                temp = L[i];
                L[i] = minimum;
                minimum = temp
        #将比较后得到的真正的最小值赋值给当前位置
        L[x] = minimum

    return L