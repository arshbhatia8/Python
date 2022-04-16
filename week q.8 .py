for i in range(100,400+1):
    c=0
    t=i
    while(t>0):
        d=t%10
        if (d%2)==0:
            c=c+1
        t//=10
    if(c==3):
        print(i)