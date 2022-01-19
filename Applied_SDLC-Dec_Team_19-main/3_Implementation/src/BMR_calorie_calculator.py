import databas as d
from src import workoutplan as w
def bmi_value():
    ##edit this part
    age = int(input(w.printf(('What is your age: '))))
    gender = input(w.printf(('What is your gender(male/female?): ')))
    weight = int(input(w.printf(('What is your weight: '))))
    height = int(input(w.printf(('What is your height in centimeter: '))))
    d.insert(height,weight)

    if gender == 'male':
        #Metric formula for men BMR = 66.47 + ( 13.75 × weight in kg ) + ( 5.003 × height in cm ) − ( 6.755 × age in years )
        c1 = 66.47
        hm = 5.003 * height
        wm = 13.75 * weight
        am = 6.76 * age
    elif gender == 'female':
        #Metric formula for women BMR = 655.1 + ( 9.563 × weight in kg ) + ( 1.85 × height in cm ) − ( 4.676 × age in years )
        c1 = 655.1
        hm = 1.85 * height
        wm = 9.563 * weight
        am = 4.7 * age

    bmi = weight/((height/100)**2)
    #BMR = 665 + (9.6 X 69) + (1.8 x 178) – (4.7 x 27)
    bmr_result = c1 + hm + wm - am

    activity_level = input(w.printf(('What is your activity level (none, light, moderate, heavy, or extreme): ')))
    if activity_level == 'none':
        activity_level = 1.2 * bmr_result
    elif activity_level == 'light':
        activity_level = 1.375 * bmr_result
    elif activity_level == 'moderate':
        activity_level = 1.55 * bmr_result
    elif activity_level == 'heavy':
        activity_level = 1.725 * bmr_result
    elif activity_level == 'extreme':
        activity_level = 1.9 * bmr_result

    goals = input(w.printf(('Do you want to lose, maintain, or gain weight: ')))
    if goals == 'lose':
        calories = activity_level - 500
    elif goals == 'maintain':
        calories = activity_level
    elif goals == 'gain':
        gain = int(input(w.printf(('Gain 1 or 2 pounds per week? Enter 1 or 2: '))))
        if gain == 1: 
            calories = activity_level + 500
        elif gain == 2:
            calories = activity_level + 1000
    w.printf('Your BMI is', bmi ,'in order to ', goals, 'weight, your daily caloric goals should be', int(calories), '!')
    #return (int(bmi))

#can remove this after integration

