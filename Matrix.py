def matrix(a,b):
    a1,m1 = [],[]
    for i in range(a):
        print("Enter how many rows are there in "+chr(65+i)+" :")
        x1 = inp()
        print("Enter how many columns are there in "+chr(65+i)+" :")
        x2 = inp()
        a1 += [[int(x1),int(x2)]]
    b2 = (b == "+") or (b == "-")
    if b2:
        if (a1[0]==a1[1]):
            # p = " "+b+" operation of the matricess is possible"
            # print(a1)
            p = add_sub(a1,b)

        else:
            p = " "+b+" operation of the matricess is not possible"
        
    else:
        if (a1[0][1]==a1[1][0]):
            p = " "+b+" operation of the matricess is possible"
            # print(a1)
            # p = multi(a1,b)
        else:
            p = " "+b+" operation of the matricess is not possible"
    return p

def add_sub(a1,b):
    f1,m = [],0
    for i in a1:
        n,d1 = 0,[]
        for j in range(int(i[0])):
            c1 = []
            for k in range(int(i[1])):
                n += 1
                print("Enter the value of "+chr(65+m)+str(n))
                inp1 = inp()
                # c1 +=[float(inp1)]
                c1 +=[inp1]               
            d1 += [c1]
        f1 += [d1]
        m += 1
    return f1

def inp():
    condition = True
    while condition:
        numb_input = input()
        if numb_input.isdigit():
            return numb_input
            a = False
        else:
            print("Invalid input")
            print("Please enter your input again:")


print("Enter matricess:")
a = inp()
if a.isdigit():
    print("Enter the operating sign :")
    b = input()
    b1 = (b == "+") or (b == "-") or (b == "*")
    if (1<int(a)<3) and b1:
        a = int(a)
        x = matrix(a,b)
    else:
        print("Wrong inputs")
        
else:
    print("Wrong inputs")

print(x)
print("press enter to close.")
input()