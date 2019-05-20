# -*- coding: utf-8 -*-
# @Time    : 19-5-20 上午10:40
# @Author  : Redtree
# @File    : main.py
# @Desc :

#直接插入排序
from func import insert_sort
#希尔排序
from func import insert_shell
#冒泡排序
from func import bubble_sort
#堆排序
from func import heap_sort
#归并排序
from func import mergearray_sort
#快速排序(递归)
from func import quick_sort
#基数排序
from func import radix_sort
#自由选择排序
from func import select_sort

L = [18,22,2,1,7,5,9]
#执行排序并查看结果
res = radix_sort.dosort(L)
print(res)