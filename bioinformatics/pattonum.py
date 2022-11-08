l=['A','C','G','T']
l2=[]
s1='AAAAAA'
for i in range(len(l)):
    s1=l[i]+s1[1:]
    for j in range(len(l)):
        s1=s1[:1]+l[j]+s1[2:]
        for k in range(len(l)):
            s1=s1[:2]+l[k]+s1[3:]
            for x in range(len(l)):
                s1+=s1[:3]+l[x]+s1[4:]
                for y in range(len(l)):
                    s1+=s1[:4]+l[y]+s1[5:]
                    for z in range(len(l)):
                        s1+=s1[:5]+l[z]
                        l2.append(s1)
print(l2)
