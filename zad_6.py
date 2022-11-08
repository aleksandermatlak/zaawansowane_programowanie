def list_duplicates(first_list: list, second_list: list) -> list:
    return [x ** 3 for x in list(set(first_list + second_list))]


test = list_duplicates([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
print(test)
