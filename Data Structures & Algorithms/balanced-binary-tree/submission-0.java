/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isBalanced(TreeNode root) {
        boolean[] balanced = new boolean[1];
        balanced[0] = true;
        dfs(root, balanced);
        return balanced[0];
    }

    private int dfs(TreeNode root, boolean[] balanced) {
        if (root == null) {
            return 0;
        }

        int left = dfs(root.left, balanced);
        int right = dfs(root.right, balanced);
        if (left - right > 1 || right - left > 1) {
            balanced[0] = false;
        }
        return 1 + Math.max(left, right);
    }
}
