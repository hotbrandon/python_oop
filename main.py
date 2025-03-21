from employee import Employee, Manager, Developer


john = Employee("John", "Doe", 50000)
jane = Employee("Jane", "Doe", 60000)

brandon = Developer("Brandon", "Smith", 70000, ["Python", "Java"])

mgr1 = Manager("Sue", "Smith", 90000)
mgr2 = Manager("David", "Smith", 90000)

mgr1.add_employee(john)
mgr1.print_employees()
mgr2.print_employees()
mgr1.add_employee(jane)
mgr1.remove_employee(john)
mgr1.print_employees()

print(repr(brandon))
print(str(brandon))
# or
# print(brandon.__repr__())
# print(brandon.__str__())
# print(help(Developer))

print(john + jane)

print(brandon.email)

# set email via setter
brandon.email = 'hotbrtandon@hotmail.com'
print(brandon.email)