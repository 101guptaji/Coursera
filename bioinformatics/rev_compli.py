s=input()
str1=s.replace('A','%tmp%').replace('T','A').replace('%tmp%','T')
str1=str1.replace('G','%tmp%').replace('C','G').replace('%tmp%','C')
print(str1[::-1])
