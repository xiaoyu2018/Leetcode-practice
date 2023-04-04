from functools import cmp_to_key

def minNumber(nums: list) -> str:
    def _comp(x:str,y:str):
        a,b=x+y,y+x
        if(a>b): return 1
        elif(a<b): return -1
        else:return 0
    
    s=[str(i) for i in nums]
    res=sorted(s,key=cmp_to_key(_comp))
    return "".join(res)
    
def minNumber(nums: list) -> str:
    def quick_sort(l , r):
        if l >= r: return
        i, j = l, r
        while i < j:
            while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
            while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
            strs[i], strs[j] = strs[j], strs[i]
        strs[i], strs[l] = strs[l], strs[i]
        quick_sort(l, i - 1)
        quick_sort(i + 1, r)
    
    strs = [str(num) for num in nums]
    quick_sort(0, len(strs) - 1)
    return ''.join(strs)



print(minNumber([3,30,34,5,9]))
