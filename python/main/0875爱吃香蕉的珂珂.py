def minEatingSpeed(piles: list, h: int) -> int:
    def _check(mid:int,h:int):
        count=0
        for pile in piles:
            count+=pile//mid if pile%mid==0 else pile//mid+1

        return count<=h
    
    l=1
    r=max(piles)

    while(l<=r):
        mid=l+((r-l)>>1)
        if(_check(mid,h)):
            l=mid+1
        else:
            r=mid-1

    return l
