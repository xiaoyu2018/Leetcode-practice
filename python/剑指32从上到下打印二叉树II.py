from binarytree import TreeNode


def levelOrder(root: TreeNode) -> list:
    if(root==None):
        return []
    
    nodes=[root]
    res=[[root.val]]

    while(len(nodes)):
        crt=[]
        for node in nodes:
            if(node.left!=None):
                crt.append(node.left)
            if(node.right!=None):
                crt.append(node.right)
        nodes=crt

        if(len(crt)):
            res.append([i.val for i in crt])
    
    return res