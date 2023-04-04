# 按二维坐标象限分为四类
# 训练集中八条样本
dataset=[
    [1,1],[2,2],
    [-1,3],[-2,3],
    [-1,-1],[-2,-2],
    [1,-3],[2,-3],
]
# 标签按顺序对应样本
labels=[1,1,2,2,3,3,4,4]


def classifier(inX:list,dataset:list,labels:list,k:int=3)->list:
    
    # 计算得出待测样本inX和训练集中每个样本的距离，保存到列表dstance中
    distance=[((inX[0]-s[0])**2+(inX[1]-s[1])**2)**0.5  for s in dataset]

    # 将distance列表和标签按元素缝合成一个列表
    labeled_dis=zip(distance,labels)
    # print(list(labeled_dis))

    # 按距离将labeled_dis排序
    labeled_dis=sorted(labeled_dis,key=lambda x:x[0])
    print(list(labeled_dis))

    # 统计最近点类别个数的字典
    count_dict=dict()
    # 只需统计前k个
    for s in labeled_dis[:k]:
        if(s[1] not in count_dict.keys()):
            count_dict[s[1]]=1
        else:
            count_dict[s[1]]+=1
    
    # 把k个中最多的几个类别返回（可能重复）
    temp=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    
    # 分类结果
    m=temp[0][1]
    res=[t[0] for t in temp if t[1]==m]

    return res




print(classifier([2,-2],dataset,labels,4))
