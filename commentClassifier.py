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


zoomitComments=pd.read_csv("C:/Users/h.safa/Downloads/Personal Files/DataScience/DataScience/Data Sets/commentTop500000.csv")
zoomitComments.describe()
zoomitComments.columns
zoomitComments.head()
zoomitComments=zoomitComments.drop(["ParentCommentid","UpdateDate2","CreateDate2","UpdatedByUserId","Name","Email"], axis=1)

#def func1st(par):
#    par.replace("<br />"," ")
#    return len(par.split(" "))

#zoomitComments['wordCount'] = zoomitComments['Message'].agg(func1st)
#zoomitComments['Message'] = zoomitComments['Message'].agg(lambda x: x.replace("<br />"," "))
#zoomitComments['Message'] = zoomitComments['Message'].agg(lambda x: x.replace("<br>"," "))
#zoomitComments['wordCount'] = zoomitComments['Message'].agg(lambda x: len(x.rsplit(" ")))


zoomitComments['Message'][499724].replace("<br />"," ")

zoomitComments['word_count'] = zoomitComments['Message'].agg(lambda x: len(x.split(" ")))


zoomitComments['Message'][2].replace("<br />"," ")

#for i in range(0,zoomitComments.shape[0],1):
#    zoomitComments['Message'][i]=zoomitComments['Message'][i].replace("<br />"," ")


