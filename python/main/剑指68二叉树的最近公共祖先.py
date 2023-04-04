from binarytree import TreeNode

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    parents=dict()
    parents[root]=None

    def _get_parents(root:TreeNode):
        if(not root):
            return 
        if(root.left):
            parents[root.left]=root
            _get_parents(root.left)
        if(root.right):
            parents[root.right]=root
            _get_parents(root.right)
    
    _get_parents(root)

    visited=set()
    
    while(p!=None):
        visited.add(p.val)
        p=parents[p]
    
    while(q!=None):
        if(q.val in visited):
            return q
        q=parents[q]
    