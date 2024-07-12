def find_largest(num1, num2):
    
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

largest_number = find_largest(num1, num2)
print("The largest number between", num1, "and", num2, "is", largest_number)
