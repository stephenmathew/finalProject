### Reading in data from OCA text file

###Reading in authors
authors = [ ' ' for x in range (0,242)]
author_id = [ ' ' for x in range(0,242)]
author_name = [ ' ' for x in range(0,242)]
post = [' ' for x in range(0,1076)]
trying = [ ' ' for x in range(0,50)]
num_articles = 0

f = open("/Users/achesky/Downloads/oncenturyavenue.wordpress.2018-03-31.xml", "r")
for i in range(0,37):
    line =f.readline()
for i in range(0,242):
    line = f.readline()
    authors[i] = line
g = open("/Users/achesky/Desktop/ocatextposts.xml", "w")
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

f.close()

from bs4 import  BeautifulSoup
import re
"""
print(post[3])
print('practice')
source_code = post[3]
soup = BeautifulSoup(source_code, "lxml")

tag = soup.title
tag.clear()
tag = soup.link
tag.clear()
hold = soup.get_text()
print('test')
print(hold)
"""


for i in range(0,len(post)):
    print(i)
    print(post[i])
    source_code = post[i]
    soup = BeautifulSoup(source_code, "lxml")
    hold = soup.find_all('p')
    print('test')
    if hold == []:
        source_code = post[i]
        soup = BeautifulSoup(source_code, "lxml")
        """
        tag = soup.title
        tag.clear()
        tag = soup.link
        tag.clear()
        """
        hold = soup.get_text()
        post[i] = hold
        print(post[i])
    else: 
        post[i] = ''
        for j in hold:
            post[i] += str(j) + ' '
        
        start = [m.start() for m in re.finditer('<', post[i])]
        end = [m.start() for m in re.finditer('>', post[i])]
        
        hold = post[i]
        post[i] = ''
        if start[0] == 0:
            for j in range(0,(len(start)-1)):
                post[0] += hold[end[j]:start[j+1]]
            post[0] = post[0].replace('>', ' ')
        else:
            print('yikes')
        print(post[i])










"""
print(post)


### Create dictionary with key as author_id and name as value
f = open("/Users/achesky/Downloads/oncenturyavenue.wordpress.2018-03-31.xml", "r")
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

"""
"""
for i in range(0,37440):
while True:
    line = f.readline()
    if len(line)==0:
        break
    line = line[:-1]
    line = line.split(',')
    x_input[i] = line
    x_input[i] = [float(x) for x in x_input[i] ]
    i += 1
f.close()
"""