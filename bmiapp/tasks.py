import csv
import os
import pandas as pd
# classify and compute BMI
from bmi.settings import BASE_DIR

# defining method
def BMIcalculator():

    with open(os.path.join(BASE_DIR, "bmi_calculate_data.csv"), 'w') as csvfile:
        field_names = ['Gender', 'HeightCm', 'WeightKg', 'BMI', 'Category', "Health Risk"]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        df = pd.read_json(os.path.join(BASE_DIR, "data.json"))
        i = 0
        for b_data in df.itertuples():
            # compute BMI
            # height convert CM to M
            HeightCm = b_data[2] / 100  # height convert CM to M
            BMI = (b_data[3]) / (HeightCm * HeightCm)

            if BMI <= 18.4:
                gender = b_data[1]
                heightm = b_data[2] / 100
                weight = b_data[3]
                bmi_value = BMI
                category = "underweight"
                heelth_risk = "Malnutrition risk"

            elif BMI >= 18.5 and BMI < 24.9:
                gender = b_data[1]
                heightm = b_data[2] / 100
                weight = b_data[3]
                bmi_value = BMI
                category = "Normal weight"
                heelth_risk = "Low risk"

            elif BMI >= 25 and BMI < 29.9:
                gender = b_data[1]
                heightm = b_data[2] / 100
                weight = b_data[3]
                bmi_value = BMI
                category = "Overweight"
                heelth_risk = "Enhanced risk"
                i = i + 1

            elif BMI >= 30 and BMI < 34.9:

                gender = b_data[1]
                heightm = b_data[2] / 100
                weight = b_data[3]
                bmi_value = BMI
                category = "Moderately obese"
                heelth_risk = "Medium risk"

            elif BMI >= 35 and BMI < 39.9:
                gender = b_data[1]
                heightm = b_data[2] / 100
                weight = b_data[3]
                bmi_value = BMI
                category = "Severely obese"
                heelth_risk = "High risk"

            elif BMI >= 40:
                gender = b_data[1]
                heightm = b_data[2] / 100
                weight = b_data[3]
                bmi_value = BMI
                category = "Very severely obese"
                heelth_risk = "Very high risk"

            else:
                print("Your BMI is None")

            writer.writerow({'Gender':gender, 'HeightCm':heightm, 'WeightKg':weight, 'BMI':bmi_value, 'Category':category, "Health Risk":heelth_risk})

        print('Total no. of overweight person are :', i)
