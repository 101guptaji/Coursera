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

pat=input()
d=int(input())
print(nebrs(pat,d))
