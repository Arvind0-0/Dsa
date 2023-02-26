def fun(i,visit,adj):

    visit[i]=1

    

    q=deque()

    t=0

    q.append(i)

    

    while q:

        t+=1

        

        u=q.popleft()

        

        for j in adj[u]:

            if visit[j]==0:

                q.append(j)

                visit[j]=1

    return t

        

 

class Solution:

    def findNumberOfGoodComponent(self, V, adj):

         

        visit=[0]*(V+1)

         

        c=0

        for i in range(1,V+1):

            if visit[i]==0:

                p=False

                a=fun(i,visit,adj)

                

                if a-1 == len(adj[i]):

                    for j in adj[i]:

                        if a-1 != len(adj[j]):

                            p=True

                    if p==False:

                        c+=1

        

        return c
