
def p_count(s, pat,a,L):
	count = 0
	k=len(pat)
	for i in range(a,L-k):
		if(s[i:i+k]==pat):
			count+=1
	return count

file=open('clumps.txt','r')
s=file.readline()
k,L,t = file.readline().split()
k,L,t=int(k),int(L),int(t)

freq=[]
#d={}
c=[]
a=0
while(L<=len(s)):
	d={}
	for j in range(a,L-k+1):
		pat=s[j:j+k]
		#cnt=p_count(s,pat,a,L)
		d[pat]=d.get(pat,0)+1
		#if(cnt>=t):
		#	d[pat]=cnt
	for key in d.keys():
		if(d[key]>=t):
			c.append(key)
	a+=1
	L+=1
#print('c ',c)
dist=set(c)
#print('dist ',dist)
for i in dist:
	print(i,end=' ')
