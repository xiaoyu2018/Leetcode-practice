from binarytree import TreeNode

def buildTree(inorder:list, postorder:list) -> TreeNode:
    if(not len(postorder) or not len(inorder)):
        return None
    
    crt_val=postorder[-1]
    postorder.pop()
    root=TreeNode(crt_val)
    
    # 中序列表切割 
    idx=inorder.index(crt_val)
    left_in=inorder[:idx]
    right_in=inorder[idx+1:]

    # 后序列表切割(使用中序列表左区间长度切割)
    left_post=postorder[:idx]
    right_post=postorder[idx:]

    root.left=buildTree(left_in,left_post)
    root.right=buildTree(right_in,right_post)

    return root

