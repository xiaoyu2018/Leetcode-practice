def two():
    input()
    expr=input()

    memo={
        ("!","!"):0,
        ("@","@"):7,
        ("#","#"):5,
        ("!","@"):13,
        ("@","!"):13,
        ("#","!"):4,
        ("!","#"):4,
        ("@","#"):20,
        ("#","@"):20,
        }
    
    a,b=expr.split("+")
    a=a.split(".")
    a_1=a[0]
    a_2=a[1] if len(a)==2 else ""
    

    b=b.split(".")
    b_1=b[0]
    b_2=b[1] if len(b)==2 else ""
    res=[]
    flag=0

    # 计算小数部分，向后补零
    
    l1=len(a_2)
    l2=len(b_2)
    size=l1
    diff=l1-l2
    if(diff>0):
        b_2+="0"*diff
        size=l1
    if(diff<0):
        a_2+="0"*(-diff)
        size=l2
    
    for i in range(size-1,-1,-1):
        crt=0
        if(a_2[i].isdigit()):
            crt=int(a_2[i])+int(b_2[i])
        else:
            crt=memo[(a_2[i],b_2[i])]
        m=(crt+flag)%10
        n=(crt+flag)//10
        flag=n
        res.append(str(m))
    res.append(".")

    #计算整数部分，前面补零
    l1=len(a_1)
    l2=len(b_1)
    size=l1
    diff=l1-l2
    if(diff>0):
        b_1=b_1+"0"*diff
        size=l1
    if(diff<0):
        a_1=a_1+"0"*(-diff)
        size=l2

    for i in range(size-1,-1,-1):
        crt=0
        if(a_1[i].isdigit()):
            crt=int(a_1[i])+int(b_1[i])
        else:
            crt=memo[(a_1[i],b_1[i])]
        m=(crt+flag)%10
        n=(crt+flag)//10
        flag=n
        res.append(str(m))

    print("".join(res[::-1]))







if __name__=='__main__':
    two()
