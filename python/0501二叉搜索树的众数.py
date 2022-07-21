from binarytree import TreeNode,level_create


def findMode(root: TreeNode) -> list:

    counts=[0,0]
    res=[]
    pre=None

    def _traversal(root:TreeNode):
        nonlocal pre
        if(root):
            _traversal(root.left)
            
            if(pre==None or pre.val==root.val):
                counts[0]+=1
            else:
                counts[0]=1

            pre=root
            if(counts[0]==counts[1]):
                res.append(root.val)
            
            if(counts[0]>counts[1]):
                counts[1]=counts[0]
                res.clear()
                res.append(root.val)
            
            _traversal(root.right)

    _traversal(root)
    return res

print(findMode(level_create([0])))