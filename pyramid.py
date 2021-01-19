n = 0
mid = 8
for r in range(1, mid+1):
    for sp in range(1,(mid-r)+1):
        print(" ",end="")
    while n != (2*r-1):
        print("#",end="")
        n=n+1
    n = 0
    print("")
print("\n\nEXECUTED BY S.M.MD.MANSOOR_19X51A05B4")
