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

def matrix_mult(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s += a[i][k] * b[k][j]
            row.append(s)
        result.append(row)
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def count_words(s):
    return len(s.split())

def most_frequent(lst):
    return max(set(lst), key=lst.count)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def sum_list(lst):
    return sum(lst)

def product_list(lst):
    prod = 1
    for x in lst:
        prod *= x
    return prod

def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

def to_uppercase(lst):
    return [s.upper() for s in lst]

def to_lowercase(lst):
    return [s.lower() for s in lst]

def squares_dict(n):
    return {x: x**2 for x in range(n)}

def cubes_dict(n):
    return {x: x**3 for x in range(n)}

def char_count(s):
    return {c: s.count(c) for c in set(s)}

def merge_lists(l1, l2):
    return l1 + l2

def zip_lists(l1, l2):
    return list(zip(l1, l2))

def filter_even(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd(lst):
    return [x for x in lst if x % 2 != 0]

def all_positive(lst):
    return all(x > 0 for x in lst)

def any_negative(lst):
    return any(x < 0 for x in lst)

def sum_matrix(matrix):
    return sum(sum(row) for row in matrix)

def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def reverse_list(lst):
    return lst[::-1]

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def count_occurrences(lst, val):
    return lst.count(val)

def find_indices(lst, val):
    return [i for i, x in enumerate(lst) if x == val]

def remove_value(lst, val):
    return [x for x in lst if x != val]

def replace_value(lst, old, new):
    return [new if x == old else x for x in lst]

def split_string(s, delim=' '):
    return s.split(delim)

def join_strings(lst, delim=' '):
    return delim.join(lst)

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def title_case(s):
    return s.title()

def is_substring(s, sub):
    return sub in s

def starts_with(s, prefix):
    return s.startswith(prefix)

def ends_with(s, suffix):
    return s.endswith(suffix)

def strip_string(s):
    return s.strip()

def left_strip(s):
    return s.lstrip()

def right_strip(s):
    return s.rstrip()

def repeat_string(s, n):
    return s * n

def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def unflatten_dict(d, sep='.'):
    result = {}
    for k, v in d.items():
        keys = k.split(sep)
        d2 = result
        for key in keys[:-1]:
            d2 = d2.setdefault(key, {})
        d2[keys[-1]] = v
    return result

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

def parse_int(s):
    try:
        return int(s)
    except ValueError:
        return None

def parse_float(s):
    try:
        return float(s)
    except ValueError:
        return None

def random_choice(lst):
    return random.choice(lst)

def random_sample(lst, k):
    return random.sample(lst, k)

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

def get_day_of_week(date_str):
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%A")

def days_between(d1, d2):
    dt1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    dt2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    
    return abs((dt2 - dt1).days)

def print_hello_world():
    print("Hello, World!")

def main():
    print(greet("User"))
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"Primes up to 20: {primes_up_to(20)}")
    print(f"Random list: {random_list(5)}")
    print(f"Current time: {current_time()}")

if __name__ == "__main__":
    main()