def convert(self,arr, n):

# code here

 a=sorted(arr)

 d={}

 for i in range(n):

     d[a[i]]=i

 for i in range(n):

     arr[i]=d[arr[i]]

     

 return arr
