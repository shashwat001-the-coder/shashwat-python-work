one= int(input("How Many Row You Want To Print:"))
two = int(input("Type 1 Or 0(1-->Ascending order and 0-->Descending order) :"))
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()