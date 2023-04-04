
def candy(ratings: list) -> int:
    size=len(ratings)
    allocation=[1]*size

    # 第一次贪心从左向右,如果比左面的rating大就比左面多分一个
    for i in range(1,size):
        if(ratings[i]>ratings[i-1]):
            allocation[i]=allocation[i-1]+1

    # 第二贪心从右向左，同时兼顾左右
    for i in range(size-1,0,-1):
        if(ratings[i-1]>ratings[i]):
            allocation[i-1]=max(allocation[i]+1,allocation[i-1])
    
    return sum(allocation)

print(candy([1,3,2,2,1]))