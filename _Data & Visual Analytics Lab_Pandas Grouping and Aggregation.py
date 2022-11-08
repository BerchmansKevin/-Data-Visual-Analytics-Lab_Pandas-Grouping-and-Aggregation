#!/usr/bin/env python
# coding: utf-8

# # `BERCHMANS KEVIN S`
# 
# 

# ## Department of Data Science - Data and Visual AnalyticsLab
# ##  `Pandas Grouping and Aggregation`

# #### `Import Necessary Modules`

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("thanksgiving-2015-poll-data.csv",encoding='Latin-1')


# In[3]:


#print top 5 rows from data

data.head()


# In[4]:


#what is the size?

data.shape


# ### `What are unique values of "Do you celebrate Thanksgiving?"column?`
# 

# In[5]:


data.iloc[0:,1].unique()


# ### `View all column names (top 5)`

# In[6]:


data.columns[0:6]


# ### Apply function to Series
# ### `How many male,female and NaN in "What is your gender?"column`

# In[7]:


data["What is your gender?"].value_counts(dropna=False)


# In[8]:


#let apply a user defined function to each value in What is your gender? 

import math
def gender_code(gender_string):
    if isinstance(gender_string, float) and math.isnan(gender_string):
        return gender_string
    return int(gender_string == 'Female')


# ### `Apply gender_code() what is your gender? column`

# In[9]:


data["gender"] = data["What is your gender?"].apply(gender_code)


# ### `Now,count male and female as 0s and 1s. How many in 'gender'column?`
# 

# In[10]:


data["gender"].value_counts(dropna=False)


# ### `Applying functions to DataFrames`
# ### `The apply method will work across each column in the DataFrame. If we pass the axis=1 keywordargument, it` `will work across each row.`
# ### `Check the data type of each column in data using a lambda function.`
# ### `Just visualize data types of first 5 columns`

# In[11]:


data.apply(lambda x: x.dtype).head()


# In[ ]:




