import datetime
import time


from application.salary import calculate_salary
from application.db.people import get_employees

calculate_salary()
get_employees()


print("Начато выполнение if __name__ == '__main__'", "\n")
if __name__ == '__main__':
    calculate_salary()
    get_employees()
    
    DateCreation = datetime.datetime.today().strftime("%d-%m-%Y")
    TimeCreation = time.strftime("%H.%M.%S")

    print("Local Date: ", TimeCreation + " " + DateCreation, "\n")