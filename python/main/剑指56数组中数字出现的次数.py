
def singleNumbers(nums:list) -> list:
    s=set()

    for num in nums:
        s.remove(num) if num in s else s.add(num)
    
    return list(s)
    