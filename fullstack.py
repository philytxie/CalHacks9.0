import tensorflow as tf
from tensorflow import keras
import numpy as np
from tkinter import*
from tkinter import ttk



from math import log10, floor
def round_sig(x, sig=3):
    return round(x, sig-int(floor(log10(abs(x))))-1)

print()
print()
print("Welcome!")
print()
print()


root = Tk()
root.geometry('1200x700')
root.title("HealthForward")

label_0 = Label(root, text="Input user data below.",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


name = Label(root, text="Full Name",width=20,font=("bold", 10))
name.place(x=80,y=130)
name_entry = Entry(root)
name_entry.place(x=240,y=130)
name_var = 0

age = Label(root, text="Age",width=20,font=("bold", 10))
age.place(x=68,y=160)
age_entry = Entry(root)
age_entry.place(x=240,y=160)
age_var = 0

height = Label(root, text="Height (in.)",width=20,font=("bold", 10))
height.place(x=68,y=190)
height_entry = Entry(root)
height_entry.place(x=240,y=190)
height_var = 0

weight = Label(root, text="Weight (lbs)",width=20,font=("bold", 10))
weight.place(x=68,y=220)
weight_entry = Entry(root)
weight_entry.place(x=240,y=220)
weight_var = 0

# bmi = 703 * (weight_entry / (height_entry ** 2))

race = Label(root, text="Race:\n(1) White\n(2) Black\n(3) Indigenous\n(4) Asian\n(5) Hawaiian/Pacific Islander\n(6) Other\n(7) Multiracial\n(8) Hispanic ",width=20,font=("bold", 10))
race.place(x=68,y=250)
race_entry = Entry(root)
race_entry.place(x=240,y=300)
race_var = 0

highBP = Label(root, text="Diagnosed high BP?\n(1) Yes\n(2) Yes, but only during pregnancy\n(3) No\n(4) Told borderline high or pre-hypertensive",width=30,font=("bold", 10))
highBP.place(x=38,y=370)
highBP_entry = Entry(root)
highBP_entry.place(x=240,y=390)
highBP_var = 0

medsBP = Label(root, text="Taking meds for high BP?\n(1) Yes\n(2) No",width=30,font=("bold", 10))
medsBP.place(x=38,y=450)
medsBP_entry = Entry(root)
medsBP_entry.place(x=240,y=450)
medsBP_var = 0

highChol = Label(root, text="Diagnosed high cholesterol?\n(1) Yes\n(2) No",width=30,font=("bold", 10))
highChol.place(x=38,y=500)
highChol_entry = Entry(root)
highChol_entry.place(x=240,y=500)
highChol_var = 0

# Column break

smoke100 = Label(root, text="Have you smoked over 100 \ncigarettes in your lifetime?\n(1) Yes\n(2) No",width=20,font=("bold", 10))
smoke100.place(x=580,y=130)
smoke100_entry = Entry(root)
smoke100_entry.place(x=740,y=140)
smoke100_var = 0

smokeFrequency = Label(root, text="Do you now smoke cigarettes \n(1) every day, (2) some days, \nor (3) not at all?",width=20,font=("bold", 10))
smokeFrequency.place(x=580,y=190)
smokeFrequency_entry = Entry(root)
smokeFrequency_entry.place(x=740,y=200)
smokeFrequency_var = 0

drinkFrequency = Label(root, text="Approximately how many times \nin the past 30 days did \nyou have 5 or more drinks?",width=22,font=("bold", 10))
drinkFrequency.place(x=580,y=240)
drinkFrequency_entry = Entry(root)
drinkFrequency_entry.place(x=740,y=250)
drinkFrequency_var = 0

physical = Label(root, text="Per week, do you engage in\n(1) 150+, (2) 1 - 149, or\n(3) 0 minutes of physical activity?",width=22,font=("bold", 10))
physical.place(x=580,y=300)
physical_entry = Entry(root)
physical_entry.place(x=740,y=310)
physical_var = 0

veggies = Label(root, text="How many servings of\nvegetables do you consume\nper day?",width=22,font=("bold", 10))
veggies.place(x=580,y=350)
veggies_entry = Entry(root)
veggies_entry.place(x=740,y=360)
veggies_var = 0

fruits = Label(root, text="How many servings of\nfruits do you consume\nper day?",width=22,font=("bold", 10))
fruits.place(x=580,y=400)
fruits_entry = Entry(root)
fruits_entry.place(x=740,y=410)
fruits_var = 0

predictAge = Label(root, text="What age would \nyou like to predict?",width=20,font=("bold", 10))
predictAge.place(x=580,y=450)
predictAge_entry = Entry(root)
predictAge_entry.place(x=740,y=460)
predictAge_var = 0

def on_click():
    name_var = name_entry.get()
    age_var = int(age_entry.get())
    height_var = int(height_entry.get())
    weight_var = int(weight_entry.get())
    race_var = int(race_entry.get())
    highBP_var = int(highBP_entry.get())
    medsBP_var = int(medsBP_entry.get())
    highChol_var = int(highChol_entry.get())
    smoke100_var = int(smoke100_entry.get())
    smokeFrequency_var = int(smokeFrequency_entry.get())
    drinkFrequnecy_var = int(drinkFrequency_entry.get())
    physical_var = int(physical_entry.get())
    veggies_var = int(veggies_entry.get())
    fruits_var = int(fruits_entry.get())
    predictAge_var = int(predictAge_entry.get())
    bmi = 703*(weight_var/(height_var**2))






    # filepaths
    h5_folder_path = "../H5s/"


    # set args
    age = age_var
    sex = 1
    wanted_age = predictAge_var
    race = race_var
    hi_bpressure = highBP_var
    on_HBP_meds = highBP_var
    hi_blood_chol = medsBP_var
    height = height_var
    weight = weight_var
    height_m = height * 0.0254
    weight_kg = weight * 0.453592
    bmi = height_m / (weight_kg**2)
    smoked_100 = smoke100_var
    smoke_freq = smokeFrequency_var # 1-everyday, 2, somedays, 3-not at all
    drink_freq = drinkFrequency_var # range 0-30
    physical_mins_week = physical_var
    veg_per_day = veggies_var
    fruits_per_day = fruits_var



    # # Phil's data
    # age = 19

    # sex = 1
    # race = 3
    # hi_bpressure = 3
    # on_HBP_meds = 2
    # hi_blood_chol = 2
    # height = 72
    # weight = 150
    # height_m = height * 0.0254
    # weight_kg = weight * 0.453592
    # bmi = height_m / (weight_kg**2)
    # smoked_100 = 2
    # smoke_freq = 3 # 1-everyday, 2, somedays, 3-not at all
    # drink_freq = 0 # range 0-30
    # physical_mins_week = 1
    # veg_per_day = 3
    # fruits_per_day = 1
    # had_heart_att = 0
    # had_stroke = 0
    # had_diabetes = 0

    # # find age difference


    inputs = np.array([hi_bpressure, on_HBP_meds, sex, hi_blood_chol, smoked_100,
            smoke_freq, drink_freq, wanted_age, fruits_per_day, veg_per_day, physical_mins_week, race, height, weight, bmi]).reshape(1, 15)


    # load model
    stroke_model = keras.models.load_model(h5_folder_path + "stroke_model.h5")
    heart_attack_model = keras.models.load_model(h5_folder_path + "heart_attack_model.h5")
    kidney_d_model = keras.models.load_model(h5_folder_path + "kidney_disease_model.h5")
    diabetes_model = keras.models.load_model(h5_folder_path + "diabetes_model.h5")
    ang_or_chd_model = keras.models.load_model(h5_folder_path + "ang_or_chd_model.h5") 
    cancer_model = keras.models.load_model(h5_folder_path + "cancer_model.h5")



    stroke_results = stroke_model.predict(inputs)
    heart_attack_results = heart_attack_model.predict(inputs)
    kidney_d_results = kidney_d_model.predict(inputs)
    diabetes_results = diabetes_model.predict(inputs)
    ang_or_chd_result = ang_or_chd_model.predict(inputs)
    cancer_result = cancer_model.predict(inputs)


    print()
    print()
    print("Stroke prediction:", stroke_results)
    print("Heart Attack prediction:", heart_attack_results)
    print("Kidney disease prediction:", kidney_d_results)
    print("Diabetes prediction:", kidney_d_results)
    print("Angina or Coronary Heart Disease prediction:", ang_or_chd_result)
    print("Cancer prediction:", cancer_result)

    pred_list = []
    pred_list.append((stroke_results[0][0], "Stroke"))
    pred_list.append((heart_attack_results[0][0], "Heart Attack"))
    pred_list.append((kidney_d_results[0][0], "Kidney Disease"))
    pred_list.append((diabetes_results[0][0], "Diabetes"))
    pred_list.append((ang_or_chd_result[0][0], "Angina or Coronary Heart Disease"))
    pred_list.append((cancer_result[0][0], "Cancer"))

    pred_list.sort(reverse=True)
    # print(pred_list)

    print("Before we show you your results, we want to remind you that predictions based on our model are in no way a replacement for regular physician checkups and any medical evaluations they may advise. We offer preventative advising that should not be taken as a rigorous diagnostic test. Feel free to discuss your results with your primary healthcare provider for a more thorough assessment of your overall health status.")

    print()
    print()
    print("Here are your personalized results!")

    print("Based on our predictions, at {w_age}, your probabilities of getting the following diseases are:".format(w_age=wanted_age))
    for tup in pred_list:
        print((tup[1] + ":"), str(round_sig(float(str(tup[0]*100))))+'%')

    most_likely_disease = pred_list[0][1]
    print()
    print()
    if (pred_list[0][0]) <= 0.4:
        print("Our predictions suggest that if you maintain your current habits, your chance of getting the above diseases at age {w_age} is low. Congrats and keep it up, {name}!".format(w_age=wanted_age, name=name_var))
    else:
        print("At age {w_age}, you are most at risk of getting {disease}. You should consider:".format(w_age=wanted_age, disease=most_likely_disease))
        if most_likely_disease=="Stroke":
            print("If you currently smoke quitting can go a long way in lowering your chance of stroke. Increasing your physical activity can improve heart health and decrease your risk for a stroke.")
        elif most_likely_disease=="Heart Attack":
            print("If you currently smoke quitting can go a long way in lowering your chance of heart attack. Increasing your physical activity can improve heart health and decrease your risk for a heart attack.")
        elif most_likely_disease=="Kidney Disease":
            print("Depending on your lifestyle, recommendations would be losing weight, if necessary, exercising more, limiting alcohol consumption, and quitting smoking.")
        elif most_likely_disease=="Diabetes":
            print("Eating healthy, including plenty of fruits and vegetables is crucial to lowering your chance of developing diabetes.")
        elif most_likely_disease=="Angina or Coronary Heart Disease":
            print("Eating healthy, including plenty of fruits and vegetables is crucial to lowering your chance of developing coronary heart disease. Additionally, getting plenty of exercise and maintaining a healthy weight help prevent coronary heart disease. ")
        elif most_likely_disease=="Cancer":
            print("Eating healthy, including plenty of fruits and vegetables can lower your future risk of cancer. If you smoke, quitting smoking can significantly lower your chance of developing lung cancer especially. ")










# label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
# label_3.place(x=70,y=230)
# var = IntVar()
# Radiobutton(root, text="Male",padx = 0, variable=var, value=1).place(x=235,y=230)
# Radiobutton(root, text="Female",padx = 0, variable=var, value=2).place(x=290,y=230)


ttk.Button(root, text='Submit',width=20, command=on_click).place(x=660,y=510)
# it is use for display the registration form on the window
root.mainloop()
print("Registration form  seccussfully created...")








