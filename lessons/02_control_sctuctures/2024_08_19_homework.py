# Generate the first 10 prime numbers using a brute force algorithm.
import random


def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

print(generate_primes(10))


# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the
# number and for multiples of five print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".
# Sample Output:
#
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

# def fizz():
#     for i in range(1, 51):
#         if i % 15 == 0:
#             print("fizzbuzz")
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#         else:
#             print(i)
# fizz()


# Write a Python program to guess a number between 1 and 9. Note: User is prompted to enter a guess. If the user
# guesses wrong then the prompt appears again until the guess is correct. On successful guess, user will get a "Well guessed!"
# message, and the program will exit.

def guess_number():
    number_to_guess = random.randint(1, 9)
    while True:
        user_guess = int(input("Zgadnij numer między 1 a 9: "))
        if user_guess == number_to_guess:
            print("Well guessed!")
            break
        else:
            print("Try again!")

guess_number()

# Extract all information to separate variables from the following string: Name: John, Age: 25, Height: 155.8 use
# string methods: split() method and string interpolation.

data = "Name: John, Age: 25, Height: 155.8"

data_table = data.split(", ")
name = data_table[0].split(": ")[1]
age = int(data_table[1].split(": ")[1])
height = float(data_table[2].split(": ")[1])

print(name, age, height)
