


def wiggleMaxLength(nums:list) -> int:
    size=len(nums)

    if(size<2):
        return size
    
    # 最后一个元素直接看作峰值
    count=1
    cur_diff=0

    # 相当于在第零位前补一个相等的元素
    pre_diff=0
    for i in range(0,size-1):
        cur_diff=nums[i+1]-nums[i]
        # 等号是为了处理相等节点的情况
        if(any([pre_diff>=0 and cur_diff<0,pre_diff<=0 and cur_diff>0])):
            count+=1
            pre_diff=cur_diff
    
        
    return count


print(wiggleMaxLength([1,7,4,9,2,5]))