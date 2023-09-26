# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:13:06 2021

@author: xingyu
"""

from dictionary import get2500,get3500
     
#dic = dic[:1000]    
poetrycloud = [""]

dic = get3500()

def dfs(n):
    global poetrycloud
    print(n)
    if n <= 0:
        return ;
    print("len::",len(poetrycloud))
    tmp = []
    for _,s in enumerate(poetrycloud):
        
        for _,word in enumerate(dic):
            ts = s
            ts += word
            #print(ts)
            tmp.append(ts)
    poetrycloud = tmp
    n -= 1
    dfs(n)


def poetry2num(poetry):
    res = 0
    for i in range(len(poetry)):
        res *= len(dic)
        res += (dic.index(poetry[i])+1)
    return res

def num2poetry(num):
    res = ""
    while num != 0:
        res += dic[int(num%(len(dic)))-1]
        num //= len(dic)
    return res[::-1]
    

#dfs(1)
if __name__ == "__main__":
    f = ' '
    while f != 'Q' and f != 'q':
        poetry = "床前明月光疑是地上霜举头望明月低头思故乡"#"啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊哎"
        print("1.数字转诗\n2.诗转数字")
        f = int(input("你的选择是："))
        if f == 2:
            poetry = input("输入诗：")
            num = poetry2num(poetry)
            print(int(num))
        if f == 1:
            num = int(input("输入数字："))
            poetry = num2poetry(num)
            print(poetry)
        f = input("Q/q退出")























