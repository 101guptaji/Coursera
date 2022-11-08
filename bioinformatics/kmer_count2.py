
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
c=[]
for j in range(len(s)-k):
	pat=s[j:j+k]
	c.append(p_count(s,pat))
maxcount=max(c)
for j in range(len(s)-k):
	if(c[j]==maxcount):
		freq.append(s[j:j+k])
fr=set(freq)
print(fr)
