s=input("enter text")
pa=input("enter pattern")
pb=input("enter pattern2")
t=list(s)
p1=list(pa)
p2=list(pb)
pl=len(pa)
pl2=len(pb)
tl=len(t)
def kmpsearch(t,p1):
	#lps construction
	lps=[]
	for i in range(pl):
		lps.append(0)
	j=0
	i=1
	while(i<pl):
		if(p1[i]==p1[j]):
			j+=1
			lps[i]=j
			i+=1
		else:
			if(j!=0):
				j=lps[j-1]
				#j-=1
			else:
				lps[i]=0
				i+=1
	print("lps=",lps)

	#kmp string matching
	j=0
	i=0
	while(i<tl):
		if(p1[j]==t[i]):
			i+=1
			j+=1
		if(j==pl):
			print("pattern found at index " + str(i-j))
			j=lps[j-1]
		elif(i<tl and p1[j]!=t[i]):
			if(j!=0):				
				j=lps[j-1]
			else:
				i+=1
kmpsearch(t,p1)
kmpsearch(t,p2)
