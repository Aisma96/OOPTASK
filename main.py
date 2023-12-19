class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def update_age(self, new_age):
        if 18 <= new_age <= 30:
            self.age = new_age
        else:
            print('Update is invalid')


student1 = Student('Jack Jackson', 20)
print(f'Student age: {student1.get_age()}')
student1.update_age(18)
print(f'Student age: {student1.get_age()}')
