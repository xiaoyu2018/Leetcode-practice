def moveZeroes(nums: list) -> None:
    size = len(nums)
    i = j = 0
    count = 0

    while i < size and j < size:

        while i < size and nums[i] != 0:
            i += 1
        while j < size and nums[j] == 0:
            j += 1

        if i < j < size:
            nums[i] = nums[j]
            nums[j] = 0
            i += 1
            j += 1
        if j < i < size:
            j += 1

nums=[0,1,0,3,12]
moveZeroes(nums)
print(nums)