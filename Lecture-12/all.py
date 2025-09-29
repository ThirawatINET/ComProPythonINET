from functools import reduce
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_number = map(lambda x: x ** 2, number)
even_squared_numbrs = filter(lambda x: x % 2 == 0, number)
sum_of__even_squared_numbers = reduce(lambda x, y: x + y, even_squared_numbrs)
print(sum_of__even_squared_numbers)