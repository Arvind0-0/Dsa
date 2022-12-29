class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        pos = []
        neg = []
        # iterate over the list
        for i,ast in enumerate(asteroids):

            if ast > 0: # if positive simply add to stack
                pos.append((i,ast))
            else:
                while pos and -ast > pos[-1][1]: # all the smaller ones are destroyed
                    last = pos.pop()
                if pos and -ast == pos[-1][1]: # if equal both are destroyed
                    last = pos.pop()
                    continue
                if not pos: # nothing can destroy it so save
                    neg.append((i,ast))

        ans = []
        for _,val in neg+pos:
            ans.append(val)
        return ans
