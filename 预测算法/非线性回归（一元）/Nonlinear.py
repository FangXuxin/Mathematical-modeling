'''
https://blog.csdn.net/OldDriver1995/article/details/105240965
'''
import pandas as pd
import numpy as np
import matplotlib
import random
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 数据部分
x = np.array(range(30))
temp_y = 10 + 2*x + x**2 + x**3
y = temp_y + 1500*np.random.normal(size=30)  #添加噪声

x = x.reshape(30,1)
y = y.reshape(30,1)

#线性回归
clf1 = LinearRegression()
clf1.fit(x,y)
y_l = clf1.predict(x)  #线性回归预测值

#非线性回归
ployfeat = PolynomialFeatures(degree=3)  #根据degree的值转换为相应的多项式（非线性回归）
x_p = ployfeat.fit_transform(x)
clf2 = LinearRegression()
clf2.fit(x_p,y)

font={"family":"FangSong",'size':12}
matplotlib.rc("font",**font)
plt.figure(figsize = (12,6))
plt.plot(x,y_l,label = "线性回归")
plt.scatter(x,y,label="real value")
plt.plot(x,np.matmul(x_p,clf2.coef_.reshape(4,1)) + clf2.intercept_,label="非线性回归")
plt.legend()
plt.show()

print("线性回归方程为: y = {} + {}x".format(clf1.intercept_[0],clf1.coef_[0,0]))
print("非线性回归曲线方程为 y = {}+{}x+{}x^2+{}x^3".format(clf2.intercept_[0],clf2.coef_[0,1],clf2.coef_[0,2],clf2.coef_[0,3]))

