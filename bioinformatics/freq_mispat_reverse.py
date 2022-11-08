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


def pat_count(kmer_list,pat,d):
	cnt=0
	for pat2 in kmer_list:
		if(humming(pat,pat2)<=d):
			cnt+=1
	return cnt

fname='freq_mispat_rev.txt' #input("file name")
fhand=open(fname,'r')
s=fhand.readline()
k,d=fhand.readline().split()
k=int(k)
d=int(d)
dic={}
pat_dict={}
kmer_list=[]
for i in range(len(s)-k+1):
	pat=s[i:i+k]
	kmer_list.append(pat)
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
	cnt1=pat_count(kmer_list,kmer,d)
	str1=kmer.replace('A','%tmp%').replace('T','A').replace('%tmp%','T')
	str1=str1.replace('G','%tmp%').replace('C','G').replace('%tmp%','C')
	cnt2=pat_count(kmer_list,str1[::-1],d)
	dic[kmer]=cnt1+cnt2

#print(dic)
m=max(dic.values())
for key,val in dic.items():
	if(val==m):
		print(key,end=' ')


