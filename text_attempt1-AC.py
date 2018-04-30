### This file cleans up all of the articles and separates them into separate instances of an array called post
### While cleaning up the text, this code also pulls the author_id & pubDate
### This file also reads in all of the authors, sorted by author_id and their real name

import pickle

###Reading in authors
authors = [ ' ' for x in range (0,242)]
author_id = [ ' ' for x in range(0,242)]
author_name = [ ' ' for x in range(0,242)]
post = [' ' for x in range(0,1077)]
trying = [ ' ' for x in range(0,50)]
num_articles = 0

# READ IN ARTICLES FROM WORDPRESS XML FILE

# Insert each article into one instance of the post array
# There is one extra instance of the post array - otherwise I could not get it to read
    # the last article (not sure why - can edit / try to fix later)
f = open("oncenturyavenue.wordpress.2018-03-31.xml", "r")
for i in range(0,37):
    line =f.readline()
for i in range(0,242):
    line = f.readline()
    authors[i] = line
j = -1
for i in range(0,200030):
    line = f.readline()
    line_test = line[0:7]
    if line_test == "	<item>":
        j+=1
        num_articles+=1
    post[j]+= line


f.close()

# SWITCH TO CLEANING TEXT
from bs4 import  BeautifulSoup
import re

# create array to store metadata (author_id, pubDate) in
w,h = 2,1077;
meta = [['' for x in range(w)] for y in range(h)]

#iterating through each post
for i in range(0,1076):
    source_code = post[i]
    ###pulling author id & pub date from post & insert into meta array
    soup = BeautifulSoup(source_code, "xml")
    
    meta[i][0] = soup.creator.get_text()
    meta[i][1] = soup.pubDate.get_text()
    soup = BeautifulSoup(source_code, "xml")
    j = 0
    #separating out 'encoded content' so that only access text
        # of post and not any metadata (since we already have metadata we want)
    hold = [' ' for x in range(0,2)]
    for encoded_content in soup.findAll("encoded"):
        for child in encoded_content.children:
            hold[j] = child
            j += 1
    post[i] = hold[0]
    
    #now that we have only the text of the article, take out html
        # text noted by < > 
    source_code = post[i]
    soup = BeautifulSoup(source_code, "lxml")
    start = [m.start() for m in re.finditer('<', post[i])]
    end = [m.start() for m in re.finditer('>', post[i])]
    
    hold = post[i]
    post[i] = ''
    # this was to account for the fact that some articles did not have any < >
    # this difference is attributable to different ways articles were entered in
    if start == []:
        continue;
        # it already has no < > 
    elif start[0] == 0:
        # has < > and can iterate through 
            for j in range(0,(len(start)-1)):
                post[i] += hold[end[j]:start[j+1]]
            post[i] = post[i].replace('>', ' ')
    else:
        # has < >, but don't iterate through, just use get_text, because the text is in
            # brackets
        hold = BeautifulSoup(hold, "lxml")
        post[i] = hold.get_text()

#g = open("ocatextposts.txt", "w")
#for i in range(0,len(post)):
#    g.write(str(i))
#    g.write('\n')
#    g.write(post[i])
#    g.write('\n')
#g.close()

articlesPickle = open('articlesPickle','wb')
pickle.dump(post,articlesPickle)


# WRITE THE CLEANED ARTICLES TO .TXT FILE
#g = open("ocatextposts.txt", "w")
#for i in range(0,len(post)):
#    g.write(str(i))
#    g.write('\n')
#    g.write(post[i])
#    g.write('\n')
#g.close()

# PRINT OUT THE 2= DIM META DATA ARRAY
#print(meta)
metaPickle = open('metaPickle','wb')
pickle.dump(meta,metaPickle)

### Create dictionary with key as author_id and name as value
f = open("oncenturyavenue.wordpress.2018-03-31.xml", "r")

for i in range(0,242):
    authors[i] = authors[i].split('[')
    authors[i][2] = authors[i][2].split(']')
    author_id[i] = authors[i][2][0]
    authors[i][6] = authors[i][6].split(']')
    author_name[i] = authors[i][6][0]

authors_dict = {}
for i in range(len(author_id)):
    authors_dict[author_id[i]] = author_name[i]
print(authors_dict)
f.close()

authorsPickle = open('authorsPickle','wb')
pickle.dump(authors_dict, authorsPickle)