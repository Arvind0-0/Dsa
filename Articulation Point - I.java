class Solution
{
    HashSet<Integer> set;   
    public ArrayList<Integer> articulationPoints(int v , ArrayList<ArrayList<Integer>> adj)
    {
        int[] tin = new int[v];
        int[] low = new int[v];
        int[] visited = new int[v];
        set = new HashSet<>();
        
        solve(adj , 0 , -1 , tin , low ,visited , 1);
        
        Iterator<Integer> it = set.iterator();
        
        ArrayList<Integer> ll = new ArrayList<>();
        
        while(it.hasNext()){
            ll.add(it.next());
        }
        if(ll.size() == 0)
            ll.add(-1);
            
        Collections.sort(ll);
        return ll;
        
    }
    
    void solve(ArrayList<ArrayList<Integer>> adj ,int src , int parent , int[] tin , int[] low , int[] visited, int timer){
        
        visited[src] = 1;
        low[src] = tin[src] = timer++;
        
        int child = 0;
        for(Integer nn : adj.get(src)){
            
            if(visited[nn] == 0 ){
                solve(adj , nn , src, tin , low , visited , timer);
                low[src] = Math.min(low[src] , low[nn]);
                
                if(low[nn] >= tin[src] && parent != -1){
                    set.add(src);
                }
                
                child++;
            }
            else{
                low[src] = Math.min(low[src] , tin[nn] ); 
            }
            
        }
        
        if(child > 1 && parent == -1){
            set.add(src);
        } 
    } 
}
