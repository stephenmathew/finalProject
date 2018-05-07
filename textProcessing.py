#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:33:48 2018

@author: stephenmathew
"""
import pickle


articlesPickleFile = open('articlesPickle','rb')
weightsFile = open('EffectWordNet.txt','r')

articlesArray = pickle.load(articlesPickleFile)
articlesPickleFile.close()

numArticles = len(articlesArray)

weightsArray = []
directionArray = []
wordsArray = []
wordsDict = {}


def removeUnderscore(word):
    wordSplit = word.split('_')
    outStr = ''
    for element in wordSplit:
        addition = str(element) + ' '
        outStr += addition
    return(outStr)

def getWeightDirectionWordArrays():
    termsInDict = 0
    for line in weightsFile:
        lineArray = line.split('\t')
        
        weight = lineArray[0]
        weightsArray.append(int(weight))
        
        direction = lineArray[1]
        directionArray.append(direction)
        
        try:
            wordTuple = lineArray[2].split(',')
    
        except :
            wordTuple = lineArray[2]
   
        for index in range(len(wordTuple)):
            wordTuple[index] = removeUnderscore(wordTuple[index])
            currentWord = wordTuple[index]
            currentWord.rstrip()
            wordsDict[currentWord] = termsInDict
       
        wordsArray.append(wordTuple)
        termsInDict+=1

getWeightDirectionWordArrays()
    
weightsFile.close()
print(wordsArray[179])
<<<<<<< Updated upstream


def readZePosts():
    postScores = []

    for post in articlesArray:

        postScore = 0
        postWords = post.split(' ')
        for searchWord in postWords:

            if (searchWord == ' '):
                continue
            search = searchWord + ' '
            wordScore = 0
            try:
                wordIndex = wordsDict[search]
                if (directionArray[wordIndex] =='+Effect'):
                    wordScore += 1
                elif(directionArray[wordIndex] =='-Effect'):
                    wordScore -= 1
                weight = (weightsArray[wordIndex])
                wordScore = wordScore * weight
            except :
                continue
            postScore += wordScore
        postScores.append(postScore)
    return(postScores)
    
postScoresArray = readZePosts()

    
    
    
        
    
    
=======
>>>>>>> Stashed changes

