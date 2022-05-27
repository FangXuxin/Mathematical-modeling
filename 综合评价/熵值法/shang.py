'''
Time : 2022/1/18 16:37
File : cal.py
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def postive_change(li):
    list = li
    Min = min(list); Max = max(list)
    for i in range(len(list)):
        list[i] = ( list[i]-Min ) / ( Max-Min ) + 1
    return list

def reverse_change(li):
    list = li
    Min = min(list); Max = max(list)
    for i in range(len(list)):
        list[i] = ( Max-list[i] ) / ( Max-Min ) + 1
    return list

def neutral_change(li):
    list = li
    Min = min(list); Max = max(list); mean = np.mean(list)
    # print(mean)
    for i in range(len(list)):
        if list[i] < mean:
            list[i] = ( list[i]-Min ) / ( Max-Min ) + 1
        else:
            list[i] = ( Max-list[i] ) / ( Max-Min ) + 1
    return list

def cal_weight(data):
    #   标准化 (看情况修改)
    std_data = []
    # for i in range(len(data)):  #w、l、e
    #     if i == 0:
    #         # print(data[i])
    #         temp = postive_change(data[i])
    #         std_data.append(temp)
    #     elif i == 1:
    #         temp = reverse_change(data[i])
    #         std_data.append(temp)
    #     else:
    #         temp = postive_change(data[i])
    #         std_data.append(temp)
    for item in data:
        temp = postive_change(item)
        std_data.append(temp)
    print('标准化数据：',std_data)

    #   求比值Pij
    P = []
    for i in std_data:
        Sum = sum(i)
        templi = []
        for j in i:
            templi.append(round(j / Sum, 4))
        P.append(templi)
    print('比值Pij：',P)

    #   求信息熵
    E = []
    for j in range(len(std_data)):  # 注意循环长度
        S = 0
        for k in P[j]:
            S = S + k * np.log(k)
        ej = -1/np.log(len(P[j]))*S
        E.append(round(ej,4))
    print('信息熵E：',E)

    #   求效用
    Gj = []
    for i in E:
        Gj.append(round(1 - i, 4))
    print('效用：',Gj)

    #求权重w
    Wj = []
    for i in Gj:
        Wj.append(round( i / sum(Gj), 4))
    print('权重：',Wj)

    return Wj



def main():
    Data = pd.read_excel('test.xlsx')
    data = []
    for i in range(1, len(Data.columns)):
        data.append(list(Data.iloc[:,i]))


    # 熵值法计算权重
    Weight = cal_weight(data)

    # 计算分数
    score = np.dot(np.array(data), np.array(Weight))
    print('最终比分结果为：', score)

    Data.insert(6,'比分',score)
    Data.to_excel('评分后.xlsx')



if __name__ == '__main__':
    main()