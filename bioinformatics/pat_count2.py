s=input()
pat=input()
count=0
k=len(pat)
for i in range(len(s)-k+1):
	pat1=s[i:i+k]
	if(pat==pat1):
		count+=1
print(count)
