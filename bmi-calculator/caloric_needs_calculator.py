#########################################################################################################################################
#                                                           CODE PSEUDOCODE                                                             #
# If any of the variables age_is_valid, sex_is_valid, height_is_valid, or weight_is_valid is False:                                     #
# a. An error message is printed to the console, indicating the invalid input.                                                          #
# b. The loop terminates.                                                                                                               #
#                                                                                                                                       #
# If physical_activity is not in valid_physical_activities:                                                                             #
# a. An error message is printed to the console, indicating the invalid input.                                                          #
# b. The loop terminates.                                                                                                               #
#                                                                                                                                       #                                                                                                                               #
# If all input variables are valid and prompts_finished is False:                                                                       #
# a. Prompts for age, sex, height, weight, and physical activity are displayed.                                                         #
# b. If any of the inputs for age, sex, height, weight, or physical activity are invalid:                                               #
# i. An error message is printed to the console, indicating the invalid input.                                                          #
# ii. The corresponding variable (age_is_valid, sex_is_valid, height_is_valid, weight_is_valid, or physical_activity) is set to False.  #
# c. If all inputs are valid:                                                                                                           #
# i. The variable prompts_finished is set to True.                                                                                      #
# ii. The function determine_weight_category is called with the calculated BMI to determine the weight category.                        #
# iii. The variables quantifier_string1 and quantifier_string2 are set based on the weight category.                                    #
# iv. The height is converted from inches to feet and inches.                                                                           #
# v. The variable report is formatted using the calculated BMI, weight category, age, sex, physical activity, and calculated calories.  #
# vi. The report is printed to the console.                                                                                             #
#                                                                                                                                       #
# The loop continues until either prompts_finished is True or any of the input variables are invalid.                                   #
#########################################################################################################################################

ACTIVITY_FACTORS =  {
"1": ["Sedentary", 1.2],
"2": ["Lightly Active", 1.375],
"3": ["Moderately Active", 1.55],
"4": ["Very Active", 1.725],
"5": ["Extra Active", 1.9]
}

# Define the function to calculate BMI
def calculate_bmi(weight_in_pounds, height_in_inches):
    weight_in_kilograms = eval(weight_in_pounds) * 0.454
    height_in_meters = eval(height_in_inches) / 39.37
    return weight_in_kilograms / height_in_meters ** 2

# Determine weight category
def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "healthy"
    elif bmi >= 25 and bmi < 30:
        return "overweight"
    else:
        return "obese"

# Calculate the number of calories
def calculate_calories(age, sex, weight_in_pounds, height_in_inches, activity):
    weight_in_kilograms = eval(weight_in_pounds) * 0.454
    height_in_centimeters = eval(height_in_inches) * 2.54

    if sex == "m":
        calories_required =  ((13.397 * weight_in_kilograms) + (4.799 * height_in_centimeters) - (5.677 * eval(age)) + 88.362) * (ACTIVITY_FACTORS.get(activity)[1])
    elif sex == "f":
        calories_required = ((9.247 * weight_in_kilograms) + (3.098 * height_in_centimeters) - (4.330 * eval(age)) + 447.593) * (ACTIVITY_FACTORS.get(activity)[1])

    return "{:.2f}".format(calories_required)


# Initialize age, sex, height, weight and physical_activity
age = "0"
sex = "m"
height = "72"
weight = "200"
physical_activity = "1"

# Define a function to identify whether a number is entered
def is_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

# A function to covert inches into feet
def inches_to_feet(length_inches):
    length_feet = eval(length_inches) / 12
    return length_feet

# Initialize valid inputs    
age_is_valid = int(age) >= 0
sex_is_valid = True
height_is_valid = is_number(height)
weight_is_valid = is_number(weight)
valid_physical_activities = ["1", "2", "3", "4", "5"]
prompts_finished = False

# Run a loop for validation, calculations and eventually generation of `reort`s
while age_is_valid and sex_is_valid and height_is_valid and weight_is_valid and physical_activity in valid_physical_activities and not prompts_finished:
    age = input("Enter your age in years:\n")
    if int(age) >= 0 and is_number(age):
        sex = input("""If you identify as non-binary or something other than male or female,
choose one of either "m" or "f" that you feel would be more accurate.
Enter your sex (m/f):\n""")
        if sex in ["m", "f"]:
            height_in_inches = input("Enter your height in inches:\n")
            if is_number(height_in_inches):
                weight_in_pounds = input("Enter your weight in pounds:\n")
                physical_activity = input("""Please select your physical activity on a weekly basis:
1. Sedentary (little or no exercise)
2. Lightly Active (light exercise/sports 1-3 days/week)
3. Moderately Active (moderate exercise/sports 3-5 days/week)
4. Very Active (hard exercise/sports 6-7 days/week)
5. Extra Active (very hard daily exercise/sports & physical job or 2X day training)\n""")
                if physical_activity in valid_physical_activities:
                    prompts_finished = True

                    if determine_weight_category(calculate_bmi(weight_in_pounds, height_in_inches)) == "underweight":
                        quantifier_string1 = "more than"
                        quantifier_string2 = "gain"
                    elif determine_weight_category(calculate_bmi(weight_in_pounds, height_in_inches)) == "overweight" or determine_weight_category(calculate_bmi(weight_in_pounds, height_in_inches)) == "obese":
                        quantifier_string1 = "less than"
                        quantifier_string2 = "lose"
                    else:
                        quantifier_string1 = "about"
                        quantifier_string2 = "maintain"
                    
                    height_in_feet = inches_to_feet(height_in_inches)
                    feet = int(height_in_feet)  # extract the integer part
                    inches = round((height_in_feet - feet) * 12)  # extract the decimal part and convert to inches
                    
                    report = f"""A {f"{feet}'{inches}"} {"male" if sex == "m" else "female"} weighing {weight_in_pounds} lbs would have a BMI of {"{:.2f}".format(round(calculate_bmi(weight_in_pounds, height_in_inches), 2))} \
which is considered {determine_weight_category(calculate_bmi(weight_in_pounds, height_in_inches))}.
At {age} years old and being {ACTIVITY_FACTORS.get(physical_activity)[0]}, you would require {quantifier_string1} {calculate_calories(age, sex, weight_in_pounds, height_in_inches, physical_activity)} \
calories in order to {quantifier_string2} weight."""
                    
                    print(report)

                else:
                    print("ERROR: Invalid physical activity.")
            else:
                weight_is_valid = False
                print("ERROR: Invalid weight")
        else:
            sex_is_valid = False
            print("ERROR: Invalid sex.")
    else:
        age_is_valid = False
        print("ERROR: Age cannot be less than zero.")
