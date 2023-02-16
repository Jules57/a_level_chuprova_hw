import datetime


class Employee:
    def __init__(self, name, daily_earnings):
        self.name = name
        self.daily_earnings = daily_earnings

    def __str__(self):
        return f'{self.name}, the Employee.'

    def work(self) -> str:
        return 'I come to office.'

    def calculate_salary(self, days: int = None) -> float:
        if days:
            return days * self.daily_earnings
        else:
            today = datetime.datetime.now()
            current_month = today.month
            current_year = today.year

            total_days = 0
            for i in range(1, today.day + 1):
                next_day = datetime.date(year=current_year, month=current_month, day=i)
                if next_day.isoweekday() in [1, 2, 3, 4, 5]:
                    total_days += 1
            return total_days * self.daily_earnings

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


class Recruiter(Employee):
    def work(self) -> str:
        return 'I come to office and start hiring.'

    def __str__(self):
        return f'{self.name}, the Recruiter.'


class Developer(Employee):
    def __init__(self, name, daily_earnings, tech_stack):
        super().__init__(name, daily_earnings)
        self.tech_stack = tech_stack

    def __str__(self):
        return f'{self.name}, the Developer.'

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __add__(self, other):
        name = self.name + ' ' + other.name
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        daily_earnings = max(self.daily_earnings, other.daily_earnings)
        dev_obj = Developer(name=name, daily_earnings=daily_earnings, tech_stack=tech_stack)
        return dev_obj

    def work(self) -> str:
        return 'I come to office and start coding.'


if __name__ == '__main__':

    jason = Employee(name='Jason',
                     daily_earnings=200)
    print(f'Employee: {jason.name}. \n'
          f'Employee daily earnings: {jason.daily_earnings} USD.')
    print(f'Employee object: {jason}')
    print(f'Employee says: {jason.work()}')
    print()

    david = Employee(name='David',
                     daily_earnings=175)
    print(f'Employee: {david.name}. \n'
          f'Employee daily earnings: {david.daily_earnings} USD.')
    print(f'Employee object: {david}\n')

    print(f'Who earns more? {david.name if david > jason else jason.name}.')
    print(f'Who earns less? {david.name if david < jason else jason.name}.\n')

    janette = Recruiter(name='Janette',
                        daily_earnings=50)
    print(f'Recruiter: {janette.name}. \n'
          f'Recruiter daily earnings: {janette.daily_earnings} USD.')
    print(f'Recruiter object: {janette}')
    print(f'Recruiter says: {janette.work()}')
    print(f'Janette\'s salary for 4 days is {janette.calculate_salary(4)} USD.\n')

    lindsey = Recruiter(name='Lindsey',
                        daily_earnings=45)
    print(f'Recruiter: {lindsey.name}.'
          f'Recruiter daily earnings: {lindsey.daily_earnings} USD.\n')
    print(f'Recruiter object: {lindsey}')
    print(f'Lindsey\'s salary for 14 days is {lindsey.calculate_salary(14)} USD.\n')
    
    print(f'Who earns more? {lindsey.name if lindsey > janette else janette.name}.')
    print(f'Who earns less? {lindsey.name if lindsey < janette else janette.name}.\n')

    thomas = Developer(name='Thomas',
                       daily_earnings=400,
                       tech_stack=['Python', 'SQL', 'Docker', 'git', 'HTML/CSS', 'Django'])
    print(f'Developer name: {thomas.name}.\n'
          f'Developer daily earnings: {thomas.daily_earnings} USD. \n'
          f'Developer tech stack: {", ".join(thomas.tech_stack)}.')
    print(f'Developer says: {thomas.work()}')
    print(f'Thomas\'s salary for this month is {thomas.calculate_salary()} USD.\n')

    william = Developer(name='William',
                        daily_earnings=500,
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
