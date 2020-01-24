a = int(input())

for i in range(1, a + 1):  # range is 1 to a a+1 doesn't count
    b = a % i
    if b == 0:
        print(i)
