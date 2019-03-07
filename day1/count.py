
def divisible(N, digit): 

	ans = 0; 
	for i in range(len(N)): 
		ans = (ans * 10 + (ord(N[i]) - ord('0'))); 
		ans %= digit; 
	return (ans == 0); 

def allDigits(N): 

	divide =[False]*10; 
	divide[1] = True; 

	for digit in range(2,10): 
		if (divisible(N, digit)): 
			divide[digit] = True; 

	result = 0; 
	for i in range(len(N)): 
	
		if (divide[(ord(N[i]) - ord('0'))] == True): 
			result+=1; 

	return result; 

N = "122324"; 
print(allDigits(N)); 

