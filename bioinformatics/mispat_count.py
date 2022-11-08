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
	for i in range(s1-p):
		pat2=s[i:i+p]
		if(hamming(pat,pat2)<=d):
			cnt+=1
	return cnt
pat=input()
txt=input()
d=int(input())
print(pat_count(txt,pat,d))
