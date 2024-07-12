n_terms = 5

fibonacci_series = [0, 1]

for i in range(2, n_terms):
 
    next_term = fibonacci_series[-1] + fibonacci_series[-2]
  
    fibonacci_series.append(next_term)

print("Fibonacci Series:")
for term in fibonacci_series:
    print(term, end=" ")
