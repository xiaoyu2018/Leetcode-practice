
# 直接递归（超时）
def canJump1(nums: list) -> bool:
    border=len(nums)-1

    def _canJump(idx:int):

        if(idx+nums[idx]>=border):
            return True
        
        for i in range(idx+1,min(idx+nums[idx]+1,border)):
            if(_canJump(i)):
                return True
        
        return False

    return _canJump(0)

# 贪心
def canJump2(nums: list) -> bool:
    cover=0
    i=0

    while(i<=cover):

        if(cover>=len(nums)-1):
            return True
        cover=max(cover,i+nums[i])
        i+=1
    return False

print(canJump2([3,2,1,0]))