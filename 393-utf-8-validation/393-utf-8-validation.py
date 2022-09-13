class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        l = [2**i for i in range(7, -1, -1)]
        
        def isXByteSeq(pos, X):
            f = data[pos]
            rem = data[pos+1:pos+X]
            ret = (f&l[X]) == 0
            for i in range(X):
                ret &= (f&l[i]) != 0
            for num in rem:
                ret &= (num&l[0]) != 0
                ret &= (num&l[1]) == 0
            return ret
            
        @cache
        def res(pos = 0):
            ret = False
            if pos == n:
                ret = True
            if pos + 3 < n:
                ret |= isXByteSeq(pos, 4) and res(pos + 4)
            if pos + 2 < n:
                ret |= isXByteSeq(pos, 3) and res(pos + 3)
            if pos + 1 < n:
                ret |= isXByteSeq(pos, 2) and res(pos + 2)
            if pos < n:
                ret |= isXByteSeq(pos, 0) and res(pos + 1)
            return ret
        
        return res()