import tkinter as tk


def calculate_maintenance():
    """Calculate the maintenance calories based on user input."""
    gender = var_gender.get()
    age = int(entry_age.get())
    weight = int(entry_weight.get())
    height = int(entry_height.get())
    activity_level = var_activity.get()

    if gender == 'male':
        maintenance_calories = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        maintenance_calories = (10 * weight) + (6.25 * height) - (5 * age) - 161

    if activity_level == 'sedentary':
        maintenance_calories *= 1.2
    elif activity_level == 'lightly active':
        maintenance_calories *= 1.375
    elif activity_level == 'moderately active':
        maintenance_calories *= 1.55
    elif activity_level == 'very active':
        maintenance_calories *= 1.725
    elif activity_level == 'extra active':
        maintenance_calories *= 1.9

    label_result.config(text="Your maintenance calories are: {:.2f}".format(maintenance_calories))


# Create the window
window = tk.Tk()
window.title("Maintenance Calories Calculator")

# Create the gender label and radio buttons
label_gender = tk.Label(window, text="Select your gender:")
label_gender.grid(column=0, row=0)
var_gender = tk.StringVar()
var_gender.set('male')
radio_male = tk.Radiobutton(window, text="Male", variable=var_gender, value='male')
radio_male.grid(column=0, row=1)
radio_female = tk.Radiobutton(window, text="Female", variable=var_gender, value='female')
radio_female.grid(column=1, row=1)

# Create the age label and entry box
label_age = tk.Label(window, text="Enter your age:")
label_age.grid(column=0, row=2)
entry_age = tk.Entry(window)
entry_age.grid(column=1, row=2)

# Create the weight label and entry box
label_weight = tk.Label(window, text="Enter your weight (in kg):")
label_weight.grid(column=0, row=3)
entry_weight = tk.Entry(window)
entry_weight.grid(column=1, row=3)

# Create the height label and entry box
label_height = tk.Label(window, text="Enter your height (in cm):")
label_height.grid(column=0, row=4)
entry_height = tk.Entry(window)
entry_height.grid(column=1, row=4)

# Create the activity level label and dropdown menu
label_activity = tk.Label(window, text="Select your activity level:")
label_activity.grid(column=0, row=5)
var_activity = tk.StringVar()
var_activity.set('sedentary')
dropdown_activity = tk.OptionMenu(window, var_activity, 'sedentary', 'lightly active', 'moderately active',
                                  'very active', 'extra active')
dropdown_activity.grid(column=1, row=5)

# Create the calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate_maintenance)
button_calculate.grid(column=1, row=6)

# Create the result label
label_result = tk.Label(window, text="")
label_result.grid(column=0, row=7, columnspan=2)

# Run the window
window.mainloop()
