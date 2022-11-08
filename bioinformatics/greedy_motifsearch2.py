def findConsensus(Motifs):
	consensus = ''
	count={}
	for i in range(len(Motifs[0])):
		count['A'] = 0
		count['C'] = 0
		count['G'] = 0
		count['T'] = 0
		for motif in Motifs:
			print(motif,motif[i])
			count[motif[i]] = count[motif[i]] + 1
		max_val=max(count.values())
		for key,value in count.items():
			if(value==max_val):
				consensus = consensus + key
	return consensus
def humming(a1,a2):
    count=0
    #print("humming ",a1,a2)
    if(len(a1)==len(a2)):
        for i in range(len(a1)):
            if(a1[i]!=a2[i]):
                count+=1
    return count

def score(motifs):
	consensus = findConsensus(motifs)
	score = 0
	for motif in motifs:
		score += humming(consensus, motif)
	return score

def P(kmer,profile):
	
	c=1.0
	for i in range(len(kmer)):
		#print(float(d[kmer[i]][i]))
		c=float(c)*float(profile[kmer[i]][i])
	return float(c)

def profilemost_kmer(text,k,profile):
	value=0
	profile_kmer=''
	for i in range(len(text)-k):
		kmer=text[i:i+k]
		if(value<P(kmer,profile)):
			value=P(kmer,profile)
			profile_kmer=kmer
	return profile_kmer

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
	print("best_motif ",best_motifs)
	for i in range(len(DNA[0])-k):
		motifs=[DNA[0][i:i+k]]
		for j in range(1,len(DNA)):
			matrix=[]
			for kmer in motifs:
				matrix=make_matrix(kmer, matrix, t)
			profile=make_profile(matrix,t)
			if(len(profilemost_kmer(DNA[j],k,profile))>0):
				motifs.append(profilemost_kmer(DNA[j],k,profile))
		print('motif ',motifs)
		if(score(motifs)<score(best_motifs)):
			best_motifs=motifs
	return best_motifs




fname='greedymotif.txt' #input("file name")
fhand=open(fname,'r')
k,t=fhand.readline().split()
k,t=int(k),int(t)
dna=[]
for i in range(t):
	dna.append(fhand.readline().strip())
#print(dna)
print(GreedyMotifSearch(dna,k,t))

