class Solution:
   def countOfNodes(self, graph,n):
       # code here
       even=1
       odd=0
       q=[]
       q.append(1)
       flag=True
       visited={1}
       while q:
           p=[]
           while q:
               poped=q.pop(0)
               for i in graph[poped]:
                   if i not in visited:
                       p.append(i)
                       visited.add(i)
           if flag:
               odd+=len(p)
               flag=False
           else:
               even+=len(p)
               flag=True
           q=p
       return ((even)*(even-1)//2)+((odd)*(odd-1)//2)
