'''
https://blog.csdn.net/Trisyp/article/details/106373924
https://blog.csdn.net/qq_39798423/article/details/89283000  //可以参考不同检验方法
https://blog.csdn.net/weixin_45709844/article/details/118404635?spm=1001.2101.3001.6650.13&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-13-118404635-blog-122460588.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-13-118404635-blog-122460588.pc_relevant_default&utm_relevant_index=17
https://www.bing.com/ck/a?!&&p=0dc353abd06a7b60b44b34193b0ddd0a6ebb59f369e0a6941d62a4ed73503ef8JmltdHM9MTY1MzI4Mjk4MSZpZ3VpZD1iZDA4ODc0YS01MmYxLTRmN2EtYWYxOC03MGQzYTU4OWE1ODkmaW5zaWQ9NTQwNQ&ptn=3&fclid=7b618e8a-da57-11ec-9931-bf46d86cdf59&u=a1aHR0cHM6Ly96aHVhbmxhbi56aGlodS5jb20vcC8xNjEwMzcyNDIjOn46dGV4dD0lRTclODElQjAlRTglODklQjIlRTklQTIlODQlRTYlQjUlOEIlRTYlOTglQUYlRTQlQjglODAlRTclQTclOEQlRTUlQUYlQjklRTUlOTAlQUIlRTYlOUMlODklRTQlQjglOEQlRTclQTElQUUlRTUlQUUlOUElRTUlOUIlQTAlRTclQjQlQTAlRTclOUElODQlRTclQjMlQkIlRTclQkIlOUYlRTglQkYlOUIlRTglQTElOEMlRTklQTIlODQlRTYlQjUlOEIlRTclOUElODQlRTYlOTYlQjklRTYlQjMlOTUlRTMlODAlODIuLCVFNyU4MSVCMCVFOCU4OSVCMiVFOSVBMiU4NCVFNiVCNSU4QiVFOSU4MCU5QSVFOCVCRiU4NyVFOSU4OSVCNCVFNSU4OCVBQiVFNyVCMyVCQiVFNyVCQiU5RiVFNSU5QiVBMCVFNyVCNCVBMCVFNCVCOSU4QiVFOSU5NyVCNCVFNSU4RiU5MSVFNSVCMSU5NSVFOCVCNiU4QiVFNSU4QSVCRiVFNyU5QSU4NCVFNyU5QiVCOCVFNSVCQyU4MiVFNyVBOCU4QiVFNSVCQSVBNiVFRiVCQyU4QyVFNSU4RCVCMyVFOCVCRiU5QiVFOCVBMSU4QyVFNSU4NSVCMyVFOCU4MSU5NCVFNSU4OCU4NiVFNiU5RSU5MCVFRiVCQyU4QyVFNSVCOSVCNiVFNSVBRiVCOSVFNSU4RSU5RiVFNSVBNyU4QiVFNiU5NSVCMCVFNiU4RCVBRSVFOCVCRiU5QiVFOCVBMSU4QyVFNyU5NCU5RiVFNiU4OCU5MCVFNSVBNCU4NCVFNyU5MCU4NiVFNiU5RCVBNSVFNSVBRiVCQiVFNiU4OSVCRSVFNyVCMyVCQiVFNyVCQiU5RiVFNSU4RiU5OCVFNSU4QSVBOCVFNyU5QSU4NCVFOCVBNyU4NCVFNSVCRSU4QiVFRiVCQyU4QyVFNyU5NCU5RiVFNiU4OCU5MCVFNiU5QyU4OSVFOCVCRSU4MyVFNSVCQyVCQSVFOCVBNyU4NCVFNSVCRSU4QiVFNiU4MCVBNyVFNyU5QSU4NCVFNiU5NSVCMCVFNiU4RCVBRSVFNSVCQSU4RiVFNSU4OCU5NyVFRiVCQyU4QyVFNyU4NCVCNiVFNSU5MCU4RSVFNSVCQiVCQSVFNyVBQiU4QiVFNyU5QiVCOCVFNSVCQSU5NCVFNyU5QSU4NCVFNSVCRSVBRSVFNSU4OCU4NiVFNiU5NiVCOSVFNyVBOCU4QiVFNiVBOCVBMSVFNSU5RSU4QiVFRiVCQyU4QyVFNCVCQiU4RSVFOCU4MCU4QyVFOSVBMiU4NCVFNiVCNSU4QiVFNCVCQSU4QiVFNyU4OSVBOSVFNiU5QyVBQSVFNiU5RCVBNSVFNSU4RiU5MSVFNSVCMSU5NSVFOCVCNiU4QiVFNSU4QSVCRiVFNyU5QSU4NCVFNyU4QSVCNiVFNSU4NiVCNSVFMyU4MCU4Mi4lMjAlRTUlODUlQjYlRTclOTQlQTglRTclQUQlODklRTYlOTclQjYlRTglQjclOUQlRTglQTclODIlRTYlQjUlOEIlRTUlODglQjAlRTclOUElODQlRTUlOEYlOEQlRTYlOTglQTAlRTklQTIlODQlRTYlQjUlOEIlRTUlQUYlQjklRTglQjElQTElRTclODklQjklRTUlQkUlODElRTclOUElODQlRTQlQjglODAlRTclQjMlQkIlRTUlODglOTclRTYlOTUlQjAlRTklODclOEYlRTUlODAlQkMlRTYlOUUlODQlRTklODAlQTAlRTclODElQjAlRTglODklQjIlRTklQTIlODQlRTYlQjUlOEIlRTYlQTglQTElRTUlOUUlOEIlRUYlQkMlOEMlRTklQTIlODQlRTYlQjUlOEIlRTYlOUMlQUElRTYlOUQlQTUlRTYlOUYlOTAlRTQlQjglODAlRTYlOTclQjYlRTUlODglQkIlRTclOUElODQlRTclODklQjklRTUlQkUlODElRTklODclOEYlRUYlQkMlOEMlRTYlODglOTYlRTglQkUlQkUlRTUlODglQjAlRTYlOUYlOTAlRTQlQjglODAlRTclODklQjklRTUlQkUlODElRTklODclOEYlRTclOUElODQlRTYlOTclQjYlRTklOTclQjQlRTMlODAlODIu&ntb=1
'''

import pandas as pd
import numpy as np

# 级比检验，建模可行性分析
def step_ratio(x0):
    n = len(x0)
    ratio = [x0[i] / x0[i + 1] for i in range(len(x0) - 1)]
    print(f"级比：{ratio}")
    min_la, max_la = min(ratio), max(ratio)
    thred_la = [np.exp(-2 / (n + 1)), np.exp(2 / (n + 1))]
    if min_la < thred_la[0] or max_la > thred_la[-1]:
        print("级比超过灰色模型的范围")
    else:
        print("级比满足要求，可用GM(1,1)模型")
    return ratio, thred_la

# GM模型搭建
def GM(x0):
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
    return x0_solve, x1_solve, u, u[0], u[1]

# 相对误差检验法
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

# 预测指定预测步长值
def predict(x0, a, b, pre_step):
    n = len(x0) + pre_step
    result_x1 = np.zeros(n)
    result_x0 = np.zeros(n)
    result_x1[0] = result_x0[0] = x0[0]
    for i in range(1, n):
        result_x1[i] = (x0[0] - b / a) * np.exp(-u[0] * i) + b / a
    for i in range(1, n):
        result_x0[i] = result_x1[i] - result_x1[i - 1]
    return result_x0


if __name__ == '__main__':
    data = pd.DataFrame(
        data={"year": [1986, 1987, 1988, 1989, 1990, 1991, 1992], "eqL": [71.1, 72.4, 72.4, 72.1, 71.4, 72.0, 71.6]})
    x0 = np.array(data.iloc[:, 1])
    ratio, thred_la = step_ratio(x0)
    x0_solve, x1_solve, u ,a ,b= GM(x0)
    pre_result = predict(x0, a, b, 5)
    epsilon, delta, rho, P = accuracy(x0, x0_solve, ratio, u)
