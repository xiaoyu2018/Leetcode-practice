from typing import *

def minNumBooths(self, demand: List[str]) -> int:
    need=[0]*26
    
    for i in demand[0]:
        need[ord(i)-97]+=1

    for day in demand[1:]:
        temp=[0]*26
        for j in day:
            crt=ord(j)-97
            temp[crt]+=1
            if(temp[crt]>need[crt]):
                need[crt]=temp[crt]
    
    return sum(need)

from binarytree import TreeNode
def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if(root.left==None and root.right==None):
        return root
    lr=rr=None
    if(root.left!=None):
        lr=self.expandBinaryTree(root.left)
        root.left=TreeNode(-1,lr)

    if(root.right!=None):
        rr=self.expandBinaryTree(root.right)
        root.right=TreeNode(-1,None,rr)

    return root

def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:

    dp=[1]*100000
    size=len(flowers)
    for i in range(1,size):
        dp[i]=dp[i-1]
        temp=[0]*100000
        for j in range(i,-1,-1):
            temp[flowers[j]]+=1
            if(temp[flowers[j]]<=cnt):
                dp[i]+=1
            else:
                break
    
    return dp[size-1]%1000000007
