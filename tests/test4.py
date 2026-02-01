#only print values without keys
x={id:['id','name','point'],1:['1','ashin','10'],2:['2','anatte','20']}
def box(d):
    l1=[]
    l2=[]
    l0=[]
    for k,l in d.items():
        l0.append(len(l[0]))
        l1.append(len(l[1]))
        l2.append(len(l[2]))
    l0m=max(l0)
    l1m=max(l1)
    l2m=max(l2)
    lm=[l0m,l1m,l2m]
    for i in lm:
        ll=i+2
        print(" ", end="")
        print("-"*ll, end="")
    print(" ")

    for k,l in d.items():
        for i in l:
            pl=0
            if len(i)<lm[l.index(i)]:
                pl=lm[l.index(i)]-len(i)
            ps=" " * (pl+1)
            print("|", end=" ")
            print(i, end=ps)
        print("|")
        for i in l:
            ll=lm[l.index(i)]+2
            print(" ", end="")
            print("-"*ll, end="")
        print(" ")

box(x)