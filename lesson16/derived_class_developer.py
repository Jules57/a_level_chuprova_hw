from base_class_employee import Employee


class Developer(Employee):
    def __init__(self, name, daily_earnings, email, tech_stack):
        super().__init__(name, daily_earnings, email)
        self.tech_stack = tech_stack

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
        daily_earnings = max(self.daily_earnings, other.daily_earnings)
        email = self.email.split('@')[0] + other.email.split('@')[0] + '@' + self.email.split('@')[1]
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        return self.__class__(
                name=name,
                daily_earnings=daily_earnings,
                email=email,
                tech_stack=tech_stack)

    def work(self) -> str:
        return 'I come to office and start coding.'
