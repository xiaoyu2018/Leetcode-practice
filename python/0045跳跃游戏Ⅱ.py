
# 贪心
# 每次都跳到覆盖范围最大的下一个位置
def jump(nums: list) -> int:
    crt=0   #当前位置覆盖范围
    next=0  #下一跳能覆盖到的最大范围
    steps=0 #跳跃次数
    i=0

    while(i<len(nums)-1):
        
        # 用于获得crt范围内下一步能跳到的最远位置
        next=max(next,i+nums[i])

        # 到达crt也没到达末尾，所以要跳一次，不需要真的跳到那个位置，只需获取下一次能跳最远的位置的范围，然后继续遍历即可
        if(i==crt):
            # 改变范围
            crt=next
            steps+=1
        i+=1

    return steps

print(jump([1,1,2,1]))