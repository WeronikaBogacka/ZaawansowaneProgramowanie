# Zad 1 metoda student
import statistics


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        meanMarks = statistics.mean(self.marks)

        if meanMarks > 50:
            return True
        else:
            return False

    def __str__(self):
        return (
                f"Imię studenta: {self.name}. "
                f"Oceny: {self.marks}."
            )


student1 = Student(name="Maria", marks=[60, 70, 80])
student2 = Student(name="Max", marks=[20, 50, 70, 40, 20])

print(student1.is_passed())
print(student2.is_passed())
