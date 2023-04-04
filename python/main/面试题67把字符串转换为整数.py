def strToInt(str: str) -> int:
    flag=res=None
    
    for c in str:
        if(c=='-'):
            if(flag==None and res==None):
                flag=-1
            else:
                break
        elif(c=='+'):
            if(flag==None and res==None):
                flag=1
            else:
                break
        elif(c=='0'):
            if(res==None or res==0):
                res=0
            else:
                res*=10
            if(flag==None):
                flag=1
        
        elif(c==' '):
            if(res==None and flag==None):
                continue
            else:
                break

        elif('1'<=c<='9'):
            if(res==None):
                res=int(c)
            else:
                res=res*10+int(c)
            if(flag==None):
                flag=1
        else:
            break

    if res and flag:
        if(flag==1):
           return min(res,2147483647)
        else:
            return max(-2147483648,-res)
    else:
        return 0


a=123
print(-a)