from functools import lru_cache

# 暴力回溯，超时
def splitArraySameAverage(nums:list) -> bool:
    total_s=sum(nums)
    total_i=len(nums)
    crt_s=0
    res=False

    # @lru_cache #追加记忆化操作，输出错误
    def _back_tracking(start):
        nonlocal total_i,total_s,crt_s,res
        
        for i in range(start,total_i-1):
            crt_s+=nums[i]
            if(crt_s/(start+1)==(total_s-crt_s)/(total_i-start-1)):
                res=True
                return
            _back_tracking(start+1)
            crt_s-=nums[i]

            
    _back_tracking(0)
    return res

