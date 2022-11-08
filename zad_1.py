class Student:
    def __init__(self, name: str, marks: list):
        self.marks = marks
        self.name = name

    def is_passed(self) -> bool:
        avg = sum(self.marks)/len(self.marks)
        return avg > 50

