def P(kmer,d):
	
	c=1.0
	for i in range(len(kmer)):
		#print(float(d[kmer[i]][i]))
		c=float(c)*float(d[kmer[i]][i])
	return float(c)

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
	if(value<P(kmer,d)):
		value=P(kmer,d)
		profile_kmer=kmer
print(profile_kmer)
