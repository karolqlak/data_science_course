from dis import disco


def make_pizza(*toppings):
    for toppings in toppings:
        print(f" - {toppings}")


# toppings - args
make_pizza("salami", "ser", "tomato")


# keywords arguments
def build_profile(first, last, **user_info):
    profile = {"firs": first, "last": last}
    profile.update(user_info)
    print(profile)


build_profile("john", "Smith", age="35", location="Warsaw")


# default param values


def fun(name="John"):
    print("My name is:" + name)


fun()
fun("Karol")


def fun2():
    pass


def calculate_price(price, discount, tax=0.23):
    discounted_price = price * (1 - discount)
    tax_amount = discounted_price * tax
    full_price = discounted_price + tax_amount
    return discounted_price, tax_amount, full_price


# print(calculate_price(100, 5))
d, t, f = calculate_price(100, 5)
print(f)


# lambda
def add(a):
    return a + 10


print(add(5))
add = lambda a: a + 10
print(add(5))

print(type(add))

r = (lambda x: x ** 2 + x + 1)(1)
# wywołanie z bomby na jedynce
print(r)

r = (lambda a, b: a + b)(5, 5)


def fun(a):
    if a > 0:
        return lambda a: a ** .5
    else:
        return lambda a: a ** 2


f = fun(-1)


def chose_lambda(a, f1, f2):
    if a > 0:
        return f1(a)
    else:
        return f2(a)


r = chose_lambda(-2, lambda a: a ** 2, lambda b: b)
print(r)

# print((lambda *args: sum(args))(1, 2, 3))
# print((lambda **kwargs: sum(kwargs.valuse()))(one=1, two=2, three=3))

# 05_functions zaczynamy next time -> lambda funcionts with math filter reduce


items = [1, 2, 3, 4, 5]


def square(x):
    return x ** 2


squared_items = [square(x) for x in items]
squared_items = list(map(square, items))
squared_items = list(map(lambda a: a % 2, items))

# reduce function sum
from functools import reduce

reduced_list = reduce(lambda x, y: x + y, items)
print(reduced_list)

# suma kwadratów nieparzystych elementów listy
sum_elements = reduce(lambda x, y: x + y, map(lambda a: a ** 2, filter(lambda a: a % 2, items)))
print(sum_elements)

# walorus operator
items = [1, 2, 3, 4, 5]
process = lambda x: x ** 3 + x

processed_items = list(filter(lambda x: x >= 10, map(process, items)))
print(processed_items)

processed_items = [result for x in items if (result := process(x)) >= 10]
print(processed_items)

# benchmarking

from time import time

start = time()
items = range(1000)
n = 10
for i in range(n):
    list(filter(lambda x: x >= 10, map(process, items)))
print(time() - start)

start = time()
for i in range(n):
    [result for x in items if (result := process(x)) >= 10]
print(time() - start)
# ine sposoby na zrobienie tego samego

