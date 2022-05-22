'''
PCA模板
'''

import random
import numpy as np
import pandas as pd
from scipy.stats import zscore
# 创造模拟数据
# df = pd.DataFrame(columns = ['每周跑单数','办公时间','身体素质'])
#
# for i in range(1000):
#     df.loc[i] = {'每周跑单数':random.randint(0,50),'办公时间':random.uniform(24,24*5),'身体素质':random.uniform(0,100)}
#
# df.index = df.index + 1
#
# df.to_excel('企业综合能力分析.xlsx')

# PCA
from sklearn.decomposition import PCA

df = pd.read_excel('企业综合能力分析.xlsx')
a = df.drop('Unnamed: 0', axis=1)
data = np.array(a)
data = zscore(data);print(data)

# 相关参数的计算 ----------------------------------------------------------------
print('相关系数矩阵：',np.around(np.corrcoef(data.T),decimals=3))  #输出相关系数矩阵
value, vector = np.linalg.eig(np.corrcoef(data.T))  # 求特征值和特征向量
print('特征值：{} \n特征向量：{}'.format(value, vector))
rate = value / value.sum()
print("各主成分的贡献率为：", rate);print('-'*50)

# PCA模块的使用-----------------------------------------------------------------
result = PCA(n_components=0.85).fit(data)  #使用PCA模块训练使得贡献率>85%
print('特征值：', result.explained_variance_)
print("主成分的贡献率：", result.explained_variance_ratio_)
print("奇异值：", result.singular_values_)
print("各主成分的系数：\n", result.components_)


print('-'*50)
k = 1  # 提出主成分的个数
F = vector[:, :k]
score_mat = data.dot(F)  # 计算主成分得分矩阵
score1 = score_mat.dot(rate[0:k])  # 计算各评价对象的得分
score2 = -score1  # 通过表中数据以及score1观测，需要调整得分的正负号
print("各评价对象的得分为：", score2)
index = score1.argsort() + 1  # 排序后的每个元素在原数组中的位置
print("从高到低各个城市的编号排序为：", index)

df.insert(1,'score',0)
print(df)

for i in range(1000):
    df.loc[i,'score'] = index[i]

# df.sort_values(by="score" , inplace=True, ascending=True)   # 按照分数排序

df.to_excel('PCA排序后.xlsx')


