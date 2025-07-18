# instance variables are unique for each instance
# class variables are shared among all the instances of a class
class Employee:  # blueprint for creating instances

    raise_amount = 1.04

    def __init__(self, name, last, email, salary):  # constructor. self is used to refer to current the instance (self is conventional )
        self.name = name  # instance variables using self
        self.last = last
        self.email = email
        self.salary = salary

    def fullname(self):  # method. Instance always gets passed automatically
        return f"{self.name} {self.last}"

    def raise_pay(self):
        self.salary = int(self.salary * 1.04)


emp1 = Employee('Nandini', 'Gupta', 'nsg2001nsg@gmail.com', 1000000)


# without constructor
# emp2.first = 'Suraj'
# emp2.last = 'Gupta'
# emp2.email = 'ssg1991ssg@gmail.com'
# emp2.salary = 1000000

print(emp1.name)
print(emp1.fullname())
print(Employee.fullname(emp1))  # does the same thing
# print(emp2.first)
