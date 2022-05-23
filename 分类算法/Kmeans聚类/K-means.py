'''
https://www.cnblogs.com/heenhui2016/p/10988892.html 可主要参考 https://blog.csdn.net/qq_38563206/article/details/120435976
https://blog.csdn.net/guihenao4010/article/details/85159661
https://blog.csdn.net/momokofly/article/details/121897291
https://blog.csdn.net/weixin_37763870/article/details/103212986
https://blog.csdn.net/qq_46556714/article/details/124893860     手动实现
'''

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
X, _ = make_blobs(n_samples=500, # 500个样本
                 n_features=2, # 每个样本2个特征
                 centers=4, # 4个中心
                 random_state=1 #控制随机性
                 )


y_pred = KMeans(n_clusters=3).fit_predict(X)
cluster = KMeans(n_clusters=3).fit(X)
centroid=cluster.cluster_centers_   # 质心
inertia=cluster.inertia_
print(centroid,inertia)
color=['red','pink','orange','gray']
fig, axi1=plt.subplots(1)
for i in range(3):
    axi1.scatter(X[y_pred==i, 0], X[y_pred==i, 1],
               marker='o',
               s=8,
               c=color[i])
axi1.scatter(centroid[:,0],centroid[:,1],marker='x',s=100,c='black')
plt.show()


