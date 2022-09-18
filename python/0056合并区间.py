
def merge(intervals: list) -> list:

    res=[]

    intervals=sorted(intervals)
    l=intervals[0][0]
    r=intervals[0][1]

    for i in intervals[1:]:

        if(i[0]<=r):
            r=max(r,i[1])
        
        else:
            res.append([l,r])
            l=i[0]
            r=i[1]

    res.append([l,r])
    return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))