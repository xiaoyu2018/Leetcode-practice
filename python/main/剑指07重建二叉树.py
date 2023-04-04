from binarytree import TreeNode

def buildTree(preorder: list, inorder: list) -> TreeNode:
    
    # 建立中序列表元素到索引的哈希，降低遍历复杂度
    val2idx={v:i for i,v in enumerate(inorder)}

    def _build(pre_left,pre_right,in_left,in_right):
        if(pre_left>pre_right):
            return None
        
        crt_val=preorder[pre_left]
        root=TreeNode(crt_val)

        in_idx=val2idx[crt_val]
        len_left=in_idx-in_left
        
        root.left=_build(pre_left+1,pre_left+len_left,in_left,in_idx-1)
        root.right=_build(pre_left+len_left+1,pre_right,in_idx+1,in_right)

        return root

    return _build(0,len(preorder)-1,0,len(inorder)-1)
