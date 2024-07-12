lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
print("Sum of elements in given list is :", sum(lst))
