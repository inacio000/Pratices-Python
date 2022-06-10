from cabecalho import cabecalho


class CorrentAcouny:

    def __init__(self, account_number: int, name: str, balance: float):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def change_name(self, new_name):
        self.name = new_name

    def deposit(self, how_much):
        self.balance += how_much

    def withdrawal(self, money_to_withdrawal):
        if self.balance >= money_to_withdrawal:
            self.balance -= money_to_withdrawal
        else:
            print('\033[31mInsufficient amount!\033[m')

    def show_datas(self):
        print(f'Older Account: {self.name} \nAccount Number: {self.account_number} \nBalance: {self.balance}')


account_older = CorrentAcouny(123456789, 'Inacio Raimundo', 10000)
account_older.show_datas()

cabecalho('NEW DATAS')
account_older.change_name('Inacio Martinho')
account_older.deposit(500)
account_older.show_datas()

cabecalho('NEW DATAS')
account_older.withdrawal(20000)
account_older.show_datas()
