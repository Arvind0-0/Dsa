class Solution:
    def minVal(self, a, b):
        abit = bin(a)[2:]
        bbit = bin(b)[2:]
        
        temp = []
        
        alen = len(abit)
        
        aco,bco = 0,0
        
        for i in range(alen):
            if abit[i] == "1":
                aco += 1
                temp.append(i)
        
        for ele in bbit:
            if ele == "1":
                bco += 1
               
        if bco > alen:
            return int("".join("1" for i in range(bco)),2)
        
        else:
            ans = [0]*alen
            
            for ele in temp:
                if bco > 0:
                    ans[ele] = 1
                else:
                    break
                bco -= 1
            j = alen-1
            while bco > 0:
                if ans[j] != 1:
                    ans[j] = 1
                    bco -= 1
                j -= 1
        return int("".join(str(ele) for ele in ans),2)
