
def maximumUnits(boxTypes: list, truckSize: int) -> int:
    bt=sorted(boxTypes,key=lambda x:x[1],reverse=True)
    res=0

    for box in bt:
        if(box[0]>truckSize):
            res+=truckSize*box[1]
            break
        
        truckSize-=box[0]
        res+=box[0]*box[1]
    return res

