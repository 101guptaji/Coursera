def hamming(a1,a2):
	count=0
	if(len(a1)==len(a2)):
		for i in range(len(a1)):
			if(a1[i]!=a2[i]):
				count+=1
	return count
def pat_count(s,pat,d):
	cnt=0
	s1=len(s)
	p=len(pat)
	for i in range(s1-p+1):
		pat2=s[i:i+p]
		if(hamming(pat,pat2)<=d):
			print(i,end=' ')
			cnt+=1
	return cnt
fname=open('mispat.txt','r')
pat=fname.readline().strip()
txt=fname.readline().strip()
d=int(fname.readline())
#print(pat,txt,d)
print('\npattern count ',pat_count(txt,pat,d))
