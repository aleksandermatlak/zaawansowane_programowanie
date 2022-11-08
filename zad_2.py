# a
def names(firstnames):
    for x in firstnames:
        print(x)


imiona = ['Aleksander', 'Stansisław', 'Michał', 'Maciej', 'Czesław']

names(imiona)


# b
def multiplication(liczby):
    num = []
    for x in liczby:
        x = x * 2
        num.append(x)
    return num


def multiplication_comprehension(liczby):
    num = [x * 2 for x in liczby]
    return num


numbers = [4, 3, 6, 2, 12]

result = multiplication(numbers)
result2 = multiplication_comprehension(numbers)
print(result)
print(result2)


# c
def even_numbers(numbers):
    for x in range(10):
        if numbers[x] % 2 == 0:
            print(numbers[x])
        else:
            continue


numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers(numbers_2)


# d
def second_numbers(numbers):
    for x in range(0, 10, 2):
        print(numbers[x])


numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

second_numbers(numbers_2)
