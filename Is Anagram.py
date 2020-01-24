list1 = list(input())
list2 = list(input())

c = set(list1).difference(set(list2))
if len(c) == 0:
    print("Yes")
else:
    print("No")
