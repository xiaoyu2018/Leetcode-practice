
# 暴力
def fourSumCount1(nums1: list, nums2: list, nums3: list, nums4: list):
    s=0
    nums_len=len(nums1)

    for i in range(nums_len):
        for j in range(nums_len):
            for k in range(nums_len):
                for l in range(nums_len):
                    if(nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0):
                        s+=1
    
    return s

# 哈希加速
def fourSumCount2(nums1: list, nums2: list, nums3: list, nums4: list):
    memo=dict()
    count=0
    for i in nums1:
        for j in nums2:
            memo[i+j]= 1 if i+j not in memo.keys() else memo[i+j]+1
    
    for i in nums3:
        for j in nums4:
            if(-i-j in memo.keys()):
                count+=memo[0-i-j]
    
    return count