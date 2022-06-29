
class TreeNode:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None


def pre_create(vals:list):
    vals=iter(vals)
    def _create():
        try:
            val=next(vals)
            if(val==None):
                raise Exception()
            
            root=TreeNode(val)
            root.left=_create()
            root.right=_create()

            return root
        
        except:
            return None

    return _create()


if __name__=='__main__':
    root=pre_create([1,None,2,3])
