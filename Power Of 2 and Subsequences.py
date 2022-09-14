class Solution:
  def numberOfSubsequences(ob,N,A):
        return ((2**len([1 for i in A if i&i-1 == 0]))-1) % 1000000007
