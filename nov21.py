#fibbonacci sequence 
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
num=int(input("Enter the number of terms for Fibonacci sequence: "))
result = fibonacci(num)
print(f"Fibonacci sequence with {num} terms: {result}")
num=int(input("Enter the number of terms for Fibonacci sequence: "))
result = fibonacci(num)
print(f"Fibonacci sequence with {num} terms: {result}")
num=int(input("Enter the number of terms for Fibonacci sequence: "))
result = fibonacci(num)
print(f"Fibonacci sequence with {num} terms: {result}")
num=int(input("Enter the number of terms for Fibonacci sequence: "))
result = fibonacci(num)
print(f"Fibonacci sequence with {num} terms: {result}")
num=int(input("Enter the number of terms for Fibonacci sequence: "))
result = fibonacci(num)
print(f"Fibonacci sequence with {num} terms: {result}")
num=int(input("Enter the number of terms for Fibonacci sequence: "))
result = fibonacci(num) 