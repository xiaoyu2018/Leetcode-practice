from collections import Counter

# 哈希
def majorityElement(nums: list) -> int:
    return Counter(nums).most_common(1)[0][0]

# 排序
def majorityElement1(nums: list) -> int:
    return sorted(nums)[len(nums)//2]

print(majorityElement1([3,1,2,3,3]))