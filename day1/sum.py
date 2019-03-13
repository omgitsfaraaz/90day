
def sumDivisible(L, R): 
	
	p = int(R/6) 

	q = int((L-1)/6) 

	sumR = 3 * (p * (p + 1)) 

	sumL = (q * (q + 1)) * 3

	return sumR - sumL 

L = 1
R = 20
print(sumDivisible(L,R)) 

