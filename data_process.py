import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "SimHei" #解决中文乱码问题
import seaborn as sns
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn import model_selection
from sklearn.neighbors import KNeighborsRegressor

# 文件路径
filePath = sys.path[0]

# # 导入数据
# df_train1 = pd.read_csv(filePath + os.sep + 'datasets' + os.sep + 'train_format1.csv', encoding='ISO-8859-1')
# df_train2 = pd.read_csv(filePath + os.sep + 'datasets' + os.sep + 'train_format2.csv', encoding='ISO-8859-1')
df_test1 = pd.read_csv(filePath + os.sep + 'datasets' + os.sep + 'test_format1.csv', encoding='ISO-8859-1')
df_test2 = pd.read_csv(filePath + os.sep + 'datasets' + os.sep + 'test_format2.csv', encoding='ISO-8859-1')
# df_user_info = pd.read_csv(filePath + os.sep + 'datasets' + os.sep + 'user_info_format1.csv', encoding='ISO-8859-1')
# df_user_log = pd.read_csv(filePath + os.sep + 'datasets' + os.sep + 'user_log_format1.csv', encoding='ISO-8859-1')

# print(df_train1.shape)
# print(df_train1.head())
# print(df_train2.shape)
# print(df_train2.head())
# print(df_test1.shape)
# print(df_test1.head())
# print(df_test2.shape)
# print(df_test2.head())
# print(df_user_info.shape)
# print(df_user_log.shape)