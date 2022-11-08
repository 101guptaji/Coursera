def text(i,p):
	str4=''
	l2=[]
	while(i<len(t)-p-1):
		x=[]
		for k in range(p):
			x.append(t[i+k])
		#print("x=",x)
		str3=''
		for ele in x:
			str3+=ele
		#print(str1)
		n=len(s)
		if( str3 in s[i+p:n]):
			if( str3 not in str4):
				#print(str3)
				l2.append(str3)
				str4+=str3
		i+=1
	#print(l2)
	return l2


def p_count(s, pat):
	count = 1
	i=s.find(pat)
	while(i<len(t)-len(pat) and i!=-1):
		#print(t,i,pat)
		if pat in text(i, len(pat)):
			count = count + 1
		i=s.find(pat,i+1)
		#print(i)
	return count


s=input("enter text")
p=int(input("enter k"))
t=[]
for i in s:
	t.append(i)
#print(t)
str2=''
c=0
l1=[]
print("Ans.3.2",p,"-mer in text ",s,"are ")
for i in range(len(t)-p-1):
	x=[]
	for k in range(p):
		x.append(t[i+k])
	#print("x=",x)
	str1=''
	for ele in x:
		str1+=ele
	#print(str1)
	n=len(s)
	if( str1 in s[i+p:n]):
		if( str1 not in str2):
			print(str1)
			l1.append(str1)
			str2+=str1
#print(l1)
for j in l1:
	print(j,p_count(s,j))
