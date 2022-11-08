
def p_count(s, pat):
	count = 0
	k=len(pat)
	for i in range(len(s)-k+1):
		if(s[i:i+k]==pat):
			count+=1
	return count


s=input("enter text")
#pat=input("enter")
#print(p_count(s,pat))
k=int(input("enter k"))
freq=[]
d={}
for j in range(len(s)-k):
	pat=s[j:j+k]
	cnt=p_count(s,pat)
	d[pat]=cnt
l1=sorted([(v,key) for key,v in d.items()],reverse=True)
for v,key in l1:
	print(key,v)
