from functools import reduce
number = [1, 2, 3, 4, 5]
sum_of_number = list(map(lambda x, y: x + y, number))
print(sum_of_number)