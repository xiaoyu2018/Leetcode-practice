from binarytree import TreeNode

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    p_path=[]
    q_path=[]

    def _get_path(root:TreeNode,obj:TreeNode,path:list):
        path.append(root)
        if(root==obj):
            return
        if(root.val<obj.val):
            _get_path(root.right,obj,path)
        else:
            _get_path(root.left,obj,path)

    _get_path(root,p,p_path)
    _get_path(root,q,q_path)

    size=min(len(p_path),len(q_path))
    
    i=0
    while (i<size-1):
        if(p_path[i+1]!=q_path[i+1]):
            return p_path[i]
        i+=1
    return p_path[i]