from binarytree import TreeNode
from collections import deque

def largestValues(root:TreeNode) -> list:
    res=[]
    nodes=deque([root])

    while(nodes):
        max_in_level=float('-inf')
        size=len(nodes)

        for _ in range(size):
            crt=nodes.popleft()
            if(crt):
                max_in_level=crt.val if crt.val>max_in_level else max_in_level
                nodes.append(crt.left)
                nodes.append(crt.right)
        if(max_in_level!=float('-inf')):
            res.append(int(max_in_level))
    return res