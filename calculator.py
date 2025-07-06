import tkinter as tk

# --- Core functions ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error"

# --- Calculator Logic ---
current_input = ""

def button_click(value):
    global current_input
    current_input += str(value)
    entry_var.set(current_input)

def clear():
    global current_input
    current_input = ""
    entry_var.set("")

def calculate():
    global current_input
    try:
        # Safe evaluation using predefined functions only
        result = eval(current_input, {"__builtins__": None}, {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
            "__builtins__": None
        })
        entry_var.set(f"Result: {result}")
        current_input = ""
    except Exception:
        entry_var.set("Error")
        current_input = ""

# --- GUI Setup ---
window = tk.Tk()
window.title("Return-Based Calculator")
window.resizable(False, False)

entry_var = tk.StringVar()
entry_display = tk.Entry(window, textvariable=entry_var, font=("Arial", 20), justify='right', bd=10, width=15)
entry_display.grid(row=0, column=0, columnspan=4, pady=10)

# Button Layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0), ("Exit", 5, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(window, text=text, width=32, height=2, command=calculate).grid(row=row, column=0, columnspan=3)
    elif text == "C":
        tk.Button(window, text=text, width=7, height=2, command=clear).grid(row=row, column=col)
    elif text == "Exit":
        tk.Button(window, text=text, width=7, height=2, command=window.quit).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, width=7, height=2, command=lambda val=text: button_click(val)).grid(row=row, column=col)

window.mainloop()
