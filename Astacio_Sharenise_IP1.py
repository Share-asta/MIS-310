import tkinter as tk

main_window = tk.Tk()
main_window.title("Health Tracker ♡")
main_window.geometry("450x450")

#variables
weight_var = tk.StringVar()
height_var = tk.StringVar()
water_var = tk.StringVar()
result_var = tk.StringVar()
water_total_var = tk.StringVar(value="Total Water Intake: 0 liters")

#dictionary
water_history = []

#functions
def calculate_bmi():
    try:
        weight = float(weight_var.get())
        height = float(height_var.get())

        #BMI calculation
        bmi_imperial = (weight / (height ** 2)) * 703

        #conversion
        weight_kg = weight * 0.453592
        height_m = height * 0.0254
        bmi_metric = weight_kg / (height_m ** 2)

        #metric BMI
        if bmi_metric < 18.5:
            category = "Underweight"
        elif bmi_metric < 24.9:
            category = "Normal weight"
        elif bmi_metric < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_var.set(
            f"Imperial BMI: {bmi_imperial:.2f}\n"
            f"Metric BMI: {bmi_metric:.2f}\nCategory: {category}"
        )
    except ValueError:
        result_var.set("Error: Enter valid numbers")

def add_water():
    try:
        water = float(water_var.get())
        water_history.append(water)
        total = sum(water_history)
        water_total_var.set(f"Total Water Intake: {total:.2f} liters")
    except ValueError:
        water_total_var.set("Error: Enter valid number")

def clear_all():
    weight_var.set("")
    height_var.set("")
    water_var.set("")
    result_var.set("")
    water_total_var.set("Total Water Intake: 0 liters")
    water_history.clear()

#labels
tk.Label(main_window, text="Weight (pounds):").pack()
tk.Entry(main_window, textvariable=weight_var).pack()

tk.Label(main_window, text="Height (inches):").pack()
tk.Entry(main_window, textvariable=height_var).pack()

tk.Label(main_window, text="Water Intake (liters):").pack()
tk.Entry(main_window, textvariable=water_var).pack()

#buttons
tk.Button(main_window, text="Calculate BMI", command=calculate_bmi).pack()
tk.Button(main_window, text="Add Water Intake", command=add_water).pack()
tk.Button(main_window, text="Clear All", command=clear_all).pack()

#output
tk.Label(main_window, textvariable=result_var).pack()
tk.Label(main_window, textvariable=water_total_var).pack()

main_window.mainloop()
