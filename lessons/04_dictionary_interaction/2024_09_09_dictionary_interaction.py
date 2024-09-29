d = {1: "a", 2: "b"}

for key, values in d.items():
    print(f"{key=} {values}")

for key in d.items():
    print(f"{key=}")

for value in d.items():
    print(f"{value=}")

s = "Hello"
for e in s:
    print(e)


# List comprehensions
l =[]
for i in range(5):
    if i % 2 ==0:
        l.append(i)

l = [i for i in range(5) if i % 2 ==0]
print(l)

d = {i: i ** 2 for i in range(5) if i % 2 ==0}

d = {v: k for k,b in d.items()}
print(d)