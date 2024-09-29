import copy

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

shallow_copy = copy.copy(list)
deep_copy = copy.deepcopy(list)

list[0][0] = 'X'

print("Oryginalna lista:", list)
print("Płytka kopia:", shallow_copy)
print("Głęboka kopia:", deep_copy)


# deep copy i shallow copy w przypadku zawierania tych samych typu danych- zadziała tak samo
# jeśli mamy listę zagnieżdżoną lista w liście itp - będą kopiowane referencje do zagnieżdżonych obiektów 