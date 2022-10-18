def is_even(x: int) -> bool:
    return x % 2 == 0


test3 = is_even(9)

if test3 == False:
    print('Liczba nieparzysta.')
else:
    print('Liczba parzysta.')
