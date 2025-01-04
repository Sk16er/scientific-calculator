import tkinter as tk
from tkinter import messagebox, scrolledtext
import numpy as np

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("520x650")
        self.root.resizable(0, 0)
        
        self.expression = ""
        self.input_text = tk.StringVar()
        self.history = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Entry widget to display the expression
        input_frame = tk.Frame(self.root, bg="#f0f0f0")  # Light gray background
        input_frame.pack(side=tk.TOP)
        
        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bg="#f0f0f0", fg="#000000", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0, columnspan=8, ipadx=8, ipady=25)
        input_field.pack(ipady=10)

        # History display
        self.history_box = scrolledtext.ScrolledText(self.root, width=50, height=6, bg="#f0f0f0", fg="#000000", font=('arial', 12))
        self.history_box.pack(pady=10)
        
        # Frame for the buttons
        btns_frame = tk.Frame(self.root, bg="#f0f0f0")  # Light gray background
        btns_frame.pack()
        
        # Button layout configuration
        buttons = [
            ('C', 1, 0, 1), ('/', 1, 1, 1), ('*', 1, 2, 1), ('-', 1, 3, 1), ('+', 1, 4, 1), ('=', 1, 5, 1),
            ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('sin', 2, 3, 1), ('cos', 2, 4, 1), ('tan', 2, 5, 1),
            ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('log', 3, 3, 1), ('√', 3, 4, 1), ('^', 3, 5, 1),
            ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('kg→lb', 4, 3, 1), ('m→ft', 4, 4, 1), ('°C→°F', 4, 5, 1),
            ('0', 5, 0, 2), ('.', 5, 2, 1), ('°C→K', 5, 3, 1), ('°F→K', 5, 4, 1), ('°F→°C', 5, 5, 1),
            ('History', 6, 0, 6)
        ]

        for (text, row, col, cs) in buttons:
            button = tk.Button(btns_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#d3d3d3", cursor="hand2", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=cs, padx=1, pady=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.btn_clear()
        elif char == '=':
            self.btn_equal()
        elif char == 'kg→lb':
            self.kg_to_lb()
        elif char == 'm→ft':
            self.m_to_ft()
        elif char == '°C→°F':
            self.c_to_f()
        elif char == '°C→K':
            self.c_to_k()
        elif char == '°F→K':
            self.f_to_k()
        elif char == '°F→°C':
            self.f_to_c()
        elif char == 'History':
            self.show_history()
        else:
            self.btn_click(char)
    
    def btn_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)
    
    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")
    
    def btn_equal(self):
        try:
            result = str(eval(self.expression, {"__builtins__": None}, {"sin": np.sin, "cos": np.cos, "tan": np.tan, "log": np.log, "sqrt": np.sqrt}))
            self.input_text.set(result)
            self.history.append(f"{self.expression} = {result}")
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

    def kg_to_lb(self):
        try:
            kg = float(self.expression)
            lb = kg * 2.20462
            self.input_text.set(f"{lb} lb")
            self.history.append(f"{kg} kg = {lb} lb")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def m_to_ft(self):
        try:
            m = float(self.expression)
            ft = m * 3.28084
            self.input_text.set(f"{ft} ft")
            self.history.append(f"{m} m = {ft} ft")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def c_to_f(self):
        try:
            c = float(self.expression)
            f = (c * 9/5) + 32
            self.input_text.set(f"{f} °F")
            self.history.append(f"{c} °C = {f} °F")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def c_to_k(self):
        try:
            c = float(self.expression)
            k = c + 273.15
            self.input_text.set(f"{k} K")
            self.history.append(f"{c} °C = {k} K")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def f_to_k(self):
        try:
            f = float(self.expression)
            k = (f + 459.67) * 5/9
            self.input_text.set(f"{k} K")
            self.history.append(f"{f} °F = {k} K")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def f_to_c(self):
        try:
            f = float(self.expression)
            c = (f - 32) * 5/9
            self.input_text.set(f"{c} °C")
            self.history.append(f"{f} °F = {c} °C")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def show_history(self):
        self.history_box.delete(1.0, tk.END)
        for entry in self.history:
            self.history_box.insert(tk.END, entry + '\n')

# Create the main window
root = tk.Tk()
Calculator(root)
root.mainloop()
