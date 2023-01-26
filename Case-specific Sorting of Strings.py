def caseSort(self,s,n):
        case = [1 if ele.isupper() else 0 for ele in s]
        s = sorted(list(s))
        upper = s[:sum(case)][::-1]
        lower = s[sum(case):][::-1]
        return ''.join([upper.pop() if x==1 else lower.pop() for x in case])
