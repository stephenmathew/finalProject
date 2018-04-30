### Reading in data from OCA text file

import pickle

###Reading in authors
authors = [ ' ' for x in range (0,242)]
author_id = [ ' ' for x in range(0,242)]
author_name = [ ' ' for x in range(0,242)]
post = [' ' for x in range(0,1079)]
trying = [ ' ' for x in range(0,50)]
num_articles = 0


f = open("oncenturyavenue.wordpress.2018-03-31.xml", "r")
for i in range(0,37):
    line =f.readline()
for i in range(0,242):
    line = f.readline()
    authors[i] = line
save = ''
j = -1
for i in range(0,200030):
    line = f.readline()
    line_test = line[0:7]
    if line_test == "	<item>":
        j+=1
        num_articles+=1
    post[j]+= line
    #splitting file into posts

post[1076] = "let's see"
post[1077] = "let's see"
post[1078] = "let's see"
f.close()

from bs4 import  BeautifulSoup
import re



print(post[-1])
for i in range(0,len(post)):
    source_code = post[i]
    soup = BeautifulSoup(source_code, "xml")
    j = 0
    hold = [' ' for x in range(0,2)]
    for encoded_content in soup.findAll("encoded"):
        for child in encoded_content.children:
            hold[j] = child
            print(child)
            j += 1
    post[i] = hold[0]

    source_code = post[i]
    soup = BeautifulSoup(source_code, "lxml")
    start = [m.start() for m in re.finditer('<', post[i])]
    end = [m.start() for m in re.finditer('>', post[i])]
    
    hold = post[i]
    post[i] = ''
    print(hold)
    print(start)
    if start == []:
        continue;
    elif start[0] == 0:
            for j in range(0,(len(start)-1)):
                post[i] += hold[end[j]:start[j+1]]
            post[i] = post[i].replace('>', ' ')
    else:
        print('yikes')
        hold = BeautifulSoup(hold, "lxml")
        post[i] = hold.get_text()
print(post[-1])
#g = open("ocatextposts.txt", "w")
#for i in range(0,len(post)):
#    g.write(str(i))
#    g.write('\n')
#    g.write(post[i])
#    g.write('\n')
#g.close()

articlesPickle = open('articlesPickle','wb')
pickle.dump(post,articlesPickle)

### Create dictionary with key as author_id and name as value
f = open("oncenturyavenue.wordpress.2018-03-31.xml", "r")
for i in range(0,113):
    line = f.readline()
    line = line[0:7]
    if line == "	<item>":
        print("Nice!")
        line_test = f.readline()
        
        if line_test == "		<dc:c":
            print("author!")
            trying[0] = line_test
            if line_test == "		<cont":
                print("content!")
                trying[1] = line_test
                while True:
                    line_testing = f.readline()
                    if line_testing == "		<exce":
                        break
                    trying[1] += line_testing
    if line == "	</item":
        print("Even better!")


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
