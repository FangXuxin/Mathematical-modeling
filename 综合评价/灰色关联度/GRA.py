'''
https://blog.csdn.net/weixin_43196531/article/details/106663262
'''

import pandas as pd
import numpy as np
# columns=['地区','GDP增长速度','第三产业增加值占比','每万人拥有卫生技术人员数','亩产GDP','森林覆盖率%']
# df = pd.DataFrame(columns=columns)
# data = [
#     ['北京市','天津市','河北省','山西省','内蒙古自治区'],
#     [1.184563,1.129583,1.133322,1.180564,1.241990],
#     [0.734873,0.428354,0.338106,0.374804,0.384142],
#     [85.551745,57.021525,35.029382,42.782788,43.987526],
#     [56.731060,15.037962,2.971666,4.797721,2.280457],
#     [21.3,8.1,17.7,13.3,17.7]
# ]
#
# for i,item in enumerate(columns):
#     df[item] = data[i]
#
# df.to_excel('test.xlsx',index=False)

df = pd.read_excel('test.xlsx')

df = df.set_index('地区')

n = list(df.columns)
for i in n:
    df[i] = df[i] / np.average(df[i])

# 这里以最优值为参考数列
A1 = []
# 获取最优列值
for i in n:
    Max = np.max(df[i])
    A1.append(Max)

# 转换形式
A1 = np.array(A1)

m = len(df)
for i in range(m):
    df[i:i+1] = abs(df[i:i+1] - A1)

# 最大值
MAX = []
# 每个指标的最大值
for i in n:
    l = max(df[i])
    MAX.append(l)

MAX = max(MAX)

# 最小值
MIN = []
# 每个指标的最小值
for i in n:
    l = min(df[i])
    MIN.append(l)

MIN = min(MIN)

# 这里 rho 为0.5，可自行调整
for i in n:
    df[i] = (MIN + 0.5 * MAX) / (df[i] + 0.5 * MAX)


score = []
for i in range(m):
    s = sum(df.iloc[i].values)/len(n)
    score.append(s)

result = pd.DataFrame(score, index = df.index, columns = ['综合得分'])
result.index.name = '地区'
# 排序
result['排序'] = result.rank(ascending = False)
print(result)
# 保存为excel
result.to_excel("综合得分.xlsx")
