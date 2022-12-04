class Solution:
    def rearrange(self, S, N):
        # code here
        vowels = sorted(c for c in S if c in ["a","e","i","o","u"])
        others = sorted(c for c in S if c not in ["a","e","i","o","u"])
        if len(vowels) == len(others) + 1:
            ans = [x for t in zip(vowels, others) for x in t] + [vowels[-1]]
        elif len(vowels) + 1 == len(others):
            ans = [x for t in zip(others, vowels) for x in t] + [others[-1]]
        elif len(vowels) == len(others):
            if vowels > others:
                ans = [x for t in zip(others, vowels) for x in t]
            else:
                ans = [x for t in zip(vowels, others) for x in t]
        else:
            ans = ["-1"]
        return "".join(ans)
