
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

def level_create(vals:list):
    from collections import deque
    if(not vals):
        return None
    root=TreeNode(vals[0])
    nodes=deque([root])
    size=len(vals)
    idx=1
    
    while(idx<size):
        lc=TreeNode(vals[idx]) if vals[idx]!=None else None
        idx+=1
        rc=None if (idx>=size or vals[idx]==None) else TreeNode(vals[idx])
        idx+=1

        crt=nodes.popleft()
        crt.left=lc
        crt.right=rc

        if(lc):
            nodes.append(lc)
        if(rc):
            nodes.append(rc)

    return root

if __name__=='__main__':
    root=level_create([1,2,3,4,5,6,7])
    