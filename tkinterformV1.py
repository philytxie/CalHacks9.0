from tkinter import*
from tkinter import ttk
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

physical = Label(root, text="How many minutes of\nphysical activity do you \nengage in per week?",width=22,font=("bold", 10))
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
    name_var = int(name_entry.get())
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
    print(age_var == 1)


# label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
# label_3.place(x=70,y=230)
# var = IntVar()
# Radiobutton(root, text="Male",padx = 0, variable=var, value=1).place(x=235,y=230)
# Radiobutton(root, text="Female",padx = 0, variable=var, value=2).place(x=290,y=230)


ttk.Button(root, text='Submit',width=20, command=on_click).place(x=660,y=510)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")