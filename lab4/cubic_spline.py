import numpy as np
import matplotlib.pyplot as plt

def calculate_h(x):
    h = np.zeros(len(x))
    for i in range(1,len(x)):
        h[i] = x[i] - x[i-1]
    return h

def create_matrix(h):
    mat = np.zeros([len(h)-2,len(h)-2])

    for i in range(len(h)-2):
        if i==0:
            mat[i][i] = 2*(h[i+1] + h[i+2])
            mat[i][i+1] = h[i+2]
        elif i==len(h)-3:
            mat[i][i-1] = h[len(h)-2]
            mat[i][i] = 2 * (h[len(h)-2] + h[len(h)-1])
        else:
            mat[i][i-1] = h[i+1]
            mat[i][i] = 2*(h[i+2] + h[i+1])
            mat[i][i+1] = h[i+2]

    return mat


def print_mat(mat):
    for i in range(mat.shape[0]):
        print(str(mat[i]))


def calculate_D(f,h):
    D = np.zeros(len(h)-2)
    for i in range(len(h)-2):
        D[i] = 6 * ( ((f[i+1] - f[i]) / h[i+2]) - ((f[i] - f[i-1]) / h[i+1]) )
    return D

def gauss(a,b):
    #a = a.reshape(len(equ),-1)
    b = b.reshape(-1,1)
    print(a)
    print(b)
    print(a.shape, b.shape)
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
    return soln

#x= np.array([-3,-2 ,-1, 0, 1, 2, 3])
x = np.array([0,1,2.5,3.6,5,7,8.1,10])
print(x)
print()

#f= np.array([-1, -1, -1, 0, 1, 1, 1])
f = np.array([0,.8,.6,-.44,-.96,.66,.97,-.54])
print(f)
print()

h = calculate_h(x)
print(h)
print()
mat = create_matrix(h)
print_mat(mat)
print()

D = calculate_D(f,h)
print(D)

a = gauss(mat,D)
print(a.shape)

T = np.array([0])
T = np.append(T,a)
T = np.append(T,0)

print(T)

for i in range(1,len(x)):
    func = lambda Z: ( (T[i-1]/(6*h[i])) * (((h[i] ** 2) * (Z - x[i])) - ((Z - x[i])**3)) ) + ( (T[i]/(6*h[i])) * (((Z - x[i-1])**3) - ((h[i] ** 2) * (Z - x[i-1]))) ) + ( (1/h[i]) * ( (f[i] * (Z - x[i-1])) - (f[i-1] * (Z - x[i])) ) )
    U = np.linspace(x[i-1],x[i])
    plt.plot(U,func(U))

plt.show()
