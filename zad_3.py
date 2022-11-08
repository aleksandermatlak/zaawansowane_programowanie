class Property:
    def __init__(self, area, rooms: int, price, address):
        self.price = price
        self.address = address
        self.rooms = rooms
        self.area = area

    def __str__(self):
        return f'Adres: {self.address}. Cena: {self.price}zł.' \
               f' Liczba pokoi:{self.rooms}. Osiedle: {self.area}'


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f' Wielkość działki:{self.plot}'


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f' Piętro: {self.floor}'


house = House('Zasole', 6, 1000000, 'Zasolska 12', 120000)
flat = Flat('Stare miasto', 4, 500000, 'Solska 2', 4)
print(house)
print(flat)
