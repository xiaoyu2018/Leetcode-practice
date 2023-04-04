from binarytree import TreeNode

# 递归
def invertTree(root: TreeNode) -> TreeNode:
    
    if(not (root and any([root.left,root.right]))):
        return root
    
    lc=invertTree(root.left)
    rc=invertTree(root.right)

    root.left=rc
    root.right=lc

    return root

from collections import deque

# 迭代
def invertTree1(root: TreeNode) -> TreeNode:
    nodes=deque([root])

    while(nodes):
        crt=nodes.pop()

        if(crt):
            nodes.append(crt.left)
            nodes.append(crt.right)

            crt.left,crt.right=crt.right,crt.left
    return root