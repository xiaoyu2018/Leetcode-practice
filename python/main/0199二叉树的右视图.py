from binarytree import TreeNode,level_create
from collections import deque

def rightSideView(root: TreeNode) -> list:
    res=[]
    nodes=deque([root])

    while(nodes):
        size=len(nodes)
        temp=None

        for _ in range(size):
            crt=nodes.popleft()

            if(crt):
                temp=crt.val
                nodes.append(crt.left)
                nodes.append(crt.right)
        
        if(temp!=None):
            res.append(temp)
    return res

print(rightSideView(level_create([0,1,2,None,3,4,None,None,5,9,None,None,6,10,None])))