from application.salary import def_class as dc
from application.db.people import employee
from datetime import date
if __name__ == '__main__':
    today = date.today()
    print("Date :", today)
    while True:
        command = input('Введите комманду: ')
        if command == '1':
            dc.def_1()
        if command == '2':
            dc.def_2()
        if command == '3':
            dc.def_3()
