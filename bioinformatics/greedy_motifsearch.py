#www.csbio.unc.edu/mcmillan/Comp555S16/Lecture05.html
def P(kmer,profile):
	
	c=1.0
	for i in range(len(kmer)):
		#print(float(d[kmer[i]][i]))
		c=float(c)*float(profile[kmer[i]][i])
	return float(c)
def make_profile(matrix,t):
	profile={'A':[], 'C':[], 'G':[], 'T':[]}
	for columns in range(len(matrix)):
		for keys in matrix[columns]:
			profile[keys]+=[matrix[columns][keys]/t]
	print(profile)
	return profile
def make_matrix(string, matrix, t):
	if len(matrix)==0:
		for ch in string:
			new_dict = {'A':0, 'C':0, 'G':0, 'T':0}
			new_dict[ch] =1
			matrix += [new_dict]
		#print(matrix)
		return matrix
	elif len(matrix)==len(string):
		for j in range(len(string)):
			matrix[j][string[j]] += 1
		#print(matrix)
	
	return matrix
	 


def GreedyMotifSearch(DNA, k, t):
	best_motifs = [i[0:k] for i in DNA]
	motifs=[]
	for i in range(len(DNA[0])-k):
		motifs.append(DNA[0][i:i+k])
	matrix=[]
	for kmer in best_motifs:
		matrix=make_matrix(kmer, matrix, t)
	profile=make_profile(matrix,t)
	for dna1 in DNA:
		value=0
		profile_kmer=''
		for i in range(len(dna1)-k):
			kmer=dna1[i:i+k]
			#print('kmer ',kmer)
			if(value<P(kmer,profile)):
				value=P(kmer,profile)
				profile_kmer=kmer
		print(profile_kmer)
    


fname='greedymotif.txt' #input("file name")
fhand=open(fname,'r')
k,t=fhand.readline().split()
k,t=int(k),int(t)
dna=[]
for i in range(t):
	dna.append(fhand.readline().strip())
#print(dna)
GreedyMotifSearch(dna,k,t)

