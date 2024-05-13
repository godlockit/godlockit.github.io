import libsql
import lib3
import libdeskdata
def display_menu():
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Добавить продукт")
    print("4. Удалить продукт")
    print("5. Выйти")

def add_employee():
    name = input("Введите имя сотрудника: ")
    salary = float(input("Введите зарплату сотрудника: "))
    hours_worked = int(input("Введите количество отработанных часов: "))
    days_worked = int(input("Введите количество отработанных дней: "))
    employee = Employee(name, salary, hours_worked, days_worked)
    business.add_employee(employee)
    print("Сотрудник успешно добавлен.")

def remove_employee():
    name = input("Введите имя сотрудника для удаления: ")
    for employee in business.employees:
        if employee.name == name:
            business.remove_employee(employee)
            print("Сотрудник успешно удален.")
            return
    print("Сотрудник не найден.")

def add_product():
    name = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    product = Product(name, price)
    business.add_product(product)
    print("Продукт успешно добавлен.")

def remove_product():
    name = input("Введите название продукта для удаления: ")
    for product in business.products:
        if product.name == name:
            business.remove_product(product)
            print("Продукт успешно удален.")
            return
    print("Продукт не найден.")

business = Business([], [])

while True:
    display_menu()
    choice = input("Выберите пункт меню: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        remove_employee()
    elif choice == "3":
        add_product()
    elif choice == "4":
        remove_product()
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

