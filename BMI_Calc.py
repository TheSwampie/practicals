import sys

try:
    measurement_unit = str(sys.argv[1])
    height = float(sys.argv[2])
    weight = float(sys.argv[3])

    if measurement_unit == "metric":
        bmi = weight / (height**2)
    elif measurement_unit == "imperial":
        bmi = 703 * weight / (height**2)

    if bmi < 16:
        status = "Severe Thinness"
    elif bmi >= 16 and bmi < 17:
        status = "Moderate Thinness"
    elif bmi >= 17 and bmi < 18.5:
        status = "Mild Thinness"
    elif bmi >= 18.5 and bmi < 25:
        status = "Normal"
    elif bmi >= 25 and bmi < 30:
        status = "Overweight"
    elif bmi >= 30 and bmi < 35:
        status = "Obese Class I"
    elif bmi >= 35 and bmi < 40:
        status = "Obese Class II"
    elif bmi > 40:
        status = "Obese Class III"

    print("%0.2f\t%0s"%(bmi,status))

except ValueError:
    print("Your input is invalid!")
except IndexError:
    print("Your input is invalid!")