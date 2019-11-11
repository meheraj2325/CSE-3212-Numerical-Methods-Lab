"""
r - read mode
w - write mode
a - append mode
r+ - read and write mode
"""

f = open("eqn.txt", "r")

# print(f.readline()) # read a line from the file and moves the cursor to the next
# print(f.readline())
# print("%%*****%%")

# print(f.read()) # read all the contents of the file from the position of the current cursor

# print("%%*****%%")

# f.close()

f = open("eqn.txt", "r")

array = f.readlines()
# print(array) # it stores all the lines of a file in an array

space = ' '
a = [[[0 for k in range(100)] for j in range(100)] for i in range(100)]
x = [0 for k in range(100)]
b = [[0 for k in range(100)] for j in range(100)]
r = 0
c = 0
for i in range(len(array)):
    eqn = array[i]
    word = eqn.split()

    for j in range(len(word)):
        if word[j] == '=':
            b[0][i] = int(word[j + 1]);
            print('b=' + str(b[0][i]))
            break
        else:
            num = word[j][0:len(word[j]) - 2]
            if (len(num) <= 1):
                if num == '+':
                    a[0][i][j] = 1
                elif num == '-':
                    a[0][i][j] = -1
                else:
                    a[0][i][j] = 1
            else:
                if num[0] == '+':
                    a[0][i][j] = int(num[1:len(num)])
                elif num[0] == '-':
                    a[0][i][j] = -1 * int(num[1:len(num)])
                else:
                    a[0][i][j] = int(num[1:len(num)])
            print(a[0][i][j])
            r = i + 1
            c = j + 1

f.close()

print('r=',end=" ")
print(r)

for k in range(r):
    a[k] = a[0]

for k in range(r - 1):
    ind = k
    mx = a[k][k][k]
    for i in range(k + 1, r):
        if (a[k][i][k] > mx):
            mx = a[k][i][k]
            ind = i

    temp = a[k][ind]
    a[k][ind] = a[k][k]
    a[k][k] = temp

    for i in range(r):
        for j in range(c):
            print('(' + str(i) + ',' + str(j) + ')=' + str(a[k][i][j]), end=" ")
        print()

    print('dividor=' + str(a[k][k][k]))

    for i in range(k + 1, r):
        for j in range(k, c):
            if a[k][k][k] == 0:
                print('found 0')
            else:
                print(a[k][k][k], end=" ")
                # a[k + 1][i][j] = a[k][i][j] - a[k][i][j] * a[k][k][j] / a[k][k][k]
                a[k + 1][i][j] = a[k][i][j] - a[k][k][j] * a[k][i][k] / a[k][k][k]
                print('k+1=' + str(k+1) + 'i=' + str(i) + 'j=' + str(j) + ' ' + str(a[k + 1][i][j]))
                print()
        print()

    print('k=' + str(k))

    for i in range(r):
        for j in range(c):
            print(a[k + 1][i][j], end=" ")
        print()




# f = open("Friends.txt","a")
# f.write("\n08 - Ayman Rasheed")
# f.close()
