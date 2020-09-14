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

#zoomitComments=pd.read_csv("C:/Users/h.safa/Downloads/Personal Files/DataScience/DataScience/Data Sets/commentTop500000.csv")
zoomitComments=pd.read_csv("/Users/Hossein/Desktop/DataScience/Data Sets/commentTop500000.csv")

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

stopWords=hm.stopwords_list()
zoomitComments['#_of_StopWords']=zoomitComments['Message'].agg(lambda x: len([w for w in x.split() if w in stopWords]))

stemWords=hm.Stemmer()
zoomitComments['Message']=zoomitComments['Message'].agg(lambda x: (' ').join([stemWords.stem(w) for w in x.split()]))

zoomitComments['Message'][2]


 reg.findall(' ++','hossein   safa')


