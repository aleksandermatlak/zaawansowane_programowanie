from Classes.Book_Class import Book


class Order(Book):
    def __init__(self, employee, student,
                 books: Book, order_date):
        self.student = student
        self.employee = employee
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Wypożyczenia dokonał student {self.student}, ' \
               f'Wypożyczył: {self.employee} ' \
               f'. Wypożyczono dnia {self.order_date} książki: {self.books}.'
