'''
https://juejin.cn/post/6986452378018906149  # 参考
https://zhuanlan.zhihu.com/p/78382376   # 理论
'''
import random

import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster


data = np.array([[1, 2], [2, 3], [-3, 3], [-2, -1], [5, -1]])
X = []

'''sklearn 实现层次聚类'''
# 画点
plt.scatter(x=data[:, 0:1], y=data[:, 1:2], marker='.', color='red')
n = np.arange(data.shape[0])
for i, txt in enumerate(n):
    plt.annotate(txt, (data[i:i + 1, 0:1], data[i:i + 1, 1:2]))
plt.show()

# 训练模型
ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='average')
clustering = ac.fit(data)

print("每个数据所属的簇编号", clustering.labels_)
print("每个簇的成员", clustering.children_)



'''Scipy实现层次聚类'''
Z = linkage(data, 'average')
print("聚类过程：", Z)
f = fcluster(Z, 4, 'distance')
print("平面聚类结果：", f)
fig = plt.figure(figsize=(5, 3))
dn = dendrogram(Z)
plt.show()