
class Solution:
    
    def pseudoPalindromicPaths (self, root):
        def helper(node):
                if node==None:
				# when we will call the left or right child of leaf node or our node will be empty
        
                    return
                dict[str(node.val)]+=1
				#we will increase the occurece of digit by one 
                if node.left==None and node.right==None:
				#  this if condition is for the child nodes, where we will check whether it is palindromic or not
                 
                # here we are checking whether number of occurence of each integer is odd or even and counting the odd one, if we have odd occurence more than one it means it won't be palindromic so we are not increasing the ans value
                    c=0
                    for i in dict:
                        if dict[i]%2!=0:
                            c+=1
                    if c<=1:
                        ans[0]+=1
                helper(node.left)
                helper(node.right)
                dict[str(node.val)]-=1
        dict=defaultdict(lambda:0)
		#for storing the occurence of each integer
        ans=[0]
        # storing the number of palindrome
        helper(root)
        return(ans[0])