a = 100
print(a)

print(type(a))

a = 100 / 3
print(a)

print(type(a))

a = "abc"
print(a)

print(type(a))

ala = "ala ma kota"
# ala = int(ala)
# ValueError błąd rzutowania TODO

ala = 10
ala = str(ala)
print(ala)
# ze stringa na int dizała prawidłowo

word = "ala "


# - Arithmetic Operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
# - Comparison Operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
# - Logical Operators: `and`, `or`, `not`
# - Assignment Operators: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `//=`, `**=`

print(5 % 2)
print(5 // 2)
print(5 ** 2)

a = True
b = False

xor = (a or b) and not (a and b)

a = "ala ma kota"
print(a)
print(a[0])
print(a[-2])
print(a[1:5])

b = "123456789"
# od pierwszego do 9 znaku co drugi
print(b[1:9:2])

print(b[-1:-5:-1])
print(b[-2:])
print(b[1:2])

a = "ala ma kota"
print(a.upper())
print(a.title())
print(a.lower())

# //konkatenacje stringów

s = "name: %s, age: %d, height: %.1f" % ("john", 25, 180.67)
print(s)

s = "name: %s, age: %d, height: %.1f"
s = s % ("john", 25, 180.67)
print(s)

s = "name: {}, age: {}, height: {}".format("Jogn", 25, 180.999)
print(s)

name = "John"
age = 24
s = f"name: {name}, age {age}"
print(s)


# //wczytanie zmiennej z pamięci
s = f"{name= } {age= }"
print(s)
