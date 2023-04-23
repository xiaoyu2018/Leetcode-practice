package main.algorithm;

public class LC0701二叉搜索树的插入操作 {
    public TreeNode insertIntoBST(TreeNode root, int val) {

        if (root == null) {
            return new TreeNode(val);
        }

        if (val > root.val) {
            TreeNode tmp = insertIntoBST(root.right, val);
            if (root.right == null)
                root.right = tmp;
        }
        if (val < root.val) {
            TreeNode tmp = insertIntoBST(root.left, val);
            if (root.left == null)
                root.left = tmp;
        }

        return root;
    }
}
