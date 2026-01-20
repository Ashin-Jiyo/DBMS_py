def box2(a,b):
    lena=len(a)+2
    lenb = len(b) + 2
    print("","-"*lena,"-"*lenb,"",sep=" ")
    print(f"| {a} | {b} |")
    print("","-"*lena,"-"*lenb,"",sep=" ")

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


box2("Hello","World")