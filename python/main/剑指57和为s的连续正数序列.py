

def findContinuousSequence(target: int) -> list:
    l=1
    r=2
    s=3
    res=[]
    while(r<target):
        if(s==target):
            res.append([i for i in range(l,r+1)])
            r+=1
            s+=r
        elif(s>target):
            s-=l
            l+=1
        else:
            r+=1
            s+=r
    return res