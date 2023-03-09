    def findAnagrams(self, head, s):
        N = len(s)
        TAR = [0]*26
        for c in s: TAR[ord(c)-97]+=1
        ans, h, t, F = [], head, head, None
        while t:
            if F is None:
                F = [0]*26
                for _ in range(N):
                    if t is None: break
                    F[ord(t.data)-97]+=1
                    t=t.next
            else:
                F[ord(h.data)-97]-=1
                F[ord(t.data)-97]+=1
                h, t = h.next, t.next
                
            if F==TAR: 
                ans.append(h)
                while h.next != t: h = h.next
                h.next = None
                h = t
                F = None
                
        return ans
