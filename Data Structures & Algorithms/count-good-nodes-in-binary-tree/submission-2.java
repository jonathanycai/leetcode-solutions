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
    public int goodNodes(TreeNode root) {
        int[] count = new int[1];
        counter(root, count, root.val);
        return count[0];
    }

    public void counter(TreeNode root, int[] count, int largest) {
        if (root == null) {
            return;
        }

        if (root.val >= largest) {
            count[0] += 1;
        }

        largest = Math.max(root.val, largest);

        counter(root.left, count, largest);
        counter(root.right, count, largest);

    }
}
