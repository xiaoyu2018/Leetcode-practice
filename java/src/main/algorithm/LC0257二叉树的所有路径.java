package main.algorithm;

import java.util.ArrayList;
import java.util.List;



public class LC0257二叉树的所有路径 {

    List<String> res = new ArrayList<String>(100);

    public List<String> binaryTreePaths(TreeNode root) {

        _foo(root, String.valueOf(root.val));
        return res;
    }
    
    private void _foo(TreeNode root,String path)
    {
        
        if(root.left==null&&root.right==null)
            res.add(path);
        if (root.left != null)
            _foo(root.left, path+"->"+root.left.val);
        if (root.right != null)
            _foo(root.right, path+"->"+root.right.val);
        
    }
}

