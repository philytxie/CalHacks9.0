import tensorflow as tf
from tensorflow import keras
import numpy as np



from math import log10, floor
def round_sig(x, sig=3):
    return round(x, sig-int(floor(log10(abs(x))))-1)

# filepaths
h5_folder_path = "../H5s/"


# set args
age = 35
sex = 1
race = 3
hi_bpressure = 1
on_HBP_meds = 1
hi_blood_chol = 1
height = 69
weight = 200
height_m = height * 0.0254
weight_kg = weight * 0.453592
bmi = height_m / (weight_kg**2)
smoked_100 = 0
smoke_freq = 1 # 1-everyday, 2, somedays, 3-not at all
drink_freq = 3 # range 0-30
physical_mins_week = 90
veg_per_day = 2
fruits_per_day = 0
had_heart_att = 0
had_stroke = 0
had_diabetes = 0


# Phil's data
age = 19
wanted_age = 60
sex = 1
race = 3
hi_bpressure = 3
on_HBP_meds = 2
hi_blood_chol = 2
height = 72
weight = 150
height_m = height * 0.0254
weight_kg = weight * 0.453592
bmi = height_m / (weight_kg**2)
smoked_100 = 2
smoke_freq = 3 # 1-everyday, 2, somedays, 3-not at all
drink_freq = 0 # range 0-30
physical_mins_week = 1
veg_per_day = 3
fruits_per_day = 1
had_heart_att = 0
had_stroke = 0
had_diabetes = 0

# find age difference


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
print(pred_list)

print("Before we show you your results, we want to remind you that predictions based on our model are in no way a replacement for regular physician checkups and any medical evaluations they may advise. We offer preventative advising that should not be taken as a rigorous diagnostic test. Feel free to discuss your results with your primary healthcare provider for a more thorough assessment of your overall health status.")

print()
print()
print("Here are the results!")

print("Based on our predictions, at {w_age}, your probabilities of getting the following diseases are:".format(w_age=wanted_age))
for tup in pred_list:
    print((tup[1] + ":"), str(round_sig(float(str(tup[0]*100))))+'%')

most_likely_disease = pred_list[0][1]
print()
print()
if (pred_list[0][0]) <= 0.4:
    print("Our predictions suggest that if you maintain your current habits, your chance of getting the above diseases at age {w_age} is low. Congrats and keep it up!".format(w_age=wanted_age))
else:
    print("At age {w_age}, you are most at risk of getting {disease}. You should consider:".format(w_age=wanted_age, disease=most_likely_disease))
    if most_likely_disease=="Stroke":
        print("If you currently smoke quitting can go a long way in lowering your chance of stroke. Increasing your physical activity can improve heart health and decrease your risk for a stroke.")
    elif most_likely_disease=="Heart Attack":
        print("If you currently smoke quitting can go a long way in lowering your chance of heart attack. Increasing your physical activity can improve heart health and decrease your risk for a heart attack.")
    elif most_likely_disease=="Kidney Disease":
        print("Depending on your lifestyle, recommendations would be losing weight, if necessary, exercising more, limiting alcohol consumption, and quitting smoking.")
    elif most_likely_disease=="Diabetes":
        print("")
    elif most_likely_disease=="Angina or Coronary Heart Disease":
        print()
    elif most_likely_disease=="Cancer":
        print()








