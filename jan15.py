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

