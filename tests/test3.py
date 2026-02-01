def box(l):
    for i in l:
        ll=len(i)+2
        print(" ", end="")
        print("-"*ll, end="")
    print(" ")
    for i in l:
        print("|", end=" ")
        print(i, end=" ")
    print("|")
    for i in l:
        ll=len(i)+2
        print(" ", end="")
        print("-"*ll, end="")
    print(" ")
box(['id', 'name', 'age'])