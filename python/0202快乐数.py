
def isHappy(n: int) -> bool:
    memo=set()

    while(True):
        s=sum([int(i)*int(i) for i in str(n)])

        if(s==1):
            return True
        if(s in memo):
            return False

        memo.add(s)
        n=s

