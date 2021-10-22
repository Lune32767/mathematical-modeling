#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/10/16 15:29
@Author :LuneD
@File   :numb2_code.py
"""

import matplotlib
from sklearn import metrics
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#训练集使用已经筛选出来的20个特征
dataSet = pd.read_csv(r'D:\csv\writer.csv', header=0)

featureArray = dataSet.columns[1:21]
resArryay = dataSet.columns[0]
X = dataSet[featureArray]
y = dataSet[resArryay]
names = featureArray

#测试集为0.2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

rf = RandomForestRegressor(n_estimators=141, max_depth=None)

#拟合
rf.fit(X_train, y_train)

#y_pred是预测值
y_pred = rf.predict(X_test)

# 评估回归性能
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#开始画图

#指定字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']=['sans-serif']

# 画出数据的散点图
fig = plt.figure()  # 整个绘图区分成一行两列，当前图是第一个。

#绘图区域大小
fig.set_size_inches(7, 7)

colors1 = '#00CED1' #点的颜色
colors2 = '#DC143C'
area = np.pi * 4**2  # 点面积

#length是测试机集合的数量，这里是395
length = len(y_test)
# # 画出数据和拟合直线的图

plt.scatter(list(y_test), list(y_pred), s=area, c=colors1, alpha=0.4)

plt.plot([3, 9.5], [3, 9.5], linewidth='1.5', color='#000000')

plt.xlabel('pIC$_{50}$_p', fontdict={'weight': 'normal', 'size': 13})
plt.ylabel('pIC$_{50}$_r', fontdict={'weight': 'normal', 'size': 13})

plt.title("pIC训练集内拟合结果")
plt.savefig(r'D:\csv\pIC拟合结果.png', dpi=300)

plt.show()
