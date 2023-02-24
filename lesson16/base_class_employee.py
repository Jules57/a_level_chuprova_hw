import csv
import datetime

from exceptions import EmailAlreadyExistsException


class Employee:
    def __init__(self, name, daily_earnings, email):
        self.name = name
        self.daily_earnings = daily_earnings
        self.email = email
        self.validate_email()
        self.save_email()

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __eq__(self, other):
        return self.daily_earnings == other.daily_earnings

    def __lt__(self, other):
        return self.daily_earnings < other.daily_earnings

    def __le__(self, other):
        return self.daily_earnings <= other.daily_earnings

    def __gt__(self, other):
        return self.daily_earnings > other.daily_earnings

    def __ge__(self, other):
        return self.daily_earnings >= other.daily_earnings

    def __ne__(self, other):
        return self.daily_earnings != other.daily_earnings

    def work(self) -> str:
        return 'I come to office.'

    def calculate_salary(self, days: int = None) -> float:
        if days:
            return days * self.daily_earnings
        else:
            today = datetime.datetime.now()
            total_days = 0
            for i in range(1, today.day + 1):
                next_day = datetime.date(year=today.year, month=today.month, day=i)
                if next_day.isoweekday() < 5:
                    total_days += 1
            return total_days * self.daily_earnings

    def save_email(self):
        with open('employee_emails.csv', 'a', newline='') as csv_file:
            fieldnames = ['emp_name', 'emp_email']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'emp_name': self.name, 'emp_email': self.email})

    def validate_email(self):
        with open('employee_emails.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if self.email in row:
                    raise EmailAlreadyExistsException
