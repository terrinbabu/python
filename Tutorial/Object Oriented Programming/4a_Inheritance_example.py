
class Employee:
    no_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        Employee.no_of_emp += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language


class Manager(Employee):
    raise_amount = 1.20

    def __init__(self, first, last, pay, subordinates=None):
        super().__init__(first, last, pay)
        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

    def add_subordinate(self, sub):
        if sub not in self.subordinates:
            self.subordinates.append(sub)

    def remove_subordinate(self, sub):
        if sub in self.subordinates:
            self.subordinates.remove(sub)

    def print_subs(self):
        i = 1
        for sub in self.subordinates:
            print(i, ': ', sub.fullname())
            i += 1


emp_1 = Employee('John', 'Schafer', 45000)
emp_2 = Employee('Testa', 'Usera', 30000)
dev_1 = Developer('Peter', 'Saint', 50000, 'python')
dev_2 = Developer('Bee', 'Yogi', 55000, 'C++')
mgr_1 = Manager('Sui', 'Ho', 65000, [emp_2, dev_1])

print('No of Employee : ', Employee.no_of_emp)
print('Employee raise : ', Employee.raise_amount)
print('Developer raise : ', Developer.raise_amount)
print('Manager raise : ', Manager.raise_amount)

print('Manager Name : ', mgr_1.fullname())
print('Manager\'s subordinates name list')
mgr_1.print_subs()

print('Adding a Developer ', dev_2.fullname(), ' to Manager')
mgr_1.add_subordinate(dev_2)

print('Manager\'s subordinates new name list')
mgr_1.print_subs()
