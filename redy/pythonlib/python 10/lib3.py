class Employee:
    def __init__(self, name, salary, hours_worked, days_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked
        self.days_worked = days_worked

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, discount_card):
        self.name = name
        self.discount_card = discount_card

class Business:
    def __init__(self, employees, products):
        self.employees = employees
        self.products = products

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)