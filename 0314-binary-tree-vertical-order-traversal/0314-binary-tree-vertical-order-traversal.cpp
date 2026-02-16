/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        if (root == nullptr)
            return {};

        int min_col = 0, max_col = 0;
        queue<pair<TreeNode*, int>> qu;
        unordered_map<int, vector<int>> map;
        qu.push({root, 0});
        vector<vector<int>> res;

        while (!qu.empty()) {
            auto p = qu.front();
            qu.pop();
            TreeNode* node = p.first;
            int col = p.second;
            map[col].push_back(node->val);
            if (node->left != nullptr) {
                qu.push({node->left, col - 1});
                min_col = min(min_col, col - 1);
            } 
            if (node->right != nullptr) {
                qu.push({node->right, col + 1});
                max_col = max(max_col, col + 1);
            }
        }

        for (int col = min_col; col <= max_col; col++) {
            res.push_back(map[col]);
        }

        return res;
    }
};