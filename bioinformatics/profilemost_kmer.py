def Probb(kmer,d):
	
	c=1
	for i in range(len(kmer)):
		print(float(d[kmer[i]][i])
		#float(c)=float(c)*float(d[kmer[i]][i])
	return c

fname='profile.txt' #input("file name")
fhand=open(fname,'r')
text=fhand.readline()
k=int(fhand.readline())
d={}
for key in ['A','C','G','T']:
	prob=fhand.readline().strip()
	l1=prob.split()
	d[key]=l1
print(d)
value=0
profile_kmer=''
for i in range(len(text)-k):
	kmer=text[i:i+k]
	#print('kmer ',kmer)
	if(value<Probb(kmer,d)):
		value=Probb(kmer,d)
		profile_kmer=kmer
print(profile_kmer)
