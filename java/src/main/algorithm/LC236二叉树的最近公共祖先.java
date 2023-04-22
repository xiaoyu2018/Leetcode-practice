package main.algorithm;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LC236二叉树的最近公共祖先 {
    Map<TreeNode, TreeNode> memo = new HashMap<>();

    private void _getRoot(TreeNode root, TreeNode base) {
        if (root != null) {
            memo.put(root, base);
            _getRoot(root.left, root);
            _getRoot(root.right, root);
        }

    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        _getRoot(root, null);
        TreeNode res = null;

        Set<TreeNode> visited = new HashSet<>();

        for (res = p; res != null; res = memo.get(res)) {
            visited.add(res);
            if (res == q)
                break;
        }

        for (res = q; res != null; res = memo.get(res)) {
            
            if (visited.contains(res))
                break;
        }
        return res;
    }
}
