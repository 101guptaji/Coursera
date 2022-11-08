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

def motiffind(dna,k,d):
    kmer_list=[]
    for pos, string in enumerate(dna):
        patterns=set()
        #print("string ", string)
        for i in range(len(string)-k+1):
            pat=string[i:i+k]
            #print('pat ',pat)
            nebrset=nebrs(pat,d)
            #print('nebrset ',nebrset)
            for pat1 in nebrset:
                patterns.add(pat1)
            #print("pattern ",patterns)
        kmer_list.append(patterns)
        #print(kmer_list)
    patt=kmer_list[0]
    for k_set in kmer_list:
        patt=patt & k_set
    return patt


k=int(input())
d=int(input())
'''
#fname=input("file name")
fname=open('motif.txt','r')
dna=[]
for line in fname:
    line.strip
    dna.append(line)
'''
dna=[
'GCAAAAGTAACTGAGTTGCACCCGT',
'AGTATGGTTAATTCATTGTCGTAAC',
'CTAGTGGAGTTTTGTGAAGTAGTAA',
'ATGGCAGTATCCAAGCCACCCTTGA',
'TCTTAAGTAAGAAATATGTACGGGA',
'ATCGTCGCCATCACCAGTAAACATG'
    ]
motifset=motiffind(dna,k,d)
#print(motifset)
for i in motifset:
    print(i,end=' ')
