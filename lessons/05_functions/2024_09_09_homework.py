from functools import reduce


## 1Find the maximum of three numbers

# Write a Python function to find the maximum of three numbers.
# Sample Input: (3, 6, -5)
# Expected Output: 6

def max_of_three(a, b, c):
    return max(a, b, c)


# max_of_three = lambda a, b, c: a if a > b and a > c else b if b > c else c

print(max_of_three(3, 6, -5))


## 2. Sum all numbers in a list

# Write a Python function to sum all the numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20

def sum_list(lst):
    return sum(lst)


print(sum_list([8, 2, 3, 0, 7]))

# lambda
sum_list = lambda lst: reduce(lambda x, y: x + y, lst)

print(sum_list([8, 2, 3, 0, 7]))


## 3.Multiply all numbers in a list

# Write a Python function to multiply all the numbers in a list.
# Sample List: (8, 2, 3, -1, 7)
# Expected Output: -336

def multiply_list(lst):
    return reduce((lambda x, y: x * y), lst)


# multiply_list = lambda lst: eval('*'.join(map(str, lst)))

print(multiply_list([8, 2, 3, -1, 7]))


# 4.
## Reverse a string
# Write a Python program to reverse a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"

def reverse_string(s):
    return s[::-1]


# reverse_string = lambda s: ''.join(reversed(s))

print(reverse_string("1234abcd"))


# 5.
## Calculate factorial
#
# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number
# as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# factorial = lambda n: eval('*'.join(map(str, range(1, n + 1)))) if n > 0 else 1

print(factorial(5))


# 6
# Check if number is in range
#
# Write a Python function to check whether a number falls within a given range.
def is_in_range(n, start, end):
    return start <= n <= end


# is_in_range = lambda n, start, end: any([start <= n <= end])

print(is_in_range(5, 1, 10))


# 7
# Remove all occurrences of an element from a list
#
# Write a Python function rem() that returns a list with all occurrences of a given element removed.
# Sample List: [1, 1, 2, 1]
# Element to remove: 1
# Expected Output: [2]
def rem(lst, element):
    return [x for x in lst if x != element]


# rem = lambda lst, element: list(filter(lambda x: x != element, lst))

print(rem([1, 1, 2, 1], 1))


# 8
# Count upper and lower case letters
#
# Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String: 'The quick Brow Fox'
# Expected Output:
# No. of Upper case characters: 3
# No. of Lower case Characters: 12
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count


# count_upper_lower = lambda s: (
#     len([char for char in s if char.isupper()]),
#     len([char for char in s if char.islower()])
# )

upper, lower = count_upper_lower('The quick Brow Fox')
print(f"No. of Upper case characters: {upper}")
print(f"No. of Lower case characters: {lower}")


# 9
# Return distinct elements from a list
#
# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List: [1, 2, 3, 3, 3, 3, 4, 5]
# Unique List: [1, 2, 3, 4, 5]
def distinct_elements(lst):
    return list(set(lst))


# distinct_elements = lambda lst: list(dict.fromkeys(lst))

print(distinct_elements([1, 2, 3, 3, 3, 3, 4, 5]))


# 10
## Check if a number is prime

# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note: A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and
# itself.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

print(is_prime(7))
print(is_prime(10))


# 11
# Print even numbers from a list
#
# Write a Python program to print the even numbers from a given list.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
# even_numbers = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 12
# ## String interpolation
#
# Use string interpolation with %s, %d, and %f to create formatted strings and print them. For example, create a
# string that says "Name: John, Age: 25, Height: 155.8". Where age is an integer and height is a float with one decimal
# place.
name = "John"
age = 25
height = 155.8

print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))
formatted_string = lambda: f"Name: {name}, Age: {age}, Height: {height:.1f}"
print(formatted_string)



# 13
## Validate PESEL number

# Create a script that checks if a Polish PESEL number is
# valid. [PESEL](https://pl.wikipedia.org/wiki/PESEL#Cyfra_kontrolna_i_
def validate_pesel(pesel):
    if len(pesel) != 11:
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - checksum % 10) % 10

    return control_digit == int(pesel[10])


print(validate_pesel("44051401359"))
