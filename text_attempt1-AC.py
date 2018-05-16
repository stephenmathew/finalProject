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
w,h = 3,1077;
meta = [['' for x in range(w)] for y in range(h)]

#iterating through each post
for i in range(0,1076):
    source_code = post[i]
    ###pulling author id & pub date from post & insert into meta array
    soup = BeautifulSoup(source_code, "xml")
    
    meta[i][0] = soup.creator.get_text()
    meta[i][1] = soup.pubDate.get_text()
    temp = meta[i][1]
    meta[i][1] = temp[8:11]
    meta[i][2] = temp[12:16]
    print(meta[i])
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
print(metaPickle)
f.close()
authors_dict = {"kvb226": "Kiril Bolotnikov, male, 2017", "nyl232": "Naomi Losman, female, 2017", "Tyler Rhorick": "Tyler Rhorick, male, 2017", "kw1446": "Kathy Wang, female, 2017", "lh1677": "Richard Lewei Huang, male, 2017", "mn1553": "Meizhi Ng, female, 2017", "cls534": "Cynthia Sun, female, 2017", "man421": "Mercy Angela Nantongo, female, 2017", "yg919": "Nancy Gong, female, 2017", "hmj239": "Hunter Jarvis, female, 2017", "zc562": "Roman Chen, male, 2017", "cas770": "Chava A. Schapira, female, 2017", "akt317": "Sarabi Eventide, female, 2017", "mll469": "Michael Lukiman, male, 2017", "bgc236": "Benjamin Goh, male, 2017", "gby203": "Gloria Yu, female, 2017", "wjl297": "Wes Livingstone, male, 2018", "tb1415": "Tatiana Bautista, female, 2017", "vlh245": "Veronica Hernandez, female, 2017", "emm590": "Enrique Menendez, male, 2017", "est289@nyu.edu": "Emma Tao, female, 2018", "shs394": "Slater Stanley, male, 2017", "cvs264@nyu.edu": "Cato van Schaik, female, 2017", "af2383": "Alhan Fakhr, male, 2017", "mam1362": "Michael Margaritoff, male, 2017", "bac407": "Baaria Chaudhary, female, 2017", "nls336": "Natalie Soloperto, female, 2017", "nas476": "Nicholas Sanchez, male, 2017", "eac536": "Elizabeth Cathcar, female, 2017t", "tz583": "Amy Zhao, female, 2017", "dcm392": "Dana Meyers, female, 2017", "eff239": "Emily Flippen, female, 2017", "emw401": "Betsie Wilson, female, 2017", "che210": "Charlotte Evans, female, faculty", "fk592": "Fikret Halilov, male, 2017", "ren248": "Royale Efae Nicholson, female, 2017", "yw1242": "Villa Wu, female, 2017", "sd1757": "Sammy Dalati, male, 2017", "rr2449": "Roxanne Roman, female, 2017", "ks3286": "Kenny Song, male, 2017", "clb478": "Cameron Ballard, male, 2017", "fr679": "Ferwa Razzaq, female, 2017", "acp458": "Abiral Chitrakar Phnuyal, male, 2017", "pmb362": "Max Bork, male, 2017", "rm3492": "Rima Mehta, female, 2017", "rd1544": "Rae Dehal, female, 2017", "OCAadmin": "Editorial Staff, oca, oca", "sexyshanghaier": "Sexy Shanghaier, oca, 2017" , "hkb257": "Kadallah Burrowes, male, 2017", "mac1053": "Mike Chen, male, 2017", "contributor": "Contributor, oca, oca", "myo207": "Mohammed Omar, male, 2017", "zh415": "Zoe Hu, female, 2017", "mew460": "Maya Williams, female, 2018", "jws443": "James Smoley, male, 2017", "ns2972": "Natsuko Saegusa, male, 2017", "lp1449": "Lu Pang, male, 2017", "shb351": "Stephanie Bailey, female, 2018", "lcm380": "Lathika Chandra Mouli, female, 2017", "zbj202": "Zoe Jordan, female, 2018", "mm7134": "Máté Mohos, male, 2018", "sc4366": "Steven Chien, male, 2017", "ayk270": "Alina Kalintceva, female 2017", "jh3693": "Jessica Herrera, female 2018", "oj294": "Olivia Jones, female, 2017", "tka220": "Tessa Ayson, female, 2019", "if492": "Isabella Farr, female, 2018", "am5431": "Alexander Mayes, male, 2017", "afc340": "Allison Chesky, female, 2018", "meg592": "Megan Graham, female, 2017", "kd1310": "Kinsa Durst, male, 2017", "if459": "Ilham Farah, female, 2017", "hbc236": "Hongbin Chen, male, 2017", "pj665": "Paddy Jow, male, 2018", "lhk250": "Lillian Korinek, female, 2018", "ab2514": "Amy Becker, female, faculty", "cap571": "Carmen Paulus, female, 2018", "ajs1030": "Annie Seaman, female, 2018", "mmw413": "Maggie Walsh, female, 2018", "ocf207": "Oscar Fossum, male, 2018", "Gabriella Butler": "Gabriella Butler, female, 2017", "Louis Plottel": "Louis Plottel, male, 2017", "ifb214": "Isabella Baranyk, female, 2018", "snk303": "Sandra Kohn, female, 2017", "sw2827": "Sunyi Wang, female, 2018", "jcs674": "Jose Antonio Cabrera Sanchez, male, 2017", "wz746": "Ben Weilun Zhang, male, 2018", "alp236": "Anna Perez, female, 2017", "pc123": "Puja Chandramohan, female, 2018", "eel276": "Lizzy Leclaire, female, 2018", "jl4910": "Jennifer Lu, female, 2019", "jhauge": "Julie Hague, female, 2017", "ak3927": "Adan Kohnhurst, male, 2017", "krn249": "Katie-Rose Nunziato, female, 2018", "gfr217": "Gabriel Ruiz, male, 2019", "Haider Ali": "Haider Ali, male, 2018", "OpenGoodbye": "Open Goodbye, oca, oca", "spaus": "Shawn Paustian, male, 2017", "ah3165": "Abel Hegyes, male, 2018", "zeliu": "Ze Liu, male, 2018", "yl2769": "Nell Lang, female, 2018", "mtl364": "Maeve Lazor, female, 2019", "ljd325": "Louis Demetroulakos, male, 2019", "jsc673": "Joanne Chun, female, 2019", "mchen": "Mengzhu Chen, female, 2018", "mhuangoca": "Michelle Huang, female, 2018", "lk1654": "Lana Kugli, female, 2018", "mw2885": "Wu Mei, female, 2019", "nh1225": "Nofar Hamrany, female, 2018", "acc593": "Ana Cicenia, female, 2018", "esk378": "Ella Kuzmenko, female, 2018", "ac5188": "Anita Bonomi, female, 2018", "yl3358": "Yuqing Li, male, 2019", "lt1268": "Leidy Tapasco, female, 2018", "jhhuang": "Johnson Hantao Huang, male, 2018", "kqp200@nyu.edu": "Kevin Pham, male, 2017", "sab863": "Savannah Billman, female, 2019", "scu215": "Serena Uy, female, 2019", "jrt386": "Jeremy Teboul, male, 2019", "jhr347": "John Rhoades, male, 2019", "qpm201": "Quinn Mchale, male, 2018", "su399": "Stephanie Ulan, female, 2017", "zf422": "Zeerak Fayiz, male, 2018", "aak473": "Alexander Kario, male, 2018", "nk1469": "Noel Konagai, male, 2017", "amc1108": "Anthony Comeau, male, 2019", "Isabella Farr and Chloe Haddaway": "Isabella Farr and Chloe Haddaway, female, 2018", "sc4849": "Shiyun Chen, male, 2018", "tbt232": "Tara Tate, female, 2018", "dhp272": "Diem Hang Pham, female, 2018", "ag4037": "Alina Gabdrakhmanova, female, 2017", "zw760": "Zihe Wang, male, 2017", "jz2159": "Jiayu Zhu, female, 2019", "ym1142": "Gareth (Yiming) Ma, male, 2018", "amj464": "Diem Hang Pham & Anna Maria Jaskiewicz, female, 2018", "oc496": "Omer Cohen, male, 2018", "aas916": "Andreas Strandgaard, male, 2019", "maw597": "Mark West, male, 2017", "mt2426": "Nady Thiam, female, 2018", "afr456778": "Anna Jaskiewicz, female, 2018", "ql470": "Qing Sponge Luo, male, 2018", "di435": "Defne Inhan, female, 2018", "mg4574": "Milica Gligic, female, 2018", "hs2623": "Haley Sadoff, female, 2018", "yy2085": "Yanming Zhang, male, 2019", "sk3319": "Kangjie Liu, female, 2019", "sa3303": "Sonia Alvarez, female, 2018", "jjg509": "Joelle Jay, female, 2019", "xy650": "Shari Yao, female, 2018", "mpf293": "Madeline Farquharson, female, 2019", "san331": "Sophia Noel female, 2017", "jl6637": "Junchao Lin, male, 2018", "zz1224": "Zhiwei Zhu, female, 2019", "wh915": "Jackie Wenqian Hu, female, 2018", "bch290": "Benjamin Haller, male, 2019", "sh3291": "Kelvin Hu, male, 2017", "dmf449": "Dillon Fournier, male, 2019", "ss8175": "Shreya Shreerman, female, 2019", "jz1483": "Sarah Jinrong Zhang, female, 2019", "alm709": "AnneLi Meisel, female, 2018", "ldc308": "Laura de Crescenzo, female, 2019", "ellas": "Ella S, female, 2018", "ywl242": "Sophie Li, female, 2018", "sms": "Usama Shahid, male, 2017", "so1168": "Sabina Olsson, female, 2020", "my1365": "Mira Yoo, female, 2019", "czcecily": "Zhiyu Cecily Chen, female, 2020", "qf263": "Andy Fang, male, 2020", "danielhuang1107": "Daniel Huang, male, 2020", "Sarah Tahir": "Sarah Tahir, female, 2020", "Millie Wong": "Millie Wong, female, 2019", "sx484": "Jesse Xu, male, 2019", "oda218": "Oriana Carisa De Angelis, female, 2019", "ytl304": "Yutong Lin, male, 2020", "bzc210": "Bishka Zareen Chand, female, 2020", "blt277": "Benjamin Tablada, male, 2020", "yl4043": "Rita Liu, female, 2020", "iba220": "Isabel Adler, female, 2020", "im850": "Ivan Marks, male, 2017", "hs2959": "Sylvia Sang, female, 2020", "mw2581": "Marjorie Wang, female, 2017", "am7766": "Anisa Muca, female, 2020", "xb285": "Xue Bin, male, 2020", "jq486": "Lyndsy Qu, female, 2019", "jhs619": "Ji Hwan Shin, male, 2020", "as7483": "Anna Schmidt, female, 2017", "zz732": "Richard Zhao, male, 2017", "ll3031": "Ray Lin, male, 2020", "es3934": "Emira Sabanovic, female, 2019", "oas243": "Cato and Osman, female, 2017", "cik229": "Catt Kim, female, 2019", "pm1815": "Pramugdha Maheswari, female, 2017", "kk3144": "Konrad Krawczyk, male, 2019", "ssg358": "Sabrina Greene, female, 2019", "abd370": "Arshaun Darabnia, male, 2019", "tjk343": "Thomas Justin Klein, male, 2018", "ys2731": "Eric Song, male, 2020", "zl1298": "Zijie Lu, male, 2019", "mw3235": "Stephanie and Millie, female, 2019", "rz1071": "Ruwen Zhou, male, 2020", "mp4080": "Momachi Pabrai, female, 2020", "mnp305": "Maike Prewett, female, 2019", "jw4098": "Jingyi Wang, female, 2017", "hal307": "Honey Asrat Lera, female, 2019", "jlg662": "Jeanne Le Galcher Baron, female, 2019", "rp2550": "Raitis Pekuss, male, 2020", "vt695": "Virgil Tataru, male, 2019", "jz1504": "Amanda Zhao, female, 2017", "jw3229": "Jacko Walz, male, 2017", "al4490": "Andre' Lucas, male, 2019", "na1881": "Nacole Abram, female, 2020", "aj1397": "Alicja Jader, female, 2017", "cheryl.li": "Cheryl Li, female, 2018", "ss7523": "Shayla Schlossenberg, female, 2017", "jnp297": "Jazz Pitts, female, 2020", "bd1071": "Bo Donners, female, 2018", "scg401": "Sara Gradinarska, female, 2020", "kay238": "Krista Young, female, 2017", "jmk746": "Jarred Kubas, male, 2017", "sy2221": "Simone Ye, female, 2021", "tlu208": "Tyson Lee Upshaw, male, 2021", "arh522": "Alessandra Hallman, female, 2021", "jz2477": "Kai Zheng, female, 2021", "xc1121": "Silvia Chen, female, 2021", "aga323": "Adriano Albarosa, male, 2018", "bej235": "Brooke Jensen, female, 2019", "kap633": "Kate Pellegrino, female, 2021", "amm1429": "Alexandra Mathew, female, 2020", "zl1588": "Flora Ziyun Lu, female, 2020", "ang405": "Austin Gregory, male, 2020", "agp357": "Andres Gomez-Perry, male, 2019", "tn836": "Tehreem Nihar, female, 2018", "bc2429": "Billy Chan, male, 2020", "ojb224": "Olivia Bensimon, female, 2020", "lhr246": "Luc Riesbeck", "sybz2285": "Simone Ye and Ben Weilun Zhang", "hsm310": "Hafeeza Mughal", "srr408": "Syed Raiyan Nuri Reza", "az1579": "Angela Zheng, female, 2021", "jdr500": "Sevi Reyes, male, 2018", "er2484": "Emma Rosensaft, female, 2021", "mdc549": "Matthew Cline, male, 2020"}

authorsPickle = open('authorsPickle','wb')
pickle.dump(authors_dict, authorsPickle)