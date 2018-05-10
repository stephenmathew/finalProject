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
postWordList = []
articlesArray = articlesArray[:-1]

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



def readZePosts():
    postScores = []

    for post in articlesArray:
        postWordList = []
        postScore = 0
        postWords = post.split(' ')
        count = 0
        for searchWord in postWords:
            count+=1
            if (searchWord == ' '):
                continue
            search = searchWord + ' '
            wordScore = 0
            wordScoreTemp = 0
            try:
                wordIndex = wordsDict[search]
                postWordList.append(search)
                if (directionArray[wordIndex] =='+Effect'):
                    wordScoreTemp += 1
                elif(directionArray[wordIndex] =='-Effect'):
                    wordScoreTemp -= 1
                #negation detection
                for neg in range(count-5, count):
                    if postWords[neg]=='not':
                        wordScore = wordScore*-1
                    elif postWords[neg]=='never':
                        wordScore = wordScore*-1
                #intensifer
                for intense in range(count-5, count):
                    if postWords[intense]=='very':
                        if wordScoreTemp == -1:
                            wordScoreTemp -=1
                        else:
                            wordScore +=1
                    elif postWords[intense]=='extremely':
                        if wordScoreTemp == -1:
                            wordScoreTemp -=1
                        else:
                            wordScore +=1
                    elif postWords[intense]=='incredibly':
                        if wordScoreTemp == -1:
                            wordScoreTemp -=1
                        else:
                            wordScore +=1
                    elif postWords[intense]=='particularly':
                        if wordScoreTemp == -1:
                            wordScoreTemp -=1
                        else:
                            wordScoreTemp +=1
                #diminisher
                for diminish in range(count-5,count):
                    if postWords[diminish]=='little':
                        if wordScoreTemp == -1:
                            wordScoreTemp +=0.5
                        else:
                            wordScoreTemp -=0.5
                    elif postWords[diminish]=='barely':
                        if wordScoreTemp == -1:
                            wordScoreTemp +=0.5
                        else:
                            wordScoreTemp -=0.5
                    elif postWords[diminish]=='hardly':
                        if wordScoreTemp == -1:
                            wordScoreTemp +=0.5
                        else:
                            wordScoreTemp -=0.5
                    elif postWords[diminish]=='rarely':
                        if wordScoreTemp == -1:
                            wordScoreTemp +=0.5
                        else:
                            wordScoreTemp -=0.5
                weight = (weightsArray[wordIndex])
                wordScore = wordScoreTemp
                wordScore = wordScore * weight
            except :
                continue
            postScore += wordScore
        postScores.append(postScore)
        
    return(postScores)
    
    
    
postScoresArray = readZePosts()

sentimentPickle = open('sentimentPickle','wb')
pickle.dump(postScoresArray, sentimentPickle)
    
        
    
    
