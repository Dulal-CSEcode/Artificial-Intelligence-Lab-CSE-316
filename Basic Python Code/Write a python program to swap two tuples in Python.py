tuple1=tuple((11,22))

tuple2=tuple((99,88))


list1=list(tuple1)

list2=list(tuple2)


tuple1=tuple(list2)
tuple2=tuple(list1)


print('tuple 1 :',tuple1)
print('tuple 2 :',tuple2)