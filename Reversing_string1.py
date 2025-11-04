g=list(input("enter your string:"))
k=""
while len(k)!=len(g):
    if len(g)!=0:
        k+=g.pop(-1)
    else:
        break
print(k)