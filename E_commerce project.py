#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import libaries

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)


# In[4]:


web_df = pd.read_csv(r"website_success_sites - website_success_sites.csv",
                     parse_dates=["publish_date"],
                     infer_datetime_format=True,
                    )
sales_df = pd.read_csv(r"website_success_transactions.csv",
                     parse_dates=["timestamp"],
                     infer_datetime_format=True,
                      )
                            


# In[5]:


web_df.head()


# In[6]:


sales_df.head()


# In[7]:


sales_df.info(show_counts=True)


# In[8]:


sales_df.shape


# In[9]:


sales_df.describe()


# In[10]:


sales_df.isna().sum()


# In[11]:


web_df.info(show_counts=True)


# In[12]:


web_df.count()


# In[13]:


web_df.isna().sum()


# In[14]:


web_df['country'] = web_df['country'].fillna('Unknown')
web_df['type'] = web_df['type'].fillna('Unknown')
web_df['industry'] = web_df['industry'].fillna('Unknown')


# # 2. Prepare & clean the Data

# --- web_df ---

# In[23]:


#variable type change and capitalize fix

web_df = web_df.astype({'country': 'string', 'type': 'string', 'industry': 'string'})
web_df['country'] = web_df['country'].str.lower()
web_df['country'] = web_df['country'].str.title()


# In[24]:


# publish date validation

web_df['publish_date'].dt.year.unique()


# In[25]:


sales_df = sales_df.loc[sales_df['timestamp'].dt.year>2020]
sales_df['timestamp'].dt.year.unique()


# In[26]:


# df Merging

merged_df = web_df.merge(sales_df,how="left",left_on=["guid"],right_on=["site_guid"],)


# In[27]:


merged_df


# In[28]:


merged_df.info()


# In[29]:


merged_df.drop(['site_guid','last_browser','last_device_type','last_ip','last_screen_resolution','last_os'],axis=1,inplace=True)


# In[46]:


# Bar plot of country distribution
country_counts = merged_df['country'].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Distribution of Countries')
plt.xticks(rotation=90)
plt.show()


# In[45]:


# Grouping data by industry and calculating average price
avg_price_by_industry = merged_df.groupby('industry')['price_usd'].mean()

plt.figure(figsize=(6, 4))
sns.barplot(x=avg_price_by_industry.index, y=avg_price_by_industry.values)
plt.xlabel('Industry')
plt.ylabel('Average Price (USD)')
plt.title('Average Price by Industry')
plt.xticks(rotation=90)
plt.show()


# In[43]:


# Pie chart of type distribution with smaller size and aspect ratio
type_counts = merged_df['type'].value_counts()
plt.figure(figsize=(6, 4))  # Decrease the figure size here
plt.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Types')
plt.gca().set_aspect('equal')  # Set aspect ratio to make it more circular
plt.show()


# In[44]:


# Box plot of price by industry
plt.figure(figsize=(6, 4))
sns.boxplot(x=merged_df['industry'], y=merged_df['price_usd'])
plt.xlabel('Industry')
plt.ylabel('Price (USD)')
plt.title('Price Distribution by Industry')
plt.xticks(rotation=90)
plt.show()

