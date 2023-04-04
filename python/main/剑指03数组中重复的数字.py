
def findRepeatNumber(nums: list) -> int:
    memo=set()
    memo.add(nums[0])
    for i in nums[1:]:
        if(i in memo):
            return i
        memo.add(i)
    return None