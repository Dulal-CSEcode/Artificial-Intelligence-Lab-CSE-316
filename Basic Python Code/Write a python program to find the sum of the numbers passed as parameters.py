def sum_of_numbers(*args):
   
    total = 0
    for num in args:
        total += num
    return total
result = sum_of_numbers(21, 39, 21, 16)
print("Sum of the numbers:", result)
