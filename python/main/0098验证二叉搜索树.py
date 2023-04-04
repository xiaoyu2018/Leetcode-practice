from binarytree import TreeNode

# BST的中序遍历节点数值是从小到大. 
def isValidBST(self, root: TreeNode) -> bool:
    cur_max = -float("INF")
    def _isValidBST(root: TreeNode) -> bool: 
        nonlocal cur_max
        
        if not root: 
            return True
        
        is_left_valid = _isValidBST(root.left)

        if cur_max >= root.val: 
            return False
        cur_max = root.val
        
        is_right_valid = _isValidBST(root.right)
        
        return is_left_valid and is_right_valid
    return _isValidBST(root)
        
