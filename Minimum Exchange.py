def MinimumExchange(self, matrix):
		# Code here
		
		m=len(matrix)
		n=len(matrix[0])
		
		seq1, seq2=0,0
		
		for i in range(m):
		    for j in range(n):
		        if matrix[i][j]=='A':
		            if (i+j)%2==0:
		                seq1+=1
		            else:
		                seq2+=1
		        else:
		            if (i+j)%2==0:
		                seq2+=1
		            else:
		                seq1+=1

		ans=min(seq1, seq2)
		if ans%2==0:
		    return ans//2
		return min(ans, (m*n-ans)//2)
