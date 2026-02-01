def box(a,b):
    lena=len(a)+2
    lenb = len(b) + 2

    print(" ",end="")
    print("-" * lena,end="")
    print(" ", end="")
    print("-" * lenb,end="")
    print(" ")

    print("|",end=" ")
    print(a, end=" ")
    print("|", end=" ")
    print(b, end=" ")
    print("|")

    print(" ",end="")
    print("-" * lena,end="")
    print(" ", end="")
    print("-" * lenb,end="")
    print(" ")


box("Hello","World")