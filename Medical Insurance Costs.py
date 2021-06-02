import pandas as pd
import numpy as np

#Separating all the data
data = pd.read_csv("insurance.csv")

ages = data["age"]
sexes = data["sex"]
bmis = data["bmi"]
num_children = data["children"]
smoker_statuses = data["smoker"]
regions = data["region"]
insurance_charges = data["charges"]

#Analyzing the data

class PatientInfo:
    def __init__(self, age, sex, bmi, num_children, smoker_status, region, insurance_charge):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_children = num_children
        self.smoker_status = smoker_status
        self.region = region
        self.insurance_charge = insurance_charge

    #Getting the average age
    def average_age(self):
        avg = np.mean(self.age)
        return avg

    #Getting sex count
    def sex_count(self):
        f = 0
        m = 0
        for sex in self.sex:
            if sex == "female":
                f += 1
            else:
                m += 1
        return(f"There are {f} females and {m} males")
    
    #Getting location count
    def loc_count(self):
        unique_r = []
        unique_count = {}
        for region in self.region:
            if region not in unique_r:
                unique_r.append(region)
        
        for unique in unique_r:
            counter = 0
            for region in self.region:
                if region == unique:
                    counter += 1
            unique_count[unique] = counter
        return unique_count

    #Getting average medical charges
    def medical_avg(self):
        avg = np.mean(self.insurance_charge)
        return(f"The average medical charge for the patients is {avg} dollars")

    #Getting smoker percentage
    def smoker_percentage(self):
        counter = 0
        length = 0
        for status in self.smoker_status:
            length += 1
            if status == "yes":
                counter += 1
        percentage = (counter/length)*100
        return(f"The percentage of smokers is {percentage}%")

    #Making a dictionary with the data
    def patient_dict(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.age]
        self.patients_dictionary["sex"] = self.sex
        self.patients_dictionary["bmi"] = self.bmi
        self.patients_dictionary["children"] = self.num_children
        self.patients_dictionary["smoker"] = self.smoker_status
        self.patients_dictionary["regions"] = self.region
        self.patients_dictionary["charges"] = self.insurance_charge
        return self.patients_dictionary

        