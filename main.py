from Classes.Library_Class import Library
from Classes.Order_Class import Order
from Classes.Book_Class import Book
from Classes.Employee_Class import Employee
from Classes.Student_Class import Student

lib_1 = Library('Katowice', 'Mariacka 10', '40-000', '8-20', 630330360)
lib_2 = Library('Katowice', 'Skargi 2', '40-000', '10-16', 550055505)
book_1 = Book(lib_1, '24-02-2004', 'Gracjan', 'Gorczyca', 450)
book_2 = Book(lib_2, '25-05-2000', 'Czesław', "Skowroński", 124)
book_3 = Book(lib_1, '24-02-2004', 'Gracjan', 'Gorczyca', 420)
book_4 = Book(lib_2, '25-05-2010', 'Czesław', "Skowroński", 154)
book_5 = Book(lib_2, '25-05-2008', 'Anna', "Skowrońska", 194)
employee_1 = Employee('Jacek', 'Pracowniczy', '25-06-2007',
                      '24-04-1972', 'Katowice',
                      'Korfantego 2', '40-000', 34567890)
employee_2 = Employee('Jan', 'Pracuś', '21-02-2007',
                      '22-09-1982', 'Katowice',
                      'Skargi 25', '40-000', 34557890)
employee_3 = Employee('Adam', 'Pracownik', '25-06-2009',
                      '14-04-1978', 'Katowice',
                      'Śląska 2', '40-000', 37867890)
student_1 = Student("Marcin", [3, 4, 5, 6, 5, 5, 5, 3, 4, 2, 4])
student_2 = Student("Tomasz", [30, 90])
student_3 = Student('Maciej', [24, 25])
order_1 = Order(employee_1, student_2,
                [book_1.__str__(), book_2.__str__()],
                '12-09-2022')
order_2 = Order(employee_3, student_1,
                [book_4.__str__(), book_3.__str__()],
                '12-10-2022')
print(order_1)
print(order_2)