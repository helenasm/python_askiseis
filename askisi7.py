import urllib.request
import json
from datetime import date
sim=date.today()     
hm=sim.day
mhn=sim.month
q=1
n=1
e=str(mhn).zfill(2)
s=str(0).zfill(2)
for i in range(hm-1) :
    s='{:02}'.format(i+1)
    k=[]
    for j in range(18):
        url="https://api.opap.gr/draws/v3.0/1100/draw-date/2021-{m}-{d}/2021-{m}-{d}?page={p}".format(m=e,d=s,p=j)
        r=urllib.request.urlopen(url)
        html=r.read()
        html=html.decode()
        data=json.loads(html,strict="False")
        lsts= [[] for i in range(10)]
        for draw in data["content"]:
            lsts[0].append(draw["winningNumbers"]["list"])

        for i in range(10):
            result = [c for c in lsts[0]]


        for i in range(10):
            tel=[c for c in result[i]]
            k.append(tel)

        from itertools import chain
        flatten_list = list(chain.from_iterable(k))
            #print(flatten_list)

        from collections import Counter
        for i in range(len(flatten_list)):
            c = Counter(flatten_list)

        lst = []
        kl=[]
        for key,value in c.items() :
            lst.append(value)
            kl.append(key)


    meg=max(lst)
    k=[]
    s1=[]
    for i in range(len(lst)):
        if lst[i]==meg:
            k.append(kl[i])
            if len(k)==1:
                print("Ο ΑΡΙΘΜΟΣ ΠΟΥ ΕΜΦΑΝΙΖΕΤΑΙ ΣΥΧΝΟΤΕΡΑ ΤΗΝ",q,"ΗΜΕΡΑ ΕΙΝΑΙ Ο " ,k)
            else:
                print("ΟΙ ΑΡΙΘΜΟΙ ΠΟΥ ΕΜΦΑΝΙΖΟΝΤΑΙ ΣΥΧΝΟΤΕΡΑ ΤΗΝ",q,"ΗΜΕΡΑ ΕΙΝΑΙ ΟΙ " ,k)
    q+=1
