import matplotlib.pyplot as mp
# 训练集
y = [.4187, .0964, .0853, .0305, .0358, .0338, .0368, .0222, .0798, .1515]
x = [[i]for i in range(len(y))]
# 待测集
w = [[i / 100 * len(y)] for i in range(100)]

def modeling(models):
    n = len(models)
    for i in range(n):
        # 建模、拟合
        models[i].fit(x, y)
        # 预测
        z = models[i].predict(w)
        # 可视化
        mp.subplot(1, n, i + 1)
        mp.scatter(x, y, s=22, color='g')
        mp.scatter(w, z, s=2, color='r')
        mp.show()

from sklearn.tree import DecisionTreeRegressor
modeling([
    DecisionTreeRegressor(max_depth=1),
    DecisionTreeRegressor(max_depth=2),
    DecisionTreeRegressor(max_depth=3),
    DecisionTreeRegressor(max_depth=4),
    DecisionTreeRegressor(),
])
