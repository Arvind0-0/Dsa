 arr=[r,g,b]

        for i in range(N-2,-1,-1):

            arr[0][i]+=min(arr[1][i+1],arr[2][i+1])

            arr[1][i]+=min(arr[0][i+1],arr[2][i+1])

            arr[2][i]+=min(arr[1][i+1],arr[0][i+1])

        return min(arr[0][0],arr[1][0],arr[2][0])
