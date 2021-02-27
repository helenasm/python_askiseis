import urllib.request
import json
from datetime import date
sim=date.today()    
hm=sim.day
mhn=sim.month
e=str(mhn).zfill(2)
s=str(1).zfill(2)
q=1
k=[]
for i in range(1,hm) :
    url="https://api.opap.gr/draws/v3.0/1100/draw-date/2021-{m}-{d}/2021-{m}-{d}?page=17".format(m=e,d=s)
    s='{:02}'.format(i+1)
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict="False")
    lsts= [[] for i in range(10)]
    for draw in data["content"]:
        lsts[0].append(draw["winningNumbers"]["list"])
    result=[]
    for i in range(10):
        result = [c for c in lsts[0]]

    tel=[c for c in result[9]]
    k.append(tel)

from itertools import chain
flatten_list = list(chain.from_iterable(k))

from collections import Counter
for i in range(len(flatten_list)):
    c = Counter(flatten_list)

lst = []
kl=[]
for key,value in c.items() :
    lst.append(value)
    kl.append(key)

num = [kl for _,kl in sorted(zip(lst,kl))]
lst.sort()

for i in range(80):
    print("Ο ΑΡΙΘΜΟΣ",num[i],"ΕΜΦΑΝΙΖΕΤΑΙ ",lst[i],"ΦΟΡΕΣ")
