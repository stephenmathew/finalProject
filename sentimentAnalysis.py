# -*- coding: utf-8 -*-
import pickle 

sentimentPickleFile = open('sentimentPickle','rb')

sentimentArray = pickle.load(sentimentPickleFile)
sentimentPickleFile.close()

metaPickleFile = open('metaPickle','rb')

metaArray = pickle.load(metaPickleFile)
metaPickleFile.close()

articlesPickleFile = open('articlesPickle','rb')

articlesArray = pickle.load(articlesPickleFile)
articlesPickleFile.close()


metaArray = metaArray[:-1]
#print(sentimentArray)

def selectionSort(l):
    for value1 in range(len(l)):
        for value2 in range(value1+1, len(l)):
            if l[value2]<l[value1]:
                l[value1],l[value2]=l[value2], l[value1]

sentimentArray = list(map(float, sentimentArray))

sentimentSort = sentimentArray
selectionSort(sentimentSort)

w,h = 3,1076;
analysisArray = [[' ' for x in range(w)] for y in range(h)]



#for senti in range(len(sentimentSort)):
#    search = sentimentSort[senti]
#    postIndex = sentimentArray.index(search)
#    analysisArray[senti] = metaArray[postIndex]
#print(analysisArray)