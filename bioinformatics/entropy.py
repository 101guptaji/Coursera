import math

def entropy(values):
	TotalEntropy=0.0
	for value in values:
		if value > 0:
			TotalEntropy+= abs(value * math.log(value, 2))
		else: continue
            
	return(TotalEntropy)
values=[0.0,0,0.5,0.5]
print(entropy(values))
