"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру, например словарь.

Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
"""
from datetime import datetime

# define a couple of department to use them in the method for moving equipment from storage to these departments
departments_list = ['HR', 'Finance']

storage_equipment = []
hr_equipment = []
finance_equipment = []


class OwnError(Exception):
    def __init__(self, text):
        self.text = text


class Storage:

    @staticmethod
    def accepting_equipment(equipment_object):
        """accepts a new equipment unit to the storage, assigns the unit new keys: unit number and date of adding it to
        storage """
        if len(storage_equipment) == 0:
            # if this is a first unit, we need to assign 1st unit number
            equipment_object.__dict__.update({'unit_number': 1})
        else:
            # if it is not the first, we'll assign unit number +1 from the last unit number from the storage
            equipment_object.__dict__.update({'unit_number': storage_equipment[-1].get('unit_number') + 1})
        # and add a timestamp of adding it to storage
        equipment_object.__dict__.update({'accepting_to_storage_date:': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        storage_equipment.append(equipment_object.__dict__)
        print(f'Unit {equipment_object.equipment_type} {equipment_object.brand_name} {equipment_object.model_name} '
              f'successfully '
              f'added to storage')

    @staticmethod
    def moving_equipment_to_department():
        """Allows user to select equipment unit and performs a move of this unit to selected department"""
        print('*' * 40)
        print('Current list of equipment kept on storage: ')
        for equipment in storage_equipment:
            # cycle to show current list of equipment on the storage with shorten list of equipment attributes
            print(f'Index number: '
                  f'{equipment.get("unit_number")}) {equipment.get("equipment_type")}, {equipment.get("brand_name")}'
                  f' {equipment.get("model_name")}')
        user_equipment_selection_to_move = int(input('Type an index number of equipment unit to move to another '
                                                     'department: '))
        print('Departments list: ')
        for department in departments_list:
            print(department)

        while True:
            # check if department name is correct and if not - ask to type again
            try:
                user_department_selection = input(
                    'Type a target department name (where to move an equipment): ').lower()
                if user_department_selection == 'hr' or user_department_selection == 'finance':
                    break
                else:
                    raise OwnError('Incorrect department name!')
            except OwnError as error:
                print(error)
                continue

        for equipment in storage_equipment:
            # check if user selected unit number that matches the one logged on storage and if yes - move it to the
            # list of equipment of the selected department
            if equipment.get('unit_number') == user_equipment_selection_to_move:
                if user_department_selection == 'hr':
                    hr_equipment.append(storage_equipment.pop(storage_equipment.index(equipment)))
                    print(f'Successfully moved the unit to HR department. Current equipment list of HR department:\
                    n{hr_equipment}')
                elif user_department_selection == 'finance':
                    finance_equipment.append(storage_equipment.pop(storage_equipment.index(equipment)))
                    print(f'Successfully moved the unit to Finance department. Current equipment list of Finance '
                          f'department:\n{finance_equipment}')


class OfficeEquipment:
    def __init__(self, brand_name, model_name, price, equipment_type=None, quantity=1):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.equipment_type = equipment_type
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, printer_type, brand_name, model_name, price, equipment_type='Printer', quantity=1):
        self.printer_type = printer_type
        super().__init__(brand_name, model_name, price, equipment_type, quantity)


class Scanner(OfficeEquipment):
    def __init__(self, dots_per_inch, brand_name, model_name, price, equipment_type='Scanner', quantity=1):
        self.dots_per_inch = dots_per_inch
        super().__init__(brand_name, model_name, price, equipment_type, quantity)


class Copier(OfficeEquipment):
    def __init__(self, pages_per_minute, brand_name, model_name, price, equipment_type='Copier', quantity=1):
        self.pages_per_minute = pages_per_minute
        super().__init__(brand_name, model_name, price, equipment_type, quantity)


# let's add new object classes and add them to storage
printer_example = Printer('type', 'HP', 'H2070', 5500)
scanner_example = Scanner(350, 'Brother', 'AG-10', 1500)
copier_example = Copier(250, 'Xerox', 'T110', 4500)

Storage.accepting_equipment(printer_example)
Storage.accepting_equipment(scanner_example)
Storage.accepting_equipment(copier_example)

# checking current list of equipment
print('*' * 40)
print(f'Current list of equipment on storage:\n{storage_equipment}')

# test moving Class method
Storage.moving_equipment_to_department()
