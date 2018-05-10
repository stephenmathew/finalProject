# -*- coding: utf-8 -*-
import pickle 

sentimentPickleFile = open('sentimentPickle','rb')

sentimentArray = pickle.load(sentimentPickleFile)
sentimentPickleFile.close()

metaPickleFile = open('metaPickle','rb')

metaArray = pickle.load(metaPickleFile)
metaPickleFile.close()


metaArray = metaArray[:-1]
print(sentimentArray)

def selectionSort(l):
    for value1 in range(len(l)):
        for value2 in range(value1+1, len(l)):
            if l[value2]<l[value1]:
                l[value1],l[value2]=l[value2], l[value1]

sentimentSort = list(map(int, sentimentArray))

selectionSort(sentimentSort)
print(sentimentSort)

