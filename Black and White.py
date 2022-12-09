def numOfWays(M, N):
    total, squares = 0, N*M
    for x in range(N):
        for y in range(M):
            temp = squares-1
            if -1<x-2<N:
                if -1<y-1<M: temp-=1
                if -1<y+1<M: temp-=1
            if -1<x-1<N:
                if -1<y-2<M: temp-=1
                if -1<y+2<M: temp-=1
            if -1<x+1<N:
                if -1<y-2<M: temp-=1
                if -1<y+2<M: temp-=1
            if -1<x+2<N:
                if -1<y-1<M: temp-=1
                if -1<y+1<M: temp-=1
            total= (total+temp)%(10**9+7)
    return total
