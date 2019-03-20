MAX_DIGITS = 20; 

def isOctal(n): 
	while(n): 
		if((n % 10) >= 8): 
			return False
		else: 
			n = int(n / 10) 
	return True

def isPalindrome(n): 
	divide = 8 if(isOctal(n) == False) else 10

	octal=[] 

	while (n != 0): 
		octal.append(n % divide) 
		n = int(n / divide) 

	j = len(octal)-1
	k = 0
	while(k <= j): 
		if(octal[j] != octal[k]): 
			return False
		j-=1
		k+=1
	return True


if __name__=='__main__': 
	n = 97; 
	if (isPalindrome(n)): 
		print("Yes") 
	else: 
		print("No") 

