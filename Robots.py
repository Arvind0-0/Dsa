class Solution:
    def moveRobots (self, s1, s2):
        i = 0
        j = 0
        n = len(s1)
        while(i < n and j < n):
                if s1[i]=='#':
                    i+=1
                elif s2[j]=='#':
                    j+=1
                elif s1[i] != s2[j]:
                    return "No"
                elif s1[i]=='B' and i>j:
                    return "No"
                elif s1[i]=='A' and i<j:
                    return "No"    
                else: 
                    i+=1
                    j+=1
        return "Yes"
