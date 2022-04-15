class Solution:
   def maximumSumRectangle(self,r,c,M):
       #code here
       
       maxx=float("-inf")
       re=[]
       for p in range(r):
           re=[0]*c
           for i in range(p,r):
               for j in range(c):
                   re[j]+=M[i][j]
               summ=self.kadane(re)
               if summ>maxx:
                   maxx=summ
       return maxx
               
       
   def kadane(self,arr):
       cur_sum=0
       maxx=float('-inf')
       for i in range(len(arr)):
           cur_sum+=arr[i]
           if cur_sum>maxx:
               maxx=cur_sum
           if cur_sum<0:
               cur_sum=0
               
       return maxx
