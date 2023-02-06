class Solution{
    private:
    Node*givetarget(Node*root,int target){
        Node*temp=root;
        while(temp){
            if(target<temp->data){
                temp=temp->left;
            }
            else if(target>temp->data){
                temp=temp->right;
            }
            else{
                return temp;
            }
        }
        return NULL;
    }
    void givesum(Node*root,long long int &sum){
        queue<pair<Node*,int>>q;
        q.push({root,0});
    
        while(!q.empty()){
            auto node=q.front();
            q.pop();
            Node*temp=node.first;
            int v=node.second;
            if(temp!=root && v==0){
                sum+=temp->data;
            }
            if(temp->left){
                q.push({temp->left,v-1});
            }
            if(temp->right){
                q.push({temp->right,v+1});
            }
            
        }
    }
    
public:
    long long int verticallyDownBST(Node *root,int target){
        Node*node=givetarget(root,target);
        if(node==NULL){
            return -1;
        }
        long long int sum=0;
        givesum(node,sum);
        return sum;
    }
};
