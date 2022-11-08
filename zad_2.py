class Student:
    def __init__(self, name: str, marks: list):
        self.marks = marks
        self.name = name

    def is_passed(self) -> bool:
        avg = sum(self.marks)/len(self.marks)
        return avg > 50

    def __str__(self):
        if self.is_passed() == False:
            return f'Student {self.name}, nie ma wysokiej średniej'
        else:
            return f'Student {self.name}, ma wysoką średnią.'


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka w {self.city} na ulicy {self.street}. ' \
               f'Jest otwarta w godzinach {self.open_hours}, tel. do biblioteki to: {self.phone}.'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street,
                 zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Pracownik {self.first_name} {self.last_name}.'


class Book(Library):
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.number_of_pages = number_of_pages
        self.author_surname = author_surname
        self.author_name = author_name
        self.publication_date = publication_date
        self.library = library

    def __str__(self):
        return f'Książka autorstwa {self.author_name} {self.author_surname}, wydana w {self.publication_date}.' \
               f'Posiada {self.number_of_pages} stron, znajduje sie w {self.library}.'


class Order(Book):
    def __init__(self, employee, student, books: list[Book], order_date):
        self.student = student
        self.employee = employee
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Wypożyczenia dokonał student {self.student}, Wypożyczył: {self.employee} ' \
               f'. Wypożyczono dnia {self.order_date} książki: {self.books}.'


lib_1 = Library('Katowice', 'Mariacka 10', '40-000','8-20',630330360)
lib_2 = Library('Katowice', 'Skargi 2', '40-000', '10-16', 550055505)
book_1 = Book(lib_1, '24-02-2004', 'Gracjan', 'Gorczyca', 450)
book_2 = Book(lib_2, '25-05-2000', 'Czesław', "Skowroński", 124)
book_3 = Book(lib_1, '24-02-2004', 'Gracjan', 'Gorczyca', 420)
book_4 = Book(lib_2, '25-05-2010', 'Czesław', "Skowroński", 154)
book_5 = Book(lib_2, '25-05-2008', 'Anna', "Skowrońska", 194)
employee_1 = Employee('Jacek', 'Pracowniczy', '25-06-2007', '24-04-1972', 'Katowice', 'Korfantego 2', '40-000', 34567890)
employee_2 = Employee('Jan', 'Pracuś', '21-02-2007', '22-09-1982', 'Katowice', 'Skargi 25', '40-000', 34557890)
employee_3 = Employee('Adam', 'Pracownik', '25-06-2009', '14-04-1978', 'Katowice', 'Śląska 2', '40-000', 37867890)
student_1 = Student("Marcin", [3, 4, 5, 6, 5, 5, 5, 3, 4, 2, 4])
student_2 = Student("Tomasz", [30, 90])
student_3 = Student('Maciej', [24, 25])
order_1 = Order(employee_1, student_2, [book_1.__str__(), book_2.__str__()], '12-09-2022')
order_2 = Order(employee_3, student_1, [book_4.__str__(), book_3.__str__()], '12-10-2022')
print(order_1)
print(order_2)
