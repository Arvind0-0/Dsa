def maxArea(A,le):
    
    i, j = 0, le-1
    ans = 0
    while i < j:
        ans = max(ans, (j-i)*min(A[i], A[j]))
        if A[j] < A[i]:
            j -= 1
        else:
            i += 1
    return ans
