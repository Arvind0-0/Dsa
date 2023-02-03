class Solution{
    
    private static int movex(int move, int x)
    {
        if(move==0) return x-1;
        if(move==2) return x+1;
        return x;
    }
    
    
    private static int movey(int move, int y)
    {
        if(move==1) return y+1;
        if(move==3) return y-1;
        return y;
    }
    
    
    static int [] endPoints(int [][]arr, int m, int n){
        int x = 0, y = 0, move = 1;
        
        while(x<m && y<n && x>=0 && y>=0)
        {
            if(arr[x][y]==1)
            {
                arr[x][y] = 0;
                move = (move+1)%4;
            }
            
            x = movex(move, x);
            y = movey(move, y);
            
        }
        
        if(x>=m) x--;
        if(x<0) x++;
        if(y>=n) y--;
        if(y<0) y++;
        
        
        return new int[]{x, y};
    }
}
 
