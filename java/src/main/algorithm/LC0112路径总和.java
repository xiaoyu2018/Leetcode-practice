package main.algorithm;

public class LC0112路径总和 {

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null)
            return false;
        return _foo(root, root.val, targetSum);
    }

    private boolean _foo(TreeNode root,int sum,int targetSum)
    {
        if(root.left==null&&root.right==null)
            return sum == targetSum;
        boolean l_b=false,r_b=false;

        if(root.left!=null)
            l_b = _foo(root.left, sum + root.left.val, targetSum);
        if(root.right!=null)
            r_b = _foo(root.right, sum + root.right.val, targetSum);
        
        return l_b || r_b;
    }
}
