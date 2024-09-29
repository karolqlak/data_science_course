# 1. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# import math

# r = int(input("Radius: "))
# area = r ** 2 * 3.14
# print(f"Powierzchnia koła wynosi: {area}")


# 2. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java


# file_name = input("filename: ")
# result = file_name.split('.')
# result = '/'.join(result)
# print(result)

# 3.Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any
# after 100 in the sequence.

# lista = [1, 2, 3, 4, 5,6,7,8,9,10]
# numberList = list(range(250))
# count = 0
# for x in numberList:
#     if x % 2 == 0:
#         print(x)
#         count = count + 1
#         if count == 100:
#             break


# 4. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
# x1 = int(input("podaj x1: "))
# x2 = int(input("podaj x2: "))
# y1 = int(input("podaj y1: "))
# y2 = int(input("podaj y2: "))
#
# delta_x = abs(x2 - x1)
# delta_y = abs(y2 - y1)
#
# distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
# print(distance)


# 5. Create a script that checks whether user have a valid moto-bike license (yes/no).
# Use a condition with to check if the person is either above 18 years old or is younger and have a valid moto-bike
# license issued in Poland.
# Print a message that tells if they are eligible to drive.
# sample input:
#
#
#     # Case 1
#     age = 17
#     license = "yes"
#     country = "Poland"
#
#     # Case 2
#     age = 19
#     license = "no"
#     country = None
#
#     # Case 3
#     age = 16
#     license = "yes"
#     country = "Germany"

# def check_licence(age, licence, country):
#     if age >= 18 or (licence == "yes" and country == "Poland"):
#         print("Może jeździć")
#     else:
#         print("Nie wsiada za kółko")
#
#
# check_licence(17, "yes", "Poland")
# check_licence(19, "yes", None)
# check_licence(16, "yes", "Germany")


# //Create a script that calculates the area of intersecting rectangles. The script should take the coordinates of the
# bottom-left and top-right corners of two rectangles as input and output the area of the intersection. If the
# rectangles do not intersect, the script should output 0. Use the following coordinates for testing:
#
#
#     # Case 1
#     x1, y1, x2, y2 = 0, 0, 2, 2
#     x3, y3, x4, y4 = 1, 1, 3, 3
#
#     # Case 2
#     x1, y1, x2, y2 = 0, 0, 1, 1
#     x3, y3, x4, y4 = 2, 2, 3, 3
#
#     # Case 3
#     x1, y1, x2, y2 = 0, 0, 1, 1
#     x3, y3, x4, y4 = 1, 1, 2, 2
#
#     # Case 4
#     x1, y1, x2, y2 = 0, 0, 1, 1
#     x3, y3, x4, y4 = 1, 0, 2, 1

# def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
#     # Calculate the overlap in the x and y directions
#     overlap_x = max(0, min(x2, x4) - max(x1, x3))
#     overlap_y = max(0, min(y2, y4) - max(y1, y3))
#
#     # Calculate the area of the intersection
#     intersection = overlap_x * overlap_y
#
#     return intersection


# 7. Create a header variable from a several variables to this format:
#  [Name] [Surname]
#  [COUNTRY_CODE] ([ZIP_CODE]) [CITY]
#  [STREET] [STREET_NUMBER]
#
#
# where
# Name - first name eg. Jan
# Surname - last name eg. Kowalski
# COUNTRY_CODE - country code (first three letters) eg. POL
# ZIP_CODE - zip code eg. 00-001
# CITY - city name eg. Warsaw
# STREET - street name eg. Złota
# STREET_NUMBER - street number eg. 44
#
#    Sample input variables:
#
# name = "JAN"
# surname = "kowalski"
# country = "Poland"
# zip_code = "00001"
# city = "WARSAW"
# street = "ZŁOTA"
# street_number = 44
#
#
# def format_address(name, surname, country, zip_code, city, street, street_number):
#     return (f"{name.capitalize()} {surname.capitalize()}\n"
#             f"{country.upper()[:3]} ({zip_code[:2]}-{zip_code[2:]}) {city}\n"
#             f"{street} {street_number}")
#
#
# print(format_address(name, surname, country, zip_code, city, street, street_number))


# 8. Use string interpolation with %s, %d, and %f to create formatted strings and print them. For example, create a
# string that says "Name: John, Age: 25, Height: 155.8". Where age is an integer and height is a float with one decimal
# place. Sample input:
# name = "John"
# age = 25.500
# height = 175.82

# def format_personal_data(name, age, height):
#     return "name: %s, age: %d, height: %.1f" % (name, age, height)
#
#
# print(format_personal_data("John", 25.500, 175.82))


# 9. Create a script that checks if polish PESEL number is
# valid. PESEL is a
# national identification number used in Poland. It is a 11-digit number that contains information about the
# person's. Add case for good and wrong control number. TIP: do not use your ar your close friends PESEL number.
#
#    Sample input:
#
#     # Case 1 - valid
#     pesel = "44051401458"
#
#     # Case 2 - invalid month
#     pesel = "44131401458"
#
#     # Case 3 - invalid day
#     pesel = "44053201458"


def valid_pesel(pesel):
    pesel = str(pesel)
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    iloczyn = 0
    weight_map = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    for i in range(10):
        iloczyn = iloczyn + int(pesel[i]) * weight_map[i]
    modulo = iloczyn % 10
    return 10 - modulo == int(pesel[10])


print(valid_pesel(44051401458))
