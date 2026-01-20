def box(a,b):
    lena=len(a)+2
    lenb = len(b) + 2
    print("","-"*lena,"-"*lenb,"",sep=" ")
    print(f"| {a} | {b} |")
    print("","-"*lena,"-"*lenb,"",sep=" ")
box("Hello","World")


def box22(a,b):

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