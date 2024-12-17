import tkinter as tk
from tkinter import messagebox
import math

# Functions for Calculator Operations


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    return a % b


def exponentiate(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(a)


def factorial(a):
    if a < 0:
        raise ValueError("Cannot compute factorial of a negative number.")
    return math.factorial(int(a))


def percentage(a, b):
    if b == 0:
        raise ValueError("Whole cannot be zero for percentage calculation.")
    return (a / b) * 100

# Function to Evaluate and Display Results


def calculate():
    try:
        operation = operation_var.get()
        num1 = float(entry1.get()) if entry1.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0

        # Perform the selected operation
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Modulus":
            result = modulus(num1, num2)
        elif operation == "Exponentiate":
            result = exponentiate(num1, num2)
        elif operation == "Square Root":
            result = square_root(num1)
        elif operation == "Factorial":
            result = factorial(num1)
        elif operation == "Percentage":
            result = percentage(num1, num2)
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred.", str(e))


# GUI Creation
app = tk.Tk()
app.title("Python Calculator")
app.geometry("400x500")
app.configure(bg="#f0f0f0")

# Heading
heading_label = tk.Label(app, text="Python Calculator",
                         font=("Arial", 18, "bold"), bg="#f0f0f0")
heading_label.pack(pady=10)

# Number 1 Entry
tk.Label(app, text="Enter first number:", bg="#f0f0f0").pack()
entry1 = tk.Entry(app, width=20, font=("Arial", 14))
entry1.pack(pady=5)

# Number 2 Entry
tk.Label(app, text="Enter second number (if applicable):", bg="#f0f0f0").pack()
entry2 = tk.Entry(app, width=20, font=("Arial", 14))
entry2.pack(pady=5)

# Dropdown for Operations
tk.Label(app, text="Choose Operation:", bg="#f0f0f0").pack(pady=5)
operations = [
    "Add", "Subtract", "Multiply", "Divide", "Modulus",
    "Exponentiate", "Square Root", "Factorial", "Percentage"
]
operation_var = tk.StringVar()
operation_var.set("Add")
operation_menu = tk.OptionMenu(app, operation_var, *operations)
operation_menu.config(font=("Arial", 12))
operation_menu.pack(pady=10)

# Calculate Button
calculate_button = tk.Button(app, text="Calculate", font=(
    "Arial", 14), bg="#4CAF50", fg="white", command=calculate)
calculate_button.pack(pady=15)

# Result Display
result_label = tk.Label(app, text="Result: ", font=(
    "Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
result_label.pack(pady=20)

# Run the GUI Loop
app.mainloop()
