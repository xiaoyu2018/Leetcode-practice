from binarytree import TreeNode
from collections import deque

def levelOrder(root: TreeNode) -> list:
    if(root==None):
        return []
    nodes=deque([root])
    flag=True
    res=[]
    while(len(nodes)):
        size=len(nodes)
        temp=[]
        for _ in range(size):
            crt=nodes.popleft()
            if(crt!=None):
                nodes.append(crt.left)
                nodes.append(crt.right)
                temp.append(crt.val)
        if(len(temp)):
            res.append(temp if flag else list(reversed(temp)))
        flag=not flag
        
    return res