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

    p_parents=[p]
    q_parents=[q]
    
    while(p!=None):
        p_parents.append(parents[p])
        p=parents[p]
    while(q!=None):
        q_parents.append(parents[q])
        q=parents[q]
    p_parents.pop()
    q_parents.pop()
    
    for i in p_parents:
        for j in q_parents:
            if(i.val==j.val):
                return i