# fully functional table printing code. put empty string for empty cells.
# All values lists should have equal no. of elements.
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

'''z={'id':['name','subject','mark','test4'],'1':['ashin','maths','10',''], \
   '2':['anatte','science','20','345'],'3':['ponnu','history','30','4567']}
box(z)'''

'''D2={'id':['name','subject','mark','Out Of'],'1':['ashin','maths','10','10'], \
   '2':['anatte','science','20','20'],'3':['ponnu','social science','30','40'], \
     '4':['achu','English','35','60'],'5':['kichu','malayalam','25','50'],\
     '6':['pachu','Italian','105','100']}

box(D2)'''