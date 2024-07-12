d = [2, 1, 3, 9, 0, 2, 1, 0, 6]
even_sum = 0
odd_sum = 0

for i in d:
    rem = i % 2
    if rem == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even sum =", even_sum)
print("Odd sum =", odd_sum)




