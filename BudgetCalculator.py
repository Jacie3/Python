from tkinter import *
from tkinter import ttk

class BudgetForm:

    def __init__(self, master):

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text = "Monthly Budget Report").grid(row = 0, column = 0, padx = 5)

        self.frame_account = ttk.Frame(master)
        self.frame_account.pack()
        
        ttk.Label(self.frame_account, text = "Monthly Earnings:").grid(row = 0, column = 0, padx = 5)
        ttk.Label(self.frame_account, text = "Savings:").grid(row = 0, column = 1, padx = 5)
        ttk.Label(self.frame_account, text = "Credit:").grid(row = 0, column = 2, padx = 5)
        
        self.entry_earnings = ttk.Entry(self.frame_account, width = 20) 
        self.entry_savings = ttk.Entry(self.frame_account, width = 20) 
        self.entry_credit = ttk.Entry(self.frame_account, width = 20)

        self.entry_earnings.grid(row = 1, column = 0, padx = 5) 
        self.entry_savings.grid(row = 1, column = 1, padx = 5) 
        self.entry_credit.grid(row = 1, column = 2, padx = 5) 

        self.frame_expenses = ttk.Frame(master)
        self.frame_expenses.pack()
        
        ttk.Label(self.frame_expenses, text = "Expenses").grid(row = 0, column = 0, padx = 5)
        ttk.Label(self.frame_expenses, text = "Rent/Mortgage:").grid(row = 1, column = 0, padx = 5)
        ttk.Label(self.frame_expenses, text = "Grocery:").grid(row = 1, column = 1, padx = 5)
        ttk.Label(self.frame_expenses, text = "Car Payment:").grid(row = 1, column = 2, padx = 5)
        ttk.Label(self.frame_expenses, text = "Gas:").grid(row = 1, column = 3)
        ttk.Label(self.frame_expenses, text = "TV/Internet:").grid(row = 3, column = 0, padx = 5)
        ttk.Label(self.frame_expenses, text = "Utilities:").grid(row = 3, column = 1, padx = 5)
        ttk.Label(self.frame_expenses, text = "Insurance:").grid(row = 3, column = 2, padx = 5)

        self.entry_rent = ttk.Entry(self.frame_expenses, width = 20)
        self.entry_grocery = ttk.Entry(self.frame_expenses, width = 20)
        self.entry_car = ttk.Entry(self.frame_expenses, width = 20)
        self.entry_gas = ttk.Entry(self.frame_expenses, width = 20)
        self.entry_internet = ttk.Entry(self.frame_expenses, width = 20)
        self.entry_utilities = ttk.Entry(self.frame_expenses, width = 20)
        self.entry_insurance = ttk.Entry(self.frame_expenses, width = 20)

        self.entry_rent.grid(row = 2, column = 0, padx = 5)
        self.entry_grocery.grid(row = 2, column = 1, padx = 5)
        self.entry_car.grid(row = 2, column = 2, padx = 5)
        self.entry_gas.grid(row = 2, column = 3, padx = 5)
        self.entry_internet.grid(row = 4, column = 0, padx = 5)
        self.entry_utilities.grid(row = 4, column = 1, padx = 5)
        self.entry_insurance.grid(row = 4, column = 2, padx = 5)

        self.frame_save = ttk.Frame(master)
        self.frame_save.pack()
        
        ttk.Label(self.frame_save, text = "Save:").grid(row = 0, column = 0, padx = 5)
        ttk.Label(self.frame_save, text = "Invest:").grid(row = 0, column = 1, padx = 5)

        self.entry_save = ttk.Entry(self.frame_save, width = 20)
        self.entry_invest = ttk.Entry(self.frame_save, width = 20)

        self.entry_save.grid(row = 1, column = 0, padx = 5)
        self.entry_invest.grid(row = 1, column = 1, padx = 5)
        

        self.frame_leisure = ttk.Frame(master)
        self.frame_leisure.pack()
        
        ttk.Label(self.frame_leisure, text = "Money left for Leisure").grid(row = 0, column = 0, padx = 5)
        self.button_leisure = ttk.Button(self.frame_leisure, text = "Calculate", command = lambda : calculate(self))
        self.entry_leisure = ttk.Entry(self.frame_leisure, width = 20)

        self.entry_leisure.grid(row = 2, column = 0, padx = 5)
        self.button_leisure.grid(row = 1, column = 0, padx = 5)

        def calculate(self):
            
            earnings = Entry.get(self.entry_earnings)
            credit = Entry.get(self.entry_credit)

            rent = Entry.get(self.entry_rent)
            grocery = Entry.get(self.entry_grocery)
            car = Entry.get(self.entry_car)
            gas = Entry.get(self.entry_gas)
            internet = Entry.get(self.entry_internet)
            utilities = Entry.get(self.entry_utilities)
            insurance = Entry.get(self.entry_insurance)

            save = Entry.get(self.entry_save)
            invest = Entry.get(self.entry_invest)
            
            leftOver = (int(earnings)) - (int(credit) + int(rent) + int(grocery) + int(car) +int(gas) + int(internet) + int(utilities) + int(insurance) + int(save) + int(invest))

            self.entry_leisure.insert(0, leftOver)
            

if __name__ == "__main__": 
    root = Tk()
    budget = BudgetForm(root)
    root.mainloop()



