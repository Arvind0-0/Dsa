import math

class Solution:
	def NthTerm(self, N):
	    if self.is_prime(N):
	        return 0
        else:
            i = 1
            while True:
                if self.is_prime(N - i) or self.is_prime(N + i):
                    return i
                else:
                    i += 1
		
    
    def is_prime(self, num):
        if num <= 1:
            return False
        upper_limit = math.floor(math.sqrt(num)) + 1
        for i in range(2, upper_limit):
            if num % i == 0:
                return False
        return True
