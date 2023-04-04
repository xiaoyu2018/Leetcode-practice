
def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    
    
    # 直接模拟
    crt_row=prev_row=[poured]
    
    for i in range(1,query_row+1):
        crt_row=[0]*(i+1)

        for j,v in enumerate(prev_row):
            if(v>1):
                crt_row[j]+=(v-1)/2
                crt_row[j+1]+=(v-1)/2
            prev_row=crt_row
    return min(1,crt_row[query_glass])
        




print(champagneTower(25,6,1))
