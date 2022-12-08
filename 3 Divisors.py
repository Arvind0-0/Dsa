from math import sqrt
class Solution:
    def sieve(self, n):
        primes = [True]*(n+1)
        primes[0] = primes[1] = False
        
        for i in range(2, n+1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False
        return primes
        
        
	def threeDivisors(self, query, q):
	    primes = self.sieve(10**6)
	    for i in range(1, len(primes)):
	        primes[i] += primes[i-1]
	        
		return [primes[int(sqrt(qi))] for qi in query]
