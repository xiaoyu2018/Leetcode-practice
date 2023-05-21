from binarytree import *

def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    leaves1=[]
    leaves2=[]

    def _bfs(root:TreeNode,leaves:list):
        if(root.left==None and root.right==None):
            leaves.append(root.val)
            return
        
        _bfs(root.left,leaves)                
        _bfs(root.right,leaves)

    _bfs(root1,leaves1)
    _bfs(root2,leaves2)

    print(leaves1)
    print(leaves2)
    return leaves1==leaves2
