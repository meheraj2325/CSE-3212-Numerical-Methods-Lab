import numpy as np
import matplotlib.pyplot as plt

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





file = open("data_lagrange1.txt","r");
data = file.readlines();

n = 0;
X = np.array([]);
F = np.array([]);

for i in range(len(data)):
    if(i==0):
        n = int(data[i])
    else:
        row = data[i].split()
        X = np.append(X,float(row[0]))
        F = np.append(F,float(row[1]))

#print(n)
#print(X)
#print(F)

x_input = np.linspace(-10,10,200)
y_output = np.zeros(200)

for i in range(len(x_input)):
    y_output[i] = lagrange(X,F,n,x_input[i])

x_input = x_input.reshape(-1,1)
y_output = y_output.reshape(-1,1)

plt.plot(x_input, y_output,color = "#0099cc")
plt.scatter(X,F)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
