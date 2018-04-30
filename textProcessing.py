#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:33:48 2018

@author: stephenmathew
"""
import pickle
#import numpy

articlesPickleFile = open('articlesPickle','rb')
weightsFile = open('EffectWordNet.txt','r')

articlesArray = pickle.load(articlesPickleFile)
articlesPickleFile.close()

numArticles = len(articlesArray)



