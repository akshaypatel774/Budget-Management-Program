class Budget:
    def __init__(self, income=0.00, expense=0.00, quit=False):
        self.currency = self.get_currency()
        self.total_budget = self.get_budget()
        self.income_name = {}
        self.income = income
        self.expense_name = {}
        self.expense = expense
        self.quit = quit
        self.star_count = 58

    def __str__(self):
        return f"{'-'*self.star_count}\nBudget Amount is {self.currency} {self.total_budget:.2f}\n{'-'*self.star_count}"

    def start(self):
        while self.quit == False:
            try:
                self.give_options()
                choice = validate_input(input("Your choice here: "))

                if self.total_budget < 0:
                    print("Budget amount is negative. Please Update income/expense!!")

                if choice == "1":
                    self.add_income()
                elif choice == "2":
                    self.add_expense()
                elif choice == "3":
                    self.update_income()
                elif choice == "4":
                    self.update_expense()
                elif choice == "5":
                    self.delete_income()
                elif choice == "6":
                    self.delete_expense()
                elif choice == "7":
                    self.summary()
                elif choice == "8":
                    self.show_all_incomes_and_expenses()
                elif choice == "q":
                    self.exit()
                    break
            except ValueError as e:
                print(e)
            print(self)

        self.show_all_incomes_and_expenses()
        print(self)

    def give_options(self):
        print('*'*self.star_count)
        print("Press the corresponding numbers for the available actions.")
        print("1 - Add Income\n2 - Add Expense\n3 - Update Income\n4 - Update Expense\n5 - Delete Income\n6 - Delete Expense")
        print("7 - Get Summary\n8 - Show all Incomes and Expenses\nq - Exit")
        print('*'*self.star_count)

    def add_income(self):
        amount = self.get_amount()
        self.income+=amount
        name = self.get_name('income')
        self.income_name[name] = self.income_name.get(name, 0) + amount
        self.total_budget+=amount

    def add_expense(self):
        amount = self.get_amount()
        self.expense+=amount
        name = self.get_name('expense')
        self.expense_name[name] = self.expense_name.get(name, 0) + amount
        self.total_budget-=amount

    def update_income(self):
        name = input("Enter the income name to update: ")
        if name in self.income_name:
            old_amount = self.income_name[name]
            new_amount = self.get_amount()
            self.income -= old_amount
            self.income_name[name] = new_amount
            self.income += new_amount
            self.total_budget += new_amount - old_amount
        else:
            print("Income not found.")

    def update_expense(self):
        name = input("Enter the expense name to update: ")
        if name in self.expense_name:
            old_amount = self.expense_name[name]
            new_amount = self.get_amount()
            self.expense -= old_amount
            self.expense_name[name] = new_amount
            self.expense += new_amount
            self.total_budget -= new_amount - old_amount
        else:
            print("Expense not found.")

    def delete_income(self):
        name = input("Enter the income name to delete: ")
        if name in self.income_name:
            amount = self.income_name.pop(name)
            self.income -= amount
            self.total_budget -= amount
        else:
            print("Income not found.")

    def delete_expense(self):
        name = input("Enter the expense name to delete: ")
        if name in self.expense_name:
            amount = self.expense_name.pop(name)
            self.expense -= amount
            self.total_budget += amount
        else:
            print("Expense not found.")

    def summary(self):
        print(f"{'-'*25}Summary{'-'*26}")
        print(f"Total Income: {self.currency} {self.income:.2f}")
        print(f"Total Expense: {self.currency} {self.expense:.2f}")

    def show_all_incomes_and_expenses(self):

        print(f"{'-'*25}Incomes{'-'*26}")
        for name, amount in self.income_name.items():
            print(f"{name}: {self.currency} {amount:.2f}")
        print(f"Total Income: {self.currency} {self.income:.2f}")

        print(f"{'-'*25}Expenses{'-'*25}")
        for name, amount in self.expense_name.items():
            print(f"{name}: {self.currency} {amount:.2f}")
        print(f"Total Expense: {self.currency} {self.expense:.2f}")

        print(f"{'-'*self.star_count}")

    def exit(self):
        print("All the data will be lost. Are you sure you want to exit?")
        response = input("Y or N: \n")
        if response.lower() == 'y':
            self.quit = True
            print("\nYou have exited the program. Here's the summary...")

    def get_name(self, name):
        if name == 'income':
            name = input("Enter Income name: ")
        else:
            name = input("Enter Expense name: ")
        return name

    def get_currency(self):
        while True:
            print("\nPlease select from available currencies: \n1 : $ (Dollar)\n2 : £ (Pound)\n3 : € (Euro)\n4 : ₹ (Rupee)")
            currency = input("Select Currency: ")
            valid_currency = validate_currency(currency)
            if valid_currency is not None:
                return valid_currency

    def get_budget(self):
        while True:
            budget = input(f"Enter budget amount: {self.currency} ")
            valid_amount = validate_amount(budget)
            if valid_amount is not None:
                return valid_amount

    def get_amount(self):
        while True:
            amount = input(f"Enter Amount: {self.currency} ")
            valid_amount = validate_amount(amount)
            if valid_amount is not None:
                return valid_amount

def main():
    budget=Budget()
    print(budget)
    budget.start()

def validate_currency(currency):
    if currency == "1":
        return '$'
    elif currency == "2":
        return '£'
    elif currency == "3":
        return '€'
    elif currency == "4":
        return '₹'
    else:
        print('Invalid choice')

def validate_amount(amount):
    if amount.replace(".", "", 1).isdigit():
        return float(amount)
    else:
        print("Please enter a valid amount!")

def validate_input(choice):
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "q"]:
        return choice
    else:
        print("Please make a valid choice!")

if __name__ == "__main__":
    main()