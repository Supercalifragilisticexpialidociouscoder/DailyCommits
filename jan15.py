import math
import random
import datetime

# jan15.py
# 100 lines of Python code demonstrating various concepts


def greet(name):
    return f"Hello, {name}!"

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(n):
    return [x for x in range(2, n+1) if is_prime(x)]

def random_list(size, lower=0, upper=100):
    return [random.randint(lower, upper) for _ in range(size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

def unique_elements(lst):
    return list(set(lst))

def square_numbers(n):
    return [x**2 for x in range(n)]

def cube_numbers(n):
    return [x**3 for x in range(n)]

def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def palindrome(s):
    return s == s[::-1]

def merge_dicts(d1, d2):
    return {**d1, **d2}

def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))

def factorial_list(n):
    return [factorial(i) for i in range(n)]

def even_numbers(n):
    return [x for x in range(n) if x % 2 == 0]

def odd_numbers(n):
    return [x for x in range(n) if x % 2 != 0]

def flatten(lst):
    return [item for sublist in lst for item in sublist]

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def matrix_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

