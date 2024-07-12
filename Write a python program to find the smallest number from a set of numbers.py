
numbers = [2, 1, 3, 9, 0, 2, 1, 0, 6]

def find_smallest_number(numbers):
   
    if not numbers:
        return None
    
 
    smallest_number = min(numbers)
    

    for num in numbers:
        if num < smallest_number:
            smallest_number = num
    
    return smallest_number


smallest = find_smallest_number(numbers)
print("The smallest number is:", smallest)
