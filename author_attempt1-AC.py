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

f.close()
print(post[1075])
print(num_articles)

testing = post[0]
print(testing)
testing = testing.split("<dc:creator")
testing[1] = testing[1].split("</dc:creator")
print(testing[1][0])
print(testing[1][1])
"""
print(post)
"""
"""
### Create dictionary with key as author_id and name as value
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