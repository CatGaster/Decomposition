import datetime
from aplication.people import get_employees
from aplication.db.salary import calculate_salary

dt = datetime.datetime.now()

if __name__ == "__main__":
    get_employees()
    calculate_salary()
    print(f' Сегодняшняя дата {dt}' )