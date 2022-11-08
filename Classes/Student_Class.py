class Student:
    def __init__(self, name: str, marks: list):
        self.marks = marks
        self.name = name

    def is_passed(self) -> bool:
        avg = sum(self.marks)/len(self.marks)
        return avg > 50

    def __str__(self):
        if not self.is_passed():
            return f'Student {self.name}, nie ma wysokiej średniej'
        else:
            return f'Student {self.name}, ma wysoką średnią.'
