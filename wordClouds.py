#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 15:13:26 2018

@author: stephenmathew
"""

from gensim import corpora, models
import pickle, logging
from collections import defaultdict
#import numpy


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

articlesPickleFile = open('articlesPickle','rb')
articlesArray = pickle.load(articlesPickleFile)

stoplistFile = open('stop-word-list.csv','r')
stopList = []
for line in stoplistFile.readlines():
    lineArray = line.split(sep=',')
    for word in lineArray:
        
        stopList.append(word.strip())

stoplistFile.close()    

postArrays = []
for post in articlesArray:
#    postArray = [word for word in post.lower().split() if word not in stopList]
    postArray = []
    for word in post.split():
        if (word.lower() not in stopList):
            postArray.append(word.lower())
            
        else:
#            print('stoplist' + word)
            continue
    
    postArrays.append(postArray)

dictionary = corpora.Dictionary(postArrays)

#credit to https://radimrehurek.com/gensim/tut1.html

frequency = defaultdict(int)
for text in postArrays:
   for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in postArrays]
    
#print(dictionary.token2id)

corpus = [dictionary.doc2bow(text) for text in texts]

#idToWord = corpora.dictionary.Dictionary
#print(dictionary[50])

lda = models.ldamodel.LdaModel(corpus=corpus,id2word=dictionary,num_topics=6,
                               update_every=0,passes=35)

#lda.print_topics(num_topics=5,num_words=5)

topicInfo = lda.show_topics(num_topics=6,num_words=20,formatted=True)

topicsPickle = open('topicsPickle','wb')
pickle.dump(topicInfo,topicsPickle)
