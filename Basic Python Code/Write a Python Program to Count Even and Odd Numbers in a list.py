def count_even_odd(numbers):
    
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

numbers_list = [2, 1, 3, 9, 0, 2, 1, 1, 6]
even_count, odd_count = count_even_odd(numbers_list)

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
