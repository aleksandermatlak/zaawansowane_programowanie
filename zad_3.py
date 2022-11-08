def is_even(x: int) -> bool:
    return x % 2 == 0


test3 = is_even(9)

if not test3:
    print('Liczba nieparzysta.')
else:
    print('Liczba parzysta.')
