def firstsymbol(pat):
    if(len(pat)==0):
        print("no pattern found")
    else:
        #print("firstsymbol ",pat[0])
        return pat[0]

def suffix(pat):
    if(len(pat)==0):
        print("no pattern found")
    else:
        #print("suffix ",pat[1:])
        return pat[1:]


def humming(a1,a2):
    count=0
    #print("humming ",a1,a2)
    if(len(a1)==len(a2)):
        for i in range(len(a1)):
            if(a1[i]!=a2[i]):
                count+=1
    return count
def nebrs(pat,d):
    if(d==0):
        return {pat}
    elif(len(pat)==1):
        return {'A','C','G','T'}
    nebrhood=set()
    suffixnebr=nebrs(suffix(pat),d)
    #print("suffixnebr ",suffixnebr)
    for text in suffixnebr:
        if(humming(suffix(pat),text)<d):
            for j in ['A','C','T','G']:
                nebrhood.add(j+text)
        else:
            nebrhood.add(firstsymbol(pat)+text)
        
    return nebrhood


def pat_count(s,pat,d):
	cnt=0
	s1=len(s)
	p=len(pat)
	for i in range(s1-p+1):
		pat2=s[i:i+p]
		if(humming(pat,pat2)<=d):
			cnt+=1
	return cnt

fname='freq_mispat.txt' #input("file name")
fhand=open(fname,'r')
s=fhand.readline()
#s='ACCTACCTGACGACCTGAGGGACGGACGTAGGGCTGACGGACGACCTACCTTAGGAGGTAGGAGGTAGGGCTGGCTGACGTAGTAGACCTGAGGGAGGGACGGAGGGAGGGACGGGCTTAGGAGGTAGGGCTGACGACCTGGCTACCTGACGGACGACCTACCTACCTTAGGAGGTAGTAGGACGGACGGGCTGGCTGAGGGACGGACGTAGGGCTACCTGAGGGACGGGCTACCTACCTTAGACCTGGCTTAGACCTACCTGAGGGAGGGAGGGGCTGACGACCTGGCTGACGACCTGACGTAGACCTACCTACCTGAGGTAGTAGTAGGACGACCTGACGGGCTTAGTAGGAGGGGCTGACG'
#s=input()
k,d=fhand.readline().split()
k=int(k)
d=int(d)
dic={}
pat_dict={}
for i in range(len(s)-k+1):
	pat=s[i:i+k]
	if(pat not in pat_dict.keys()):
		nebrset=nebrs(pat,d)
		pat_dict[pat]=nebrset
	else:
		continue
all_kmer=set()
for set1 in pat_dict.values():
	for ele in set1:
		all_kmer.add(ele)
#print(all_kmer)

for kmer in all_kmer:
	cnt=pat_count(s,kmer,d)
	dic[kmer]=cnt

#print(dic)
m=max(dic.values())
for key,val in dic.items():
	if(val==m):
		print(key,end=' ')




