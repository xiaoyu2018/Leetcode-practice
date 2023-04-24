package main.algorithm;


public class LC0450删除二叉搜索树中的节点 {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root==null)
            return null;
        
        if (root.val > key)
            root.left = deleteNode(root.left, key);
        if (root.val < key)
            root.right = deleteNode(root.right, key);
        
        if (root.val == key)
        {
            if (root.left == null && root.right == null && root.val == key)
                return null;
            if(root.left==null)
                return root.right;
            if(root.right==null)
                return root.left;
            
            // 左右子树都不为空时，直接找右子树中最左面的节点
            TreeNode prev = root;
            TreeNode crt = root.right;

            while(crt.left!=null)
            {
                prev = crt;
                crt = crt.left;
            }
            
            crt.left = root.left;
            prev.left = crt.right;
            if(root.right!=crt)
                crt.right = root.right;
            
            return crt;
        }

        return root;
    }
}
