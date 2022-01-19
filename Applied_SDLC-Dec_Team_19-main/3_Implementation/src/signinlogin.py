from src import workoutplan as w
from datetime import datetime

now = datetime.now()
def start():
    if now.hour >= 0 and now.hour < 12:
        w.printf("     Good Morning Welcome to our FFE MANAGEMENT")
        w.printf("         ..Always by your side..\n")
    elif now.hour >= 12 and now.hour <= 16:
        w.printf("     Good Afternoon Welcome to our FFE MANAGEMENT")
        w.printf("         ..Always by your side..\n")
    elif now.hour >= 17 and now.hour <= 19:
        w.printf("     Good Evening Welcome to our FFE MANAGEMENT")
        w.printf("         ..Always by your side..\n")
    else:
        w.printf("     Hope you had a Great Day Welcome to our FFE MANAGEMENT")
        w.printf("         ..Always by your side..\n")

def register():
    my_db = open("file.txt", "r")
    my_name = input("    Create Username:")
    my_new_password = input("    Create Password:")
    my_confirm_password = input("    Confirm Password:")
    U = []
    P = []
    for i in my_db:
        u, p = i.split(", ")
        p = p.strip()
        U.append(u)
        P.append(p)
    data = dict(zip(U, P))
    #w.printf(data)

    if my_new_password != my_confirm_password:
        w.printf("    Password dont match, Restart\n")
        register()
    else:
        if len(my_new_password) < 8:
            w.printf("    Password too short minimum length is 8, Restart\n")
            register()
        elif my_name in U:
            w.printf("    Sorry User already exist\n")
            register()
        else:
            my_db = open("file.txt", "a")
            my_db.write(my_name+", "+my_new_password+"\n")
            my_db.close()
            w.printf("    Success! "+ my_name +" Your Account has been created successfully")
            w.printf("    Now login to your account\n")
            home()
            
def access():
    my_db = open("file.txt", "r")
    my_name = input("   Username:")
    my_new_password = input("   Password:")

    if not len(my_name or my_new_password) < 1:
        U = []
        P = []
        for i in my_db:
            u, p = i.split(", ")
            p = p.strip()
            U.append(u)
            P.append(p)
        data = dict(zip(U, P))

        try:
            if data[my_name]:
                try:
                    if my_new_password == data[my_name]:
                        w.printf("    ..Login Success..\n")
                        w.printf("    Hi "+ my_name +" We are at your service")
                        
                        
                    else:
                        w.printf("    Password or Username is Incorrect\n")
                        home()
                except:
                    w.printf("    Incorrect Password or Username\n")
                    home()
            else:
                w.printf("    Username doesnt exist\n")
                home()
        except:
            w.printf("    Username doesn't exist Request you to create account\n")
            home()
    else:
        w.printf("    Please Enter a value\n")
        home()

def home(option=None):
    w.printf("        Enter required option")
    w.printf("        A.Signup")
    w.printf("        B.Login")
    option = input("        Option:")
    if option == 'A':
        register()
    elif option == 'B':
        access()
    else:
        w.printf("    Please enter proper option\n")
        home()

