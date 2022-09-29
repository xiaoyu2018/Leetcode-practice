from typing import *

def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    return [i[0] for i in sorted(zip(names,heights),key=lambda x:x[1])][::-1]


def longestSubarray(self, nums: List[int]) -> int:
    size=len(nums)
    if(size==1):
        return 1

    temp_l=[1]
    temp_v=1
    dp=[nums[0]]*size
    for i in range(1,size):
        
        if(nums[i]<=(nums[i]&dp[i-1])):
            dp[i]=nums[i]&dp[i-1]
            temp_v+=1
        else:
            dp[i]=nums[i]
            temp_v=1
        temp_l.append(temp_v)

    print(dp)
    print(temp_l)
    return max(zip(dp,temp_l))[1]

def goodIndices(self, nums: List[int], k: int) -> List[int]:
    size=len(nums)
    left_dp=[1]*size
    right_dp=[1]*size

    for i in range(1,size):
        if(nums[i]<=nums[i-1]):
            left_dp[i]+=left_dp[i-1]
    for i in range(1,size):
        if(nums[i]>=nums[i-1]):
            right_dp[i]+=right_dp[i-1]
    print(left_dp)
    print(right_dp)
    return [i for i in range(k,size-k) if left_dp[i-1]>=k and right_dp[i+k]>=k]

print(goodIndices(None, [2,1,1,1,3,4,1],2))