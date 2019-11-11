import numpy as np
import matplotlib.pyplot as plt

def divided_diff(i,j,X,Y):

    if flag[i][j]==1:
        return A[i][j]

    if i==j:
        flag[i][j] = 1
        A[i][j] = Y[i]
        return A[i][j]

    A[i][j] = (divided_diff(i+1,j,X,Y)-divided_diff(i,j-1,X,Y))/(X[j]-X[i])
    flag[i][j] = 1
    return A[i][j]

def newton(X,Y,n,inputx):

    outputy = 0

    for i in range(n):
        temp=divided_diff(0,i,X,Y)
        mul=1

        for j in range(i):
            mul *= (inputx-X[j])

        temp *= mul
        outputy += temp

    return outputy

def lagrange(X,F,n,x_input):

    ret = 0.0

    for i in range(n):
        result = F[i];

        for j in range(n):
            if i != j:
                x_i = X[i]
                x_j = X[j]
                result = result * ((x_input - x_j) / (x_i - x_j))

        ret += result

    return ret



file = open('data_lagrange1.txt','r')
data = file.readlines()
n = 0;
X = np.array([]);
Y = np.array([]);

for i in range(len(data)):
    if(i==0):
        n = int(data[i])
    else:
        row = data[i].split()
        X = np.append(X,float(row[0]))
        Y = np.append(Y,float(row[1]))

print(n,X,Y)

flag = np.zeros((n+2,n+2))
A = np.zeros((n+2,n+2))
x_input = np.linspace(-30,30,100)
y_output_lagrange = np.zeros(100)
y_output_newton = np.zeros(100)

for i in range(len(x_input)):
    y_output_lagrange[i] = lagrange(X,Y,n,x_input[i])

for i in range(len(x_input)):
    y_output_newton [i]= newton(X,Y,n,x_input[i])


x_input = x_input.reshape(-1,1)
y_output_lagrange = y_output_lagrange.reshape(-1,1)
y_output_newton = y_output_newton.reshape(-1,1)
#print(x_input.shape)
#print(y_output_newton.shape)

plt.plot(x_input, y_output_newton,color="y")
plt.plot(x_input,y_output_lagrange,color = "g")
plt.scatter(X,Y)
plt.xlim(-32,32)
plt.ylim(-10,10)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()
