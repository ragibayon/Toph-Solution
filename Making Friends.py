a = int(input())  # here the roll no of bayang will be N
f = 0
for i in range(1, a):  ##so he can make friends upto N-1
    b = a % i
    if b == 0:
        f = f + 1
print(f)
