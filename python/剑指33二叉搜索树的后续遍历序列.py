
def verifyPostorder(postorder: list) -> bool:

    def _foo(left:int,right:int):
        if(left>=right):
            return True

        # 划分左右子树
        p=left
        while(postorder[p]<postorder[right]):p+=1
        # 检查右子树值是否全部大于根节点
        m=p
        while(postorder[m]>postorder[right]):m+=1

        return m==right and _foo(left,p-1) and _foo(p,right-1)
    return _foo(0,len(postorder)-1)