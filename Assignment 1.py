# Time complexity: O(N^2)
# Space complexity: O(N)

class Student(object):
    def __init__(self, name, age, marks, rollNumber):
        self.name = name
        self.age = age
        self.marks = marks
        self.rollNumber = rollNumber
    name = ""
    age = 0
    marks = 0
    rollNumber = 0

    def get_dict(self):
        return {'name': self.name, 'age': self.age, 'marks': self.marks, 'rollNumber': self.rollNumber}


def studentSort(studen, keys):
    return sorted(students, key=lambda a: tuple(keys))


students = [Student("A", 5, 50, 3).get_dict(), Student("A", 5, 60, 3).get_dict(), Student(
    "A", 6, 50, 3).get_dict(), Student("B", 5, 50, 3).get_dict(), Student("A", 5, 50, 1).get_dict()]

print(studentSort(students, ['name', 'age']))
