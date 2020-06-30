#!/usr/bin/env python
# coding: utf-8

# 

# In[13]:


# 使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 数据加载
file = "C:\\Users\\Administrator\\Desktop\\Data_Engine_with_Python-master\\Data_Engine_with_Python-master\\L3\\car_data.csv"
#data = pd.read_csv('Mall_Customers.csv', encoding='gbk')
headers = ['地区','人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']
#?pd.read_csv
data = pd.read_csv(file, encoding='gbk', names =headers,skiprows=1)
#print(data.index)
#print(data['city'])
#data = data[1:]
#data.drop(index = [i for i in data.index if i==0], inplace = True)
print(data)


# In[16]:


train_header = headers[1:]
train_x = data[train_header]

# LabelEncoder
#from sklearn.preprocessing import LabelEncoder
#le = LabelEncoder()
#train_x['Gender'] = le.fit_transform(train_x['Gender'])

# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index=False)
#print(train_x)


### 使用KMeans聚类
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
get_ipython().run_line_magic('pinfo', 'result.to_csv')
result.to_csv("customer_cluster_result.csv",index=False,encoding='gbk')


# In[ ]:




