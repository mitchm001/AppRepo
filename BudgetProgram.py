import sys

class Program():
    def __init__(self):
        self.income = 0
        self.income_name = []
        self.income_list = []
        self.expense = 0
        self.expense_name = []
        self.expense_list = []
        self.start_income()

        #asks for income
    def income_ask(self):
        add_income = input('Add source of income? [y/n]:')
        return add_income

        #sums income if multiple entries
    def income_sum(self):
        self.income = sum(self.income_list)

        #asks for expense
    def expense_ask(self):
        add_expense = input('Add an expense? [y/n]:')
        return add_expense

        #sumes expenses if multiple entries
    def expense_sum(self):
        self.expenses = sum(self.expense_list)

        #checking if user enters income
    def income_check(self):
        if not self.income_list:
            print('Please enter atleast one source of income. ')
            self.start_income()
        else:
            return

        #checking if user enters expense
    def expense_check(self):
        if not self.expense_list:
            print('Please enter atleast one expense. ')
            self.start_expense()
        else:
            return

        #start of program
    def start_income(self):
        x = False
        while not x:
            result = self.income_ask()
            if result == 'y':  #when user enters 'y' for income_ask
                income_input = int(input('Enter annual income amount $: [numbers only] '))
                self.income_list.append(income_input)
                income_name = input('Enter income name: ')
                self.income_name.append(income_name)
                #appending for multiple entures
            else:
                self.income_check()
                x = True
        #summing income(s)
        self.income_sum()
        name = [name for name in self.income_name]
        income = [income for income in self.income_list]
        income_dict = dict(zip(name, income))
        for t in income_dict:
            print(t + ': ', '$' + str(income_dict[t]))
            print('Total income: ', '$' + str(self.income))
            self.start_expense()

        #start expense part
    def start_expense(self):
        x = False
        while not x:
            result = self.expense_ask()
            if result == 'y':  #when user enters 'y' for expense_ask
                expense_input = int(input('Enter expense amount: [numbers only] '))
                self.expense_list.append(expense_input)
                expense_name = input('Enter expense name: ')
                self.expense_name.append(expense_name)
                #appending for multiple entries
            else:
                self.expense_check()
                x = True
            #summing expenses
            self.expense_sum()
            name = [name for name in self.expense_name]
            expense = [income for income in self.expense_list]
            expense_dict = dict(zip(name, expense))
            for k in expense_dict:
                print(k + ': ', '$' + str(expense_dict[k]))
                print('Total expenses: ', '$' + str(self.expenses))
                self.user_info()

        #displaying user statiscits based off input of income and expenses
    def user_info(self):
        value = self.income - self.expenses
        if value < 0:
            print('Watch your spending! You have a deficit of ' + '$' + str(value))
        if value == 0:
            print('You are breaking even.  You spend exactly as much as you make.')
        if value > 0:
            print('Good job! You have a surplus of ' + '$' + str(value))
        again = input('Would you like to run the program again? [y/n]: ')
        if again == 'y':
            self.reset_program()
        else:
            self.close_program()

    def reset_program(self):
        self.income = 0
        self.expenses = 0
        del self.expense_list[0:]
        del self.expense_name[0:]
        del self.income_name[0:]
        del self.income_list[0:]
        self.start_income()

    def close_program(self):
        print('Exiting...')
        sys.exit(0)

if __name__ == '__main__':
    Program()
