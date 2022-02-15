class Employee(object):
    age = 36
    No_of_employees = 0
    hike = 1.75

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + '@gmail.com'
        self.random=dict()  # v0.1
        self.pay = pay
        Employee.No_of_employees += 1

    @classmethod
    def email(cls, email):
        return email, cls.age

    @staticmethod
    def isEligible() -> bool:
        return Employee.age > 18

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def raiseSalary(self):
        return int(self.hike * self.pay)


print('No of Employees -', Employee.No_of_employees)
emp1 = Employee('dhamoadaran', 'rajendran', 5_85_000)
emp2 = Employee('gundu', 'payyan', 8_90_000)
print('No of Employees -', Employee.No_of_employees)
emp1.age = 40
print(emp1.__dict__)  # namespace of emp1 instance
print(emp1.email)
print(emp2.fullname())
print(Employee.fullname(emp2))  # same as one above calling the method for instance emp2
print(Employee.email(emp2.email))  # calling class method
print(Employee.isEligible())  # calling static method
print(emp1.raiseSalary())