import os

relative_path = "dir/file.txt"

absolute_path = os.path.abspath(relative_path)
print(f"relative path:  {relative_path}")
print(f"relative path:  {absolute_path}")

# file operations
# write
file = open(relative_path, "w")
file.write("hello world")
file.close()

# read
file = open(relative_path, "r")
content = file.read()
file.close()
print(content)

# append
file = open(relative_path, "a")
file.write("\nHello append")
file.close()

# # with statement
# with open(relative_path, "r") as file:
#     content = file.read()
#     print(content)
#
# with open(relative_path, "rb") as file:
#     content = file.read()
#     print(content)
#
# with open("dir/file.bin", "wb") as file:
#     file.write(b'Hello world')

with open("dir/file.csv", "r") as file:
    file.readline()
    for line in file.readlines():
        index, value1, value2 = (line.strip().split(";"))
        print(index, value1, value2)

# //start with file methods