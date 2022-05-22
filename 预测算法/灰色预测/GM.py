'''
https://blog.csdn.net/Trisyp/article/details/106373924
https://blog.csdn.net/qq_66183206/article/details/123136657
https://blog.csdn.net/weixin_45709844/article/details/118404635?spm=1001.2101.3001.6650.13&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-13-118404635-blog-122460588.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-13-118404635-blog-122460588.pc_relevant_default&utm_relevant_index=17
'''

import pandas as pd
import numpy as np


def step_ratio(x0):
    n = len(x0)
    ratio = [x0[i] / x0[i + 1] for i in range(len(x0) - 1)]
    print(f"级比：{ratio}")
    min_la, max_la = min(ratio), max(ratio)
    thred_la = [np.exp(-2 / (n + 2)), np.exp(2 / (n + 2))]
    if min_la < thred_la[0] or max_la > thred_la[-1]:
        print("级比超过灰色模型的范围")
    else:
        print("级比满足要求，可用GM(1,1)模型")
    return ratio, thred_la


def predict(x0):
    n = len(x0)
    x1 = np.cumsum(x0)
    z = np.zeros(n - 1)
    for i in range(n - 1):
        z[i] = 0.5 * (x1[i] + x1[i + 1])
    B = [-z, [1] * (n - 1)]
    Y = x0[1:]
    u = np.dot(np.linalg.inv(np.dot(B, np.transpose(B))), np.dot(B, Y))
    x1_solve = np.zeros(n)
    x0_solve = np.zeros(n)
    x1_solve[0] = x0_solve[0] = x0[0]
    for i in range(1, n):
        x1_solve[i] = (x0[0] - u[1] / u[0]) * np.exp(-u[0] * i) + u[1] / u[0]
    for i in range(1, n):
        x0_solve[i] = x1_solve[i] - x1_solve[i - 1]
    return x0_solve, x1_solve, u


def accuracy(x0, x0_solve, ratio, u):
    epsilon = x0 - x0_solve
    delta = abs(epsilon / x0)
    print(f"相对误差：{delta}")
    # Q = np.mean(delta)
    # C = np.std(epsilon)/np.std(x0)
    S1 = np.std(x0)
    S1_new = S1 * 0.6745
    temp_P = epsilon[abs(epsilon - np.mean(epsilon)) < S1_new]
    P = len(temp_P) / len(x0)
    print(f"预测准确率：{P * 100}%")
    ratio_solve = [x0_solve[i] / x0_solve[i + 1] for i in range(len(x0_solve) - 1)]
    rho = [1 - (1 - 0.5 * u[0] / u[1]) / (1 + 0.5 * u[0] / u[1]) * (ratio[i] / ratio_solve[i]) for i in
           range(len(ratio))]
    print(f"级比偏差：{rho}")
    return epsilon, delta, rho, P


if __name__ == '__main__':
    data = pd.DataFrame(
        data={"year": [1986, 1987, 1988, 1989, 1990, 1991, 1992], "eqL": [71.1, 72.4, 72.4, 72.1, 71.4, 72.0, 71.6]})
    x0 = np.array(data.iloc[:, 1])
    ratio, thred_la = step_ratio(x0)
    x0_solve, x1_solve, u = predict(x0)
    epsilon, delta, rho, P = accuracy(x0, x0_solve, ratio, u)
