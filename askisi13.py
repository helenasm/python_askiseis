import string
import re
file=open('two_cities_ascii.txt','r')
all=file.read()

sentence = " ".join(re.split("\s+", all, flags=re.UNICODE))
xx=sentence.translate(str.maketrans('', '', string.punctuation))
result1 = ''.join([i for i in xx if not i.isdigit()])
tel=result1.lower()    

lst=list(tel.split(" "))

length=len(lst)

lsts= [[] for i in range(21)]
num= [[] for i in range(21)]

for j in range(21):
    for i in range(length):
        if len(lst[i])==j:
            lsts[j].append(lst[i])
    #print(lsts[j])
    num[j]=(len(lsts[j]))

for k in range(11):
    while (num[k]>0 and num[20-k]>0 ):
        print(lsts[k].pop(0),lsts[20-k].pop(0))
        num[k]=num[k]-1
        num[20-k]=num[20-k]-1

file.close()
