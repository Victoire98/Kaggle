
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd 


# In[6]:


market = pd.read_csv('marketdata_sample.csv')


# In[7]:


news = pd.read_csv('news_sample.csv')


# In[8]:


news['unique_code'] = news.index


# In[9]:



def get_articles(news, market): 
    mar = market.copy()
    mar['articles'] = None
    for i in mar.index : 
        L = []
        code = mar['assetCode'][i]
        for j in news.index : 
            if code in news['assetCodes'][j]: 
                L.append(news['unique_code'][j])
        mar['articles'][i] = L 
    return mar
        


# In[10]:


new_market = get_articles(news,market)


# In[11]:


def numart(market):
    market['num_articles'] = 0
    for i in market.index: 
        market['num_articles'][i] = len(market['articles'][i])
    return market


# In[12]:


new_market = numart(new_market)


# In[25]:



def grade_articles(data, news): 
    new = news.copy()
    new = new.set_index('unique_code')
    data['sentimentClass'] = None
    data['sentimentPositive'] = None
    data['sentimentNegative'] = None
    data['sentimentNeutral'] = None
    data['sentimentWordCount'] = None
    for i in data.index :
        L,M,N,O,P = [], [], [], [], []
        for j in data['articles'][i]:
            if j in new.index : 
                L.append(new['sentimentClass'][j]) 
                M.append(new['sentimentPositive'][j]) 
                N.append(new['sentimentNegative'][j])
                O.append(new['sentimentNeutral'][j])
                P.append(new['sentimentWordCount'][j])
        data['sentimentClass'][i] = L 
        data['sentimentPositive'][i] = M
        data['sentimentNegative'][i] = N
        data['sentimentNeutral'][i] = O
        data['sentimentWordCount'][i] = P
        
        
    return data
                                                                                               
                                                                                               
                                                                                               
        


# In[26]:


new_market = grade_articles(new_market, news)


# In[51]:


def get_value(data2): 
    article_value = []
    data = data2.set_index('unique_code')
    for i in data.index : 
        article_value.append([i, data['urgency'][i], data['relevance'][i], data['firstMentionSentence'][i]])
    return article_value


# In[52]:


article_value = get_value(news)


# In[50]:


for i in news.index :
    if news['firstMentionSentence'][i] ==0:
        news['firstMention_grade'][i] = 100
    else :
        news['firstMention_grade'][i] = 1000*(max(news['firstMentionSentence'])-news['firstMentionSentence'][i])/max(news['firstMentionSentence'])

# In[50]:

news['relevance_grade'] = news['relevance']*1000
news['article_grade'] = news['relevance_grade']*0.5 + news['firstMention_grade']*0.5

# In[50]:

def note_relevance(data, liste):
    news = data.copy()
    news['note_article'] = 0
    news = news.set_index('unique_code')
    for i in news.index:
        for j in 



