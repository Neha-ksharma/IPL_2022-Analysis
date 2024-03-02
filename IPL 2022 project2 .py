#!/usr/bin/env python
# coding: utf-8

# # IPL DATA ANALYSIS PROJECT

# In[30]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns




# In[28]:


data = pd.read_csv("IPL 2022.csv")
df=pd.read_csv('IPL 2022.csv')
df.head()


# In[6]:


pd.read_csv("IPL 2022.csv")


# # Number of matches won by each team in ipl 2022

# In[7]:


figure = px.bar(data, x = data['match_winner'], title = "Number of Matches won in IPL 2022")
figure.show()


# In[8]:


data['won_by']= data['won_by'].map ({'Wickets': 'Chasing', 'Runs':'Defending'} )
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values

colors = ['red','lightgreen']
fig = go.Figure (data=[go.Pie(labels= label , values = counts)])
fig.update_layout(title_text = "Number of matches won by defending or chasing")
fig.update_traces(hoverinfo = 'label+percent', textinfo = 'value', textfont_size = 30, marker = dict(colors =colors, line = dict(color= 'black', width = 3)))


# In[9]:


figure = px.bar(data,x = data["best_bowling"], title = "Best Bowler in IPL 2022")
figure.show()


# In[10]:


figure = px.bar(data, x =['player_of_the_match'],title = "Most Player of the match awards")
figure.show()


# # Top scrorer in IPl2022

# In[11]:


figure = px.bar(data, x = data["top_scorer"],
               y = data['highscore'],
               color = data['highscore'], title= "Top scoreres in IPL 2022")
figure.show()


# In[12]:


toss = data["toss_decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue','yellow']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision')
fig.update_traces(hoverinfo='label+percent', 
                  textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[13]:


figure = go.Figure()
figure.add_trace(go.Bar(
    x=data["venue"],
    y=data["first_ings_wkts"],
    name='First Innings Wickets',
    marker_color='gold'
))
figure.add_trace(go.Bar(
    x=data["venue"],
    y=data["second_ings_wkts"],
    name='Second Innings Wickets',
    marker_color='lightgreen'
))
figure.update_layout(barmode='group', xaxis_tickangle=-45)
figure.show()


# In[18]:


df.head(5)


# In[19]:


df.tail(-5)


# In[20]:


df.isna().sum()


# In[22]:


df.isnull().sum()


# In[34]:


df.info()


# In[ ]:




