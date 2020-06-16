
# coding: utf-8

# # action1：求2+4+46+8+...+100的求和

# In[2]:


s = sum(range(2,101,2))
s


# # 统计全班的成绩

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


data1={
    '语文':[68,95,98,90,80],
    '数学':[65,76,86,88,90],
    '英语':[30,98,88,77,90]
}
df = pd.DataFrame(data1, index=['张飞','关羽','刘备','典韦','许褚'], columns = ['语文', '数学', '英语'])
df


# In[4]:


print('平均值:\n',df.mean())
print('最小值:\n',df.min())
print('最大值:\n',df.max())
print('方差值:\n',df.var())
print('标准差值:\n',df.std())


# In[5]:


df.sum(axis=1).sort_values(ascending = False)


# # 汽车质量数据的处理

# In[32]:


file_path = "C:\\Users\\xiexujun\\Desktop\\car_complain.csv"
data = pd.read_csv(file_path)
data


# In[33]:



data = data.drop('problem', 1).join(data.problem.str.get_dummies(','))
tags = data.columns[7:] 


df1 = data.groupby(['brand'])['id'].agg(['count'])
df2 = data.groupby(['brand'])[tags].agg(['sum'])
df2 = df1.merge(df2, left_index=True, right_index=True, how='left')
df2.reset_index(inplace=True)
df2 = df2.sort_values('count', ascending=False)
print(df2) 


# In[34]:



df3 = data.groupby(['car_model'])['id'].agg(['count'])
df4 = data.groupby(['car_model'])[tags].agg(['sum'])
df4 = df3.merge(df4, left_index=True, right_index=True, how='left')
df4.reset_index(inplace=True)
df4 = df4.sort_values('count', ascending=False)
print(df4) 


# In[36]:



df_new = data.groupby(['brand'])['A11'].agg(['count'])
df_new.sort_values('count',ascending=False)

