
points = [[1,2],[3,4],[5,6],[7,8]]

def findMinArrowShots(points: list) -> int:
    points=sorted(points,key=lambda x:x[0])
    print(points)
    res=1
    r=points[0][1]
    
    for p in points[1:]:
        if(p[0]>r):
            res+=1
            r=p[1]
        elif(p[1]<r):
            r=p[1]

    return res


print(findMinArrowShots((points)))