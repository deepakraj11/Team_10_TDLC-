from src import workoutplan as w
from src import BMR_calorie_calculator as bmi
from src import menu as m 
from src import budget
from src import reminder as r
#import databas as d
from src import signinlogin as si
try:
    si.start()
    si.home()
    option=m.menu()
    if option==1:    
        bmi.bmi_value()
        w.assign()
    elif option==2:
        budget.start()
    elif option==3:
        r.reminder()
    else:
        w.printf("Thanks have a nice day")      
    
except:
    w.printf("Wrong input")

