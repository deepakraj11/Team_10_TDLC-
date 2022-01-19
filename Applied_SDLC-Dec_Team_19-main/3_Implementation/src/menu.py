from src import workoutplan as w
def menu():
    try:
        w.printf("Choose Any")   
        w.printf ("[1] : FITNESS ")
        w.printf ("[2] : FINANCE ")
        w.printf ("[3] : EVENT CALENDER ")
        w.printf ("[4] : EXIT THE ASSISTANT ")
        a=int(input(w.printf("Enter -")))
        return a
    except:
        w.printf("wrong input")

def fitness_menu():
    w.printf("Choose Any")
    w.printf ("[1] : Exercise" )
    w.printf ("[2]: Calorie Track" )
    w.printf ("[3]: Go to main menu")
    a=int(input(w.printf("Enter -")))
    return a   
    
def finance_menu():
    w.printf ("[1]:Revenue")
    w.printf ("[2]: Expense")
    w.printf ("[3]: Summary")
    w.printf ("[4]: GO to Main Menu")

def event_calender_menu():
    w.printf ("[1]: Set Reminder")
    w.printf("[2]: Check Calender")
    w.printf ("{3]: Go to Main Menu")

      