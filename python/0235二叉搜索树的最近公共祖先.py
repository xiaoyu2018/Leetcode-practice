from binarytree import TreeNode

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
    if(root in [None,p,q]):
        return root
    
    if(p.val<root.val<q.val or q.val<root.val<p.val):
        return root
    
    if(root.val<p.val or root.val<q.val):
        return lowestCommonAncestor(root.right,p,q)
    
    # root.val>q or root.val>p
    return lowestCommonAncestor(root.left,p,q)