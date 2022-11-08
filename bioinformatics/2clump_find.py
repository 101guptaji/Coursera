s=input("enter text")
k=int(input("enter k"))
L=int(input("enter L"))
t=int(input("enter t"))

for i in range(len(s)-L):
    d={}
    for j in range(L-k):
        pat=s[i+j:k]
        d[pat]=d.get(pat,0)+1
    print(d)
    for key in d.keys():
        if(d[key]>=t):
            print(key)
