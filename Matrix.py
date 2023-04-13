def matrix(a,b):
    a1,m1 = [],[]
    for i in range(a):
        print("Enter how many rows are there in "+chr(65+i)+" :")
        x1 = int(input())
        print("Enter how many columns are there in "+chr(65+i)+" :")
        x2 = int(input())
        a1 += [[x1,x2]]
    b2 = b == "+" or b == "-"
    if b2:
        if a1[0]==a1[1]:
            p = " "+b+" operation of the matricess is possible"
            # print(a1)

        else:
            p = " "+b+" operation of the matricess is not possible"
        
    else:
        if a1[0][1]==a1[1][0]:
            p = " "+b+" operation of the matricess is possible"
            # print(a1)
        else:
            p = " "+b+" operation of the matricess is not possible"
    return p

print("Enter matricess:")
a = int(input())
print("Enter the operating sign :")
b = input()
b1 = (b == "+") or (b == "-") or (b == "*")

if (1<a<3) and b1:
    x = matrix(a,b)
else:
    print("Wrong inputs")
print(x)
print("press enter to close.")
input()