
# 暴力
def canCompleteCircuit(gas: list, cost: list) -> int:

    travel_len=len(gas)

    for i in range(travel_len):
        crt=i
        gas_storage=0
        steps=0
        
        while(steps<travel_len):
            gas_storage+=gas[crt]
            gas_storage-=cost[crt]
            if(gas_storage<0):
                break
            steps+=1
            if(steps==travel_len):
                return i
            crt=(crt+1)%travel_len
            

    return -1

def canCompleteCircuit1(gas: list, cost: list) -> int:

    n = len(gas)
    cur_sum = 0
    min_sum = float('inf')
    
    for i in range(n):
        cur_sum += gas[i] - cost[i]
        min_sum = min(min_sum, cur_sum)
    
    if cur_sum < 0: return -1
    if min_sum >= 0: return 0
    
    # 找到能把未来途中欠的油补上的起始位置
    for j in range(n - 1, 0, -1):
        min_sum += gas[j] - cost[j]
        if min_sum >= 0:
            return j
    
    return -1
            






print(canCompleteCircuit1([5,1,2,3,4],[4,4,1,5,1]))