def box(d):
    lk=[]
    ln = []
    maxlenl=0

    for k in d.keys():
        lk.append(len(k))

    for l in d.values():
        if maxlenl<len(l):
            maxlenl=len(l)
    for i in range(maxlenl):
        ln.append(0)
    for l in d.values():
        for i in range(maxlenl):
            if ln[i]<len(l[i]):
                ln[i]=len(l[i])

    lkm=max(lk)

    print(" ", end="")
    lkml=lkm+2
    print("-"*lkml, end="")
    for i in ln:
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
        lii=0
        for i in l:
            lii+=1
            pl=0
            if len(i)<ln[l.index(i)]:
                pl=ln[lii-1]-len(i)
            ps=" " * (pl+1)
            print("|", end=" ")
            print(i, end=ps)
        print("|")

        print(" ", end="")
        lkml = lkm + 2
        print("-" * lkml, end="")
        lii2=0
        for i in l:
            lii2 += 1
            ll=ln[lii2-1]+2
            print(" ", end="")
            print("-"*ll, end="")
        print(" ")



d=eval(input("Enter a dictioary: "))
print(box(d))
