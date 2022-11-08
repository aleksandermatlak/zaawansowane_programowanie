from Classes.Library_Class import Library


class Book(Library):
    def __init__(self, library: Library, publication_date,
                 author_name, author_surname, number_of_pages):
        self.number_of_pages = number_of_pages
        self.author_surname = author_surname
        self.author_name = author_name
        self.publication_date = publication_date
        self.library = library

    def __str__(self):
        return f'Książka autorstwa {self.author_name} ' \
               f'{self.author_surname}, wydana w {self.publication_date}.' \
               f'Posiada {self.number_of_pages} stron, ' \
               f'znajduje sie w {self.library}.'
