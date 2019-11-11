import numpy as np


f1 = open("input.txt","r");
equ = f1.readlines();

a = np.array([]);
b = np.array([]);
cap = 0;
small = 0;

e = 0
p = 1
m = 1

for i in range(len(equ)):
    s = ""
    temp = np.array([])
    e = 0
    p = 1
    m = 0

    for j in range(len(equ[i])):
        if equ[i][j] == ' ':
            continue

        if (equ[i][j] >= 'A' and equ[i][j] <='Z') or (equ[i][j] >= 'a' and equ[i][j] <='z'):

            if s == "":
                num = 1
            else:
                num = float(s)
            if m == 1:
                num = (-1) * num

            temp = np.append(temp,num)
            s = ""
            p = 0
            m = 0
            if(equ[i][j] >= 'A' and equ[i][j] <='Z') : cap = 1
            if(equ[i][j] >= 'A' and equ[i][j] <='Z') and (equ[i][j+1] >= '0' and equ[i][j+1] <='9') :
                print("Given input is invalid. There can't be any integer following capital letter.")
                exit()
            if(equ[i][j] >= 'a' and equ[i][j] <='z') :
                if (not(equ[i][j+1] >= '0' and equ[i][j+1] <='9')) :
                    print("Given input is invalid. There should be an integer following small letter.")
                    exit()

                small = 1;
                j = j + 1
            continue

        if equ[i][j] == '=':
            e = 1
            s = ""
            continue

        if equ[i][j] == '+':
            p = 1
            s = ""
            continue

        if equ[i][j] == '-':
            p = 1
            m = 1
            continue

        if e == 1:
            s += equ[i][j]
            continue

        if p == 1:
            s += equ[i][j]

    num = float(s)
    if m == 1:
        num = (-1) * num
    b = np.append(b,num)
    a = np.append(a,temp)

if cap and small :
    print("Given input is invalid. There can't be mixing of both small and capital letter.")
    exit()

a = a.reshape(len(equ),-1)
b = b.reshape(-1,1)
print(a)
print(b)

A = np.array(a)
[m,n] = a.shape

for i in range(m-1):
    print("Step : " + str(i+1))
    pivot = A[i][i]

    if(pivot == 0):
        for k in range(i+1,m):
            if A[k][i] != 0:
                P = np.identity(m, dtype = float)
                P[[i, k]] = P[[k, i]]
                A = np.dot(P,A)
                b = np.dot(P,b)
                print("After permutaion : ")
                print(A)
                print("\n")

    for j in range(i+1 , m):
        multiplier = -( A[j][i]/pivot)
        E = np.identity(m, dtype = float)
        E[j][i] = multiplier
        print("Elimination Matrix : ")
        print(E)
        print("\n")
        A = np.dot(E,A)
        b = np.dot(E,b)
        print("After Elimination: ")
        print("A = ")
        print(A)
        print("b = ")
        print(b)
        print("\n")

soln = np.zeros([m,1])
for i in range(m-1,-1,-1):

    soln[i] = b[i];

    for j in range(i+1,m):
        soln[i] -= A[i][j] * soln[j];

    soln[i] = soln[i] / A[i][i];

print(soln)

f2 = open("output.txt","w");
for i in range(len(soln)):
    if cap:
        f2.write( chr(i+65) + " = " + str(soln[i]) + "\n")
    else :
        f2.write("x" + str(i+1) + " = " + str(soln[i])  + "\n")
