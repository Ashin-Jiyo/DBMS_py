#print both keys and values but only for 3 elements in values list
def box(d):
    l1=[]
    l2=[]
    l0=[]
    lk=[]
    for k,l in d.items():
        l0.append(len(l[0]))
        l1.append(len(l[1]))
        l2.append(len(l[2]))
        lk.append(len(k))
    l0m=max(l0)
    l1m=max(l1)
    l2m=max(l2)
    lkm=max(lk)
    lm=[l0m,l1m,l2m]

    print(" ", end="")
    lkml=lkm+2
    print("-"*lkml, end="")
    for i in lm:
        ll=i+2
        print(" ", end="")
        print("-"*ll, end="")
    print(" ")

    for k,l in d.items():
        plk=0
        if len(k)<lkm:
            plk=lkm-len(k)
        psk=" " * (plk+1)
        print("|", end=" ")
        print(k, end=psk)
        for i in l:
            pl=0
            if len(i)<lm[l.index(i)]:
                pl=lm[l.index(i)]-len(i)
            ps=" " * (pl+1)
            print("|", end=" ")
            print(i, end=ps)
        print("|")

        print(" ", end="")
        lkml = lkm + 2
        print("-" * lkml, end="")
        for i in l:
            ll=lm[l.index(i)]+2
            print(" ", end="")
            print("-"*ll, end="")
        print(" ")

x={'id':['name','subject','mark'],'1':['ashin','maths','10'],'2':['anatte','science','20']}
box(x)