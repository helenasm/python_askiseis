from random import shuffle
import numpy as np
print ("ΔΩΣΕ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ")
dias=input()
num=int(dias)
while num<4:
    print("ΔΩΣΕ ΞΑΝΑ ΣΩΣΤΟ ΑΡΙΘΜΟ ΜΕΓΑΛΥΤΕΡΟ ΤΟΥ 4 ΔΗΛΑΔΗ ")
    dias=input()
    num=int(dias)
uesi=num*num
s=0
for k in range(100):
    d1=[]
    for i in range(uesi):
        d1.append(0)

    if uesi %2==0:   
        tel=int(uesi/2)
    else:
        tel=int(uesi/2)+1

    for i in range(tel):
        d1[i]=1
    shuffle(d1)

    a = np.array(d1).reshape(num,num)
    print(a)

    pl=0
    athr=0

    for i in range(0,num):
        for j in range(0,num-3):
            if a[i][j]==a[i][j+1]==a[i][j+2]==a[i][j+3]==1:
                pl=pl+1

    for i in range(0,num-3):
        for j in range(0,num):
            if a[i][j]==a[i+1][j]==a[i+2][j]==a[i+3][j]==1:
                pl=pl+1

    for i in range(0,num-3):
        for j in range(0,num-3):
            if i==j:
                if a[i][j]==a[i+1][j+1]==a[i+2][j+2]==a[i+3][j+3]==1:
                    pl=pl+1

    if num==4:
        if a[3][0]==a[2][1]==a[1][2]==a[0][3]==1:
            pl=pl+1
    else:
        for i in range(num-1, num-3, -1):
                for j in range(num//2):
                        if (a[i][j] == a[i - 1][j + 1] == a[i - 2][j + 2] == a[i - 3][j + 3]):
                            pl=pl+1

    athr=athr+pl
    s=s+athr
mo=s/100
print("Ο ΜΕΣΟΣ ΟΡΟΣ ΤΩΝ ΤΕΤΡΑΔΩΝ ΕΙΝΑΙ",mo)
