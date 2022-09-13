

def lemonadeChange(bills:list) -> bool:
    five_dollars=0
    ten_dollars=0

    for i in bills:
        if(i==5):
            five_dollars+=1
            continue

        if(i==10):
            five_dollars-=1
            ten_dollars+=1
        
        if(i==20):
            if(ten_dollars):
                ten_dollars-=1
                five_dollars-=1
            else:
                five_dollars-=3

        if(any([five_dollars<0,ten_dollars<0])):
            return False
    
    return True