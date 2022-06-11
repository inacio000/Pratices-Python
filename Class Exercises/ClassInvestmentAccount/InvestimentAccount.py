class Account:

    def __init__(self, account_number: int, name: str):
        self.account_number = account_number
        self.name = name
        self.balance = 0

    def change_name(self, new_name):
        self.name = new_name

    def deposit(self, amount):
        self.balance += amount

    def whithdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('\033[31mInsufficient amount!\033[m')

    def show_data(self):
        print(f'Account number: {self.account_number} \nOlder name: {self.name} \nBalance: {self.balance}')


class InvestmentAcount(Account):

    def __init__(self, account_number, name, balance, interest_rate):
        Account.__init__(self, account_number, name)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += (self.balance * self.interest_rate / 100)


savings = InvestmentAcount(123456789, 'Inacio', 1000, 10)
print(savings.balance)
savings.add_interest()
savings.add_interest()
savings.add_interest()
savings.add_interest()
savings.add_interest()
print(savings.balance)
