import csv
import datetime
import faulthandler
import traceback

from base_class_employee import Employee
from derived_class_developer import Developer
from derived_class_recruiter import Recruiter
from exceptions import EmailAlreadyExistsException


def main():
    def create_csv_with_headers(filename):
        with open(filename, 'w') as csv_file:
            fieldnames = ['emp_name', 'emp_email']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    create_csv_with_headers('employee_emails.csv')

    jason = Employee(
            name='Jason',
            daily_earnings=200,
            email='jason@gmail.com')
    print(f'Employee: {jason.name}. \n'
          f'Employee daily earnings: {jason.daily_earnings} USD.')
    print(f'Employee object: {jason}')
    print(f'Employee says: {jason.work()}\n')

    david = Employee(
            name='David',
            daily_earnings=175,
            email='david@gmail.com')
    print(f'Employee: {david.name}. \n'
          f'Employee daily earnings: {david.daily_earnings} USD.')
    print(f'Employee object: {david}\n')

    print(f'Who earns more? {david.name if david > jason else jason.name}.')
    print(f'Who earns less? {david.name if david < jason else jason.name}.\n')

    janette = Recruiter(
            name='Janette',
            daily_earnings=50,
            email='janette@gmail.com')
    print(f'Recruiter: {janette.name}. \n'
          f'Recruiter daily earnings: {janette.daily_earnings} USD.')
    print(f'Recruiter object: {janette}')
    print(f'Recruiter says: {janette.work()}')
    print(f'Janette\'s salary for 4 days is {janette.calculate_salary(4)} USD.\n')

    lindsey = Recruiter(
            name='Lindsey',
            daily_earnings=45,
            email='lindsey@gmail.com')
    print(f'Recruiter: {lindsey.name}.\n'
          f'Recruiter daily earnings: {lindsey.daily_earnings} USD.\n')
    print(f'Recruiter object: {lindsey}')
    print(f'Lindsey\'s salary for 14 days is {lindsey.calculate_salary(14)} USD.\n')

    print(f'Who earns more? {lindsey.name if lindsey > janette else janette.name}.')
    print(f'Who earns less? {lindsey.name if lindsey < janette else janette.name}.\n')

    thomas = Developer(
            name='Thomas',
            daily_earnings=400,
            email='william@gmail.com',
            tech_stack=['Python', 'SQL', 'Docker', 'git', 'HTML/CSS', 'Django'])

    print(f'Developer name: {thomas.name}.\n'
          f'Developer daily earnings: {thomas.daily_earnings} USD. \n'
          f'Developer tech stack: {", ".join(thomas.tech_stack)}.')
    print(f'Developer says: {thomas.work()}')
    print(f'Thomas\'s salary for this month is {thomas.calculate_salary()} USD.\n')

    william = Developer(
            name='William',
            daily_earnings=500,
            email='william@gmail.com',
            tech_stack=['JavaScript', 'Angular', 'SQL', 'HTML/CSS'])

    print(f'Developer name: {william.name}.\n'
          f'Developer daily earnings: {william.daily_earnings} USD. \n'
          f'Developer tech stack: {", ".join(william.tech_stack)}.')
    print(f'William\'s salary for this month is {william.calculate_salary()} USD.\n')

    print(f'Who is more experienced? {thomas.name if thomas > william else william.name}.')
    print(f'Who needs to improve his professional skills? {thomas.name if thomas <= william else william.name}.')
    print(f'Do our developers have the same competence? {"Yes" if thomas == william else "No"}.\n')

    print(f'What if we could combine Thomas and William? \n{thomas + william}\n')

    print(f'Does Janette earn more than William? {"Yes" if janette > william else "No"}.')


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException as exc:
        tb = traceback.format_exc()
        with open('log.txt', 'a') as outfile:
            outfile.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {tb}\n')
    else:
        print('Great! No errors!')
    finally:
        print('You did your best. Better luck next time.')
