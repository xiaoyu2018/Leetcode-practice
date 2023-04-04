from binarytree import TreeNode
from collections import deque

def averageOfLevels(root:TreeNode) -> list:
    res=[]

    nodes=deque([root])

    while(nodes):
        size=len(nodes)
        level_vals=[]

        for _ in range(size):
            crt=nodes.popleft()

            if(crt):
                level_vals.append(crt.val)
                nodes.append(crt.left)
                nodes.append(crt.right)
        
        if(level_vals):
            res.append(round(sum(level_vals)/len(level_vals),5))
        

    return res