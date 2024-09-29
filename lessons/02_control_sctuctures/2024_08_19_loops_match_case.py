# i = 0
# while True:
#     i += 1
#     if i > 5:
#         break
# print(i)

# while True:
#     x = int(input("enter number"))
#     if x == 0:
#         break
#     elif x == 1:
#         continue
#     else:
#         pass

#
# for i in range(100, 110, 2):
#     print(i)

# for i, e in enumerate(["a", "b", "2"]):
#     print(i * e)
#     # print(type(e))
#     # print(e)
#
# names = ["Alice", "Bob", "Charlie"]
#
# # scores = [5, 4, 3]
# scores = list([5, 4, 3])
#
# for n, s in zip(names, scores):
#     print(f"score of {n} is: {s} ")
#
# names_reversed = list(reversed(names))
# print(names_reversed)
#
# sorted_scores = sorted(scores)
# print(sorted_scores)
#
# for i in range(5):
#     for j in range(i, 10):
#         if j % 2:
#             print("*" * j)
#     if i == 3:
#         break

while True:
    option = int(input("Chose option"))
    match option:
        case 1:
            print("Option one")
        case 2:
            print("Option two")
        case _:
            break
