from binarytree import TreeNode
from collections import deque

# 层次遍历+判断回文
def isSymmetric(root: TreeNode) -> bool:
    if(not root):
        return True
    
    que=deque([root.left,root.right])

    while(len(que)):
        size=len(que)
        vals=[]

        for _ in range(size):
            crt=que.popleft()
            if(crt!=None):
                que.append(crt.left)
                que.append(crt.right)
            
            vals.append(None if crt==None else crt.val)
        
        v_size=len(vals)
        for i in range(v_size>>1):
            if(vals[i] != vals[v_size-1-i]):
                return False


    return True

def isSymmetric1(root: TreeNode) -> bool:

    def _check(r1:TreeNode,r2:TreeNode):
        if(r1==None and r2==None):
            return True
        if(r1==None or r2==None):
            return False
        
        return r1.val==r2.val and _check(r1.left,r2.right) and _check(r1.right,r2.left)
    
    return _check(root,root)