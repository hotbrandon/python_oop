class Employee:
    raise_amt = 1.05

    def __init__(self, first_name, last_name, salary, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self._email = email

    # a 'getter' method
    @property    
    def email(self):
        return self._email
    
    @email.setter
    def email(self, mail):
        self._email = mail
        

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    # __repr__ is implicitly called when we call repr()
    # calling __str__ will fallback to __repr__ if __str__ is not available
    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', {self.salary})"
    
    # __str__ is implicitly called when we call str()
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, Salary: ${self.salary}"
    
    # define what happens when we add 2 employees together
    def __add__(self, other):
        return self.salary + other.salary
    
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first_name, last_name, salary, skills=None):
        super().__init__(first_name, last_name, salary)
        self.skills = skills or []  


# Using a mutable default argument like a list (employees=[]) in a function or method 
# definition is not recommended in Python. 
# This approach can lead to unexpected behavior because the default list is shared 
# across all instances of the class that use the default value.

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        self.employees = employees or []


    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        print('employee list:')
        for emp in self.employees:
            print('-->', emp.first_name)