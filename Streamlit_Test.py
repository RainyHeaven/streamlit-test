#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


st.write('# Test page')
raw = pd.DataFrame([1,2,3])
raw


# In[3]:


st.bar_chart(raw)


# In[ ]:




