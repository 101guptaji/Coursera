def humming(a1,a2):
    count=0
    #print("humming ",a1,a2)
    if(len(a1)==len(a2)):
        for i in range(len(a1)):
            if(a1[i]!=a2[i]):
                count+=1
    return count

def d(pat,dna):
	
	s1=len(dna[0])
	k=len(pat)
	d=0
	for s in dna:
		cnt=k*len(dna)
		for i in range(s1-k+1):
			pat2=s[i:i+k]
			if(cnt>humming(pat2,pat)):
				cnt=humming(pat2,pat)
		d+=cnt
			
	return d
def median(dna,k):
	dist=1000
	import itertools
	for pattern in itertools.product('ACGT',repeat=k):
		pat=''.join(pattern)
		if(dist>d(pat,dna)):
			dist=d(pat,dna)
			median=pat
	return median
'''dna=['AAATTGACGCAT',
'GACGACCACGTT',
'CGTCAGCGCCTG',
'GCTGAGCACCGG',
'AGTTCGGGACAG']'''
#d=input()
file=open('median.txt','r')
k = int(file.readline())
dna = file.readlines()
print(median(dna,k))
