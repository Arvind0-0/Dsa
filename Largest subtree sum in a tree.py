class Solution {
  public:
    int res;
    int dfs(Node* root) {
        if(!root) return 0;
        int sum = root->data + dfs(root->left) + dfs(root->right);
        res = max(res, sum);
        return sum;
    }
    
    int findLargestSubtreeSum(Node* root) {
        res = -1e9;
        dfs(root);
        return res;
    }
};
