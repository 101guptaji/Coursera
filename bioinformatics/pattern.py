p=input()
s=input()
f2=open('out.txt','w')
i=s.find(p)
while(i<len(s) and i>=0):
	f2.write(str(i))
	i=s.find(p,i+1,len(s))

print('helo')
f2.close()
