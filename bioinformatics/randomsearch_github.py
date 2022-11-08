from random import randint

def HammingDistance(a1,a2):
	count=0
	#print("humming ",a1,a2)
	if(len(a1)==len(a2)):
		for i in range(len(a1)):
			if(a1[i]!=a2[i]):
				count+=1
	return count

def profile_with_pseudocounts(motifs):
	'''Returns the profile of the dna list motifs.'''
	profile = {}
	for i in range(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in range(len(motifs))])
		for nuc in 'ACGT':
			profile[nuc]=profile.get(nuc,[])+[float(col.count(nuc)+1)/float(len(col)+4)]

	return profile


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

def motifs_from_profile(profile, dna, k):
	return [profile_most_probable_kmer(seq,k,profile) for seq in dna]

def randomized_motif_search(dna,k,t):
	# Randomly generate k-mers from each sequence in the dna list.
	rand_ints = [randint(0,len(dna[0])-k) for a in range(t)]
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]
	#motifs=['TGA','GTT','CTT','TTG']
	#print(rand_ints,motifs)
	# Initialize the best score as a score higher than the highest possible score.
	best_score = [score(motifs), motifs]
	#print('best_score ',best_score)
	# Iterate motifs.
	while True:
		current_profile = profile_with_pseudocounts(motifs)
		motifs = motifs_from_profile(current_profile, dna_list, k)
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]
		else:
			return best_score

if __name__ == '__main__':

	with open('randomsearch.txt') as input_data:
		k,t = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	# Initialize the best scoring motifs as a score higher than the highest possible score.
	best_motifs = [k*t, None]
	# Repeat the radomized motif search 1000 times.
	for repeat in range(1000):
		current_motifs = randomized_motif_search(dna_list,k,t)
		#print(current_motifs)
		if (current_motifs[0] < best_motifs[0]):
			best_motifs = current_motifs
			#print(best_motifs)
	# Print and save the answer.
	print ('\n'.join(best_motifs[1]))
