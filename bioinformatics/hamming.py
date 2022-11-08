a1=input()
a2=input()
count=0
if(len(a1)==len(a2)):
	for i in range(len(a1)):
		if(a1[i]!=a2[i]):
			count+=1
print(count)
