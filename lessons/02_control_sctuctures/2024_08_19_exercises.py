# Czy dwie liczby są względnie pierwsze - mają conajmniej dwa dzielniki '1' + coś innego

# a, b = 14, 2
#
# for i in range(2, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         print("dzielnik: ", i)

# zrób choinkę i pozwól wpisać ile wierszy ma miec ta choinka

'''
  *
 ***
*****
'''

# rows = int(input("Liczba wierszy:"))
# for i in range(rows):
#     print(" " * (rows - 1 - i), end="")
#     print("*" * (i * 2 + 1))

# wygeneruj 100 wszych liczb z ciągu fibonaciego
fibonacci_sequence = [1, 1]
while len(fibonacci_sequence) < 100:
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

print(fibonacci_sequence)
