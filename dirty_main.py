from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    current_date = date.today()
    print(current_date)
    calculate_salary()
    get_employees()
    print('Программы выполнены')