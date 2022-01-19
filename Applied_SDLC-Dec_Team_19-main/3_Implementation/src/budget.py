import os
from src import workoutplan as w

def start():
    
    budget = float(input(w.printf(('How much is your budget?\n'))))
    spending = budget * 0.5
    main(budget,spending)
    
def main(budget,spending):
    w.printf('This calculator uses 5:3:2 rule of spending by default.')
    w.printf('Your budget is')
    w.printf(budget)
    main_option = int(input(w.printf(('\nWhat do you want to do?\n1) View Budget Plan\n2) View Spending Budget\n3) Exit\n'))))
    if main_option == 1:
        budget_plan(budget,spending)
    elif main_option == 2:
        spending_budget(budget,spending)
    else:
        quit

def budget_plan(budget,spending):
    
    option = int(input(w.printf(('How much do you want to save?\n1) 20%\n2) 30%\n'))))
    if option == 1:
        saving = 0.2
    elif option == 2:
        saving = 0.3
    else:
        w.printf('Please select only 1 or 2')
    final_saving = budget * saving
    extra = budget-spending-(budget*saving)
    w.printf('\nSpending:')
    w.printf(spending)
    w.printf('\nTo Save: ')
    w.printf(final_saving)
    w.printf('\nExtra: ')
    w.printf(extra)
    w.printf("Thanks have a nice day")

def spending_budget(budget,spending):
    
    w.printf('Spending Budget')
    w.printf(spending)
    rent = float(input(w.printf(('\nHow much is your rent/mortgage?\n'))))
    bills = float(input(w.printf(('\nHow much are your monthly bills?\n'))))
    food = spending - rent - bills
    bal= budget-spending
    w.printf('\nEXPENSES:\nRent:')
    w.printf(rent)
    w.printf('\nBills')
    w.printf(bills)
    w.printf('\nFood')
    w.printf(food)
    w.printf('\nBalance')
    w.printf(bal)

    w.printf("Thanks have a nice day")
    
    
    


