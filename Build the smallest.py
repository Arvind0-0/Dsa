def buildLowestNumber(self, S,N):
        # code here
        stack = []
        
        for i in S:
            if len(stack) and stack[-1] > i:
                while N > 0 and len(stack) and stack[-1] > i:
                    stack.pop()
                    N -= 1
                stack.append(i)
            else:
                stack.append(i)
        while N > 0:
            stack.pop()
            N -= 1
        ans = ''.join(stack)
        result = ans.lstrip('0')
        if len(result) == 0:
            return "0"
        return result
