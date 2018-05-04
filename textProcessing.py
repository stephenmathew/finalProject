#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:33:48 2018

@author: stephenmathew
"""
import pickle
#import numpy as np

articlesPickleFile = open('articlesPickle','rb')
weightsFile = open('EffectWordNet.txt','r')

articlesArray = pickle.load(articlesPickleFile)
articlesPickleFile.close()

numArticles = len(articlesArray)

weightsArray = []
directionArray = []
wordsArray = []


def removeUnderscore(word):
    wordSplit = word.split('_')
    outStr = ''
    for element in wordSplit:
        addition = str(element) + ' '
        outStr += addition
    return(outStr)

def getWeightDirectionWordArrays():
    for line in weightsFile:
        lineArray = line.split('\t')
        
        weight = lineArray[0]
        weightsArray.append(weight)
        
        direction = lineArray[1]
        directionArray.append(direction)
        
        try:
            wordTuple = lineArray[2].split(',')
    
        except :
            wordTuple = lineArray[2]
   
        for index in range(len(wordTuple)):
            wordTuple[index] = removeUnderscore(wordTuple[index])
       
        wordsArray.append(wordTuple)

getWeightDirectionWordArrays()
    
weightsFile.close()
#print(wordsArray[179])

