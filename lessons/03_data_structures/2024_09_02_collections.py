# # Lists and Tuples
# from math import trunc
#
# list1 = [1, 2]
# list2 = [3, 4]
# # list1 = list1 + list2
# # list1.append(list2)
# # list1.extend(list2)
# list1.insert(10, 10)
# print(list1)
l3 = [1, 2, 1, 2, 3]
print(l3.pop(2))
#
# print(l3.index(3))
# print(l3.count(1))
# l3.sort(reverse=True)
# print(l3)
#
# # Unpacking with star operator
# l1 = [1, 2]
# a, b, c = l1
# print(a)
# print(b)
# print(c)
#
# l1 = [1, 2, 3, 4, 5, 6]
# a, *b, c = l1
# print(a)
# print(b)
# print(c)


# def sum_all(l):
#     print(sum(l))
#
# sum_all([1, 2, 3])
#
# def sum_all(*args):
#     print(sum(args))
#
# sum_all(1, 2, 3)

# sets
#
# s1 = {1,2,3}
# print(s1)
# s1.add(4)
# print(s1)


# Dictionary

d1 = {"a": 1, "b": 2}
print(d1)

d1 = dict(a=1, b=2)
print(d1)


# shallow copy, deep copy  kawałek kodu który demonstruje różnicę w kodzie (na przykładzie listy)