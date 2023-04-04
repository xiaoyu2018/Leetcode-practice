from binarytree import level_create
from collections import deque

def levelOrder(root) -> list:
    queue=deque()
    if(not root):
        return []
    queue.append(root)
    res=[[root.val]]

    while(queue):
        temp=[]
        size=len(queue)

        for _ in range(size):
            crt=queue.popleft()

            lc=crt.left
            if(lc):
                queue.append(lc)
                temp.append(lc.val)  
            rc=crt.right
            if(rc):
                queue.append(rc)
                temp.append(rc.val)

        if(temp):
            res.append(temp)

    return res
        

print(levelOrder(level_create([])))
# print([[]])