#User function Template for python3

class Solution:
    def decodedString(self, s):
        stack=[]
        curstr=''
        curdig=''
        prevdig=''
        prevstr=''
        for i in range(len(s)):
            if s[i]=='[':
                stack.append(curstr)
                stack.append(curdig)
                curdig=''
                curstr=''
            elif s[i]==']':
                prevdig=stack.pop()
                prevstr=stack.pop()
                curstr=prevstr+curstr*int(prevdig)
            elif s[i].isdigit():
                curdig+=s[i]
            else:
                curstr+=s[i]
        return curstr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends