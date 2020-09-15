#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:01:30 2020

@author: Hossein
"""

!git add "commentClassifier.py"
!git commit -m "from-Mac-Spyder"
!git push

import numpy as np
import pandas as pd
import hazm as hm
import re as reg

path="C:/Users/h.safa/Downloads/Personal Files/DataScience/DataScience/Data Sets/"
comment_csv=["commentTop500000.csv","commentTop500000Page2.csv","commentTop500000Page3.csv"]

list_of_dataframes = []
for filename in comment_csv:
    list_of_dataframes.append(pd.read_csv(path+filename))

zoomitComments = pd.concat(list_of_dataframes)
zoomitComments['Status'].unique()
zoomitComments['Status'].value_counts()
len(zoomitComments)
zoomitComments.describe()
zoomitComments=pd.read_csv("C:/Users/h.safa/Downloads/Personal Files/DataScience/DataScience/Data Sets/commentTop500000.csv")
#zoomitComments=pd.read_csv("/Users/Hossein/Desktop/DataScience/Data Sets/commentTop500000.csv")

zoomitComments.dtypes
zoomitComments.describe()
zoomitComments.columns
zoomitComments.head()
zoomitComments=zoomitComments.drop(["ParentCommentid","UpdateDate2","CreateDate2","UpdatedByUserId","Name","Email"], axis=1)

zoomitComments['Message']=zoomitComments['Message'].astype(str)
zoomitComments['Message'] = zoomitComments['Message'].agg(lambda x: reg.sub('[<br />]',' ',x))
zoomitComments['wordCount'] = zoomitComments["Message"].agg(lambda x: len(x.split(" ")))
zoomitComments['charCount'] = zoomitComments["Message"].agg(lambda x: len(x))
zoomitComments['Message'] = zoomitComments['Message'].agg(lambda x: reg.sub('\s+',' ',x))

#zoomitComments['Message']=zoomitComments['Message'].agg(lambda x: (' ').join(reg.sub('.','',[w for w in x.split() if reg.match('([\w]+\.)+[\w]+(?=[\s]|$)',w)]))

stopWords=hm.stopwords_list()
zoomitComments['#_of_StopWords']=zoomitComments['Message'].agg(lambda x: len([w for w in x.split() if w in stopWords]))

stemWords=hm.Stemmer()
zoomitComments['Message']=zoomitComments['Message'].agg(lambda x: (' ').join([stemWords.stem(w) for w in x.split()]))

pubComment=zoomitComments.loc[zoomitComments['Status']==1,:].loc[:,['Message']]
unpubComment=zoomitComments.loc[zoomitComments['Status']==0,:].loc[:,['Message']]

pub_No_Stop=zoomitComments['Message'].agg(lambda x: (' ').join([w for w in x.split() if w not in stopWords]))
unpub_No_stop=zoomitComments['Message'].agg(lambda x: (' ').join([w for w in x.split() if w not in stopWords]))

pub_comment_count=pub_No_Stop.split(expand=True).stack().value_counts()

zoomitComments['Status'].unique()
len(pubComment)
len(unpubComment)


stopWords
len(stopWords)

