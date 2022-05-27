'''
Time : 2022/1/18 16:37 
File : cal.py 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(path):
    data = pd.read_csv(path)
    name = data.iloc[:,0].tolist()
    dic1 = {}; dic2 = {}
    for i in range(len(name)):
        dic1[name[i]] = data.iloc[i,1:].tolist()

    n = 0
    for k in data.columns.tolist():
        dic2[k] = data.iloc[:,n].tolist()
        n += 1
    return dic1, dic2

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

def Plot_result(score,ctg):
    X = list(range(1, len(score) + 1)); Y = []
    # 结果重排序
    T = list(score.items())
    T.sort(key=lambda x: x[1], reverse=True)
    temp_score = dict(T)

    rank = 1
    for k, v in temp_score.items():
        temp_score[k] = rank
        rank += 1
    print(ctg + ' 重排序结果：',temp_score)

    for k, v in score.items():
        for i, j in temp_score.items():
            if i == k:
                Y.append(j)
    # print(Y)
    # 绘图
    '''英文'''
    plt.scatter(X, X, label='The original rank', color='r', s=10)
    plt.scatter(X, Y, label='Ranking by entropy'+'('+ctg+')', color='b', s=10)
    plt.xlabel('Player Number')
    plt.ylabel('Rank Number')
    plt.title('Entropy-based ranking compared with the original ranking'+'('+ctg+')')
    plt.legend()
    plt.show()

    # '''中文'''
    # plt.scatter(X, X, label='原始排名', color='r', s=10)
    # plt.scatter(X, Y, label='熵值法排名' + '(' + ctg + ')', color='b', s=10)
    # plt.xlabel('球员序号')
    # plt.ylabel('名次')
    # plt.title('熵值法评价后排名和原排名对比图' + '(' + ctg + ')')
    # plt.legend()
    # plt.show()

def cal_weight(data):
    #   标准化
    std_data = []
    for i in range(3):  #w、l、e
        if i == 0:
            # print(data[i])
            temp = postive_change(data[i])
            std_data.append(temp)
        elif i == 1:
            temp = reverse_change(data[i])
            std_data.append(temp)
        else:
            temp = postive_change(data[i])
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
    for j in range(3):  #w、l、e
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
    Path = {'MS':'csv_data\MS.csv',
            'WS':'csv_data\WS.csv',
            'MD':'csv_data\MD.csv',
            'WD':'csv_data\WD.csv',
            'MIXD':'csv_data\MIXD.csv'}

    for key, value in Path.items():
        print('-'*1000)
        path = value
        # 导入数据
        Data, w_data = load_data(path)
        data = []
        for k in w_data:
            if k != 'Unnamed: 0':
                data.append(w_data[k])

        # 熵值法计算权重
        Weight = cal_weight(data)

        # 计算分数
        score = {}
        for k,v in Data.items():
            # print(k,v)
            score[k] = round(sum(list(np.multiply(v,Weight))),4)
        print('%s 的最终结果为：' % key,score)

        # 画图
        Plot_result(score,key)


if __name__ == '__main__':
    main()