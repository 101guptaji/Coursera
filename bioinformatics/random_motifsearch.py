from random import randint

def HammingDistance(a1,a2):
	count=0
	#print("humming ",a1,a2)
	if(len(a1)==len(a2)):
		for i in range(len(a1)):
			if(a1[i]!=a2[i]):
				count+=1
	return count
def score(motifs):
	'''Returns the score of the dna list motifs.'''
	score = 0
	for i in range(len(motifs[0])):
		motif = ''.join([motifs[j][i] for j in range(len(motifs))])
		score += min([HammingDistance(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
		#print(score)
	return score

def P(kmer,d):
	
	c=1.0
	for i in range(len(kmer)):
		#print(float(d[kmer[i]][i]))
		c=float(c)*float(d[kmer[i]][i])
	return float(c)

def profile_most_probable_kmer(text, k, profile):
	value=0
	profile_kmer=''
	for i in range(len(text)-k):
		kmer=text[i:i+k]
		#print('kmer ',kmer)
		if(value<P(kmer,profile)):
			value=P(kmer,profile)
			profile_kmer=kmer
	return profile_kmer

def make_motifs(profile, dna, k):
	return [profile_most_probable_kmer(seq,k,profile) for seq in dna]

def make_profile(motifs):
	'''Returns the profile of the dna list motifs.'''
	profile = {}
	#prof=[]
	for i in range(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in range(len(motifs))])
		for nuc in 'ACGT':
			profile[nuc]=profile.get(nuc,[])+[float(col.count(nuc)+1)/float(len(col)+4)]
	return profile
def randomized_motif_search(dna,k,t):
	rand_ints = [randint(0,len(dna[0])-k) for a in range(t)]
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]
	#motifs=['CCA','CCT','CTT','TTG']
	bestmotifs=motifs
	while True:
		profile=make_profile(motifs)
		motifs=make_motifs(profile,dna,k)
		if(score(motifs)<score(bestmotifs)):
			bestmotifs=motifs
		else:
			return bestmotifs

if __name__ == '__main__':

	with open('randomsearch.txt') as input_data:
		k,t = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]
	print(randomized_motif_search(dna_list,k,t))
