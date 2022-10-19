
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
a = max(list_numbers)
for i in list_numbers:
    i=a
list_numbers[9], list_numbers[-1] = list_numbers[-1], list_numbers[9]

print(list_numbers)
