
def partitionLabels(s: str) -> list:

    res=[]
    memo=[-1]*26 # 统计字母在s中最后出现的位置
    count=0 # 统计当前分片的元素个数
    furthest=-1 #当前分片最远重复元素位置

    for i in range(len(s)):
        idx=ord(s[i])-ord('a')
        if(i>memo[idx]):
            memo[idx]=i
    
    for i in range(len(s)):
        idx=ord(s[i])-ord('a')
        furthest=max(furthest,memo[idx])
        count+=1

        if(i==furthest):
            res.append(count)
            count=0

    return res

print(partitionLabels("ababcbacadefegdehijhklij"))