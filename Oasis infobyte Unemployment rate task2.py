#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[52]:


df=pd.read_csv('Unemployment in india.csv')
df=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
df


# In[53]:


df.head()


# In[54]:


df.shape


# In[55]:


df.info()


# In[56]:


df.columns


# In[57]:


df.describe()


# In[58]:


df['Region'].unique()


# In[59]:


df['Region'].value_counts()


# In[60]:


print(df.isnull().sum())


# In[61]:


df.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]


# In[62]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr())
plt.show()


# In[63]:


df.columns= ["Region","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Area",
               "longitude","latitude"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=df)
plt.show()


# In[64]:


plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=df)
plt.show()


# In[65]:


unemploment = df[["Area", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemploment, path=["Region", "Area"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")


# In[66]:


figure.show()


# In[ ]:




