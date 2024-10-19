# create a program that checks a students performance
marks=int(input("Enter Marks"))

if marks<=100 and marks>=80:
    print("You have an A")
elif 79>= marks >=60:

    print("you have a B")
elif marks<=59 and marks >=40:
    print("You have a C" )
elif marks<=39 and marks>=0:
    print("You have Failed")
else:
    print("inavalid marks")


    def calculate_bmi(weight, height):
        try:
            bmi = weight / (height ** 2)
            return round(bmi, 2)
        except ZeroDivisionError:
            return "Height must be greater than zero."


    # Input from user
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Validate inputs
        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
        else:
            # Calculate and display BMI
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi}")

            # Determine BMI category
            if isinstance(bmi, float):
                if bmi < 18.5:
                    print("Category: Underweight")
                elif 18.5 <= bmi < 24.9:
                    print("Category: Normal weight")
                elif 25 <= bmi < 29.9:
                    print("Category: Overweight")
                else:
                    print("Category: Obesity")
    except ValueError:
        print("Please enter valid numbers for weight and height.")