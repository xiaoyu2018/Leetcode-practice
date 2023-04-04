
# 两个维度就一定要先考虑其中一个，在考虑另一个进行重排
def reconstructQueue(people: list) -> list:

    # 先按身高从大到小排序，注意身高相同时第二项大的在后面
    people=sorted(people,key=lambda x:(-x[0],x[1]))

    res=[]

    # 直接把第二项当作索引插入，从前往后遍历，符合题目要求
    for i in people:
        res.insert(i[1],i)

    return res

print(reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))