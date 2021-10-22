#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time   :2021 2021/10/16 21:00
@Author :LuneD
@File   :num3_2_pie.py
"""


import matplotlib
import matplotlib.pyplot as plt
import xgboost
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# load data
dataSet = pd.read_csv(r'D:\csv\DSM3.csv', header=0)

len = dataSet.columns
#len长度为476
featureArray = dataSet.columns[5:476]
names = featureArray
res = dataSet.columns[2]

#训练集
X = dataSet[featureArray]
#测试集
y = dataSet[res]

seed = 7

#分成7次模型可以
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


#开始画图

#指定字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']=['sans-serif']

# 画出数据的散点图
fig = plt.figure()  # 整个绘图区分成一行两列，当前图是第一个。

#绘图区域大小
fig.set_size_inches(7, 7)


colors1 = '#00CED1' #蓝色
colors2 = '#DC143C' #品红色
colors3 = '#6B8E23' #灰绿色

area = np.pi * 4**2  # 点面积

#length是测试机集合的数量，这里是395
#print(y_test)

length = pd.Series.__len__(y_test)
print(length)

# # 画出数据和拟合直线的图
#真实的值

list1 = list(y_test)
list2 = list(y_pred)
list3=[]
list4=[]
cnt = 0
for index in range(length):
    if list1[index] == list2[index]:
        list3.append(1)
        cnt+=1
    else:
        list3.append(0)



labels = ['正确','错误']
correct = (cnt * 1.0 / length) * 100
failure = 100 - correct
x = [correct, failure]
#显示百分比
#饼图分离
explode = (0, 0.1)
color = ['#F08080', '#BDB76B']
#设置阴影效果
plt.title("hERG样本测试集分类结果饼状图")
plt.pie(x, labels=labels, colors=color,autopct='%3.2f%%', explode=explode, shadow=True)

#设置x,y的刻度一样，使其饼图为正圆
plt.axis('equal')
plt.savefig(r'D:\csv\picture\hERG样本测试集分类结果饼状图.png', dpi=300)
plt.show()