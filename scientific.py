import tkinter as tk
from tkinter import messagebox
import numpy as np

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("480x600")
        self.root.resizable(0, 0)
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Entry widget to display the expression
        input_frame = tk.Frame(self.root, bg="#282c34")
        input_frame.pack(side=tk.TOP)
        
        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bg="#282c34", fg="#61dafb", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0, columnspan=8, ipadx=8, ipady=25)
        input_field.pack(ipady=10)
        
        # Frame for the buttons
        btns_frame = tk.Frame(self.root, bg="#282c34")
        btns_frame.pack()
        
        # Button layout configuration
        buttons = [
            ('C', 1, 0), ('/', 1, 1), ('*', 1, 2), ('-', 1, 3), ('+', 1, 4), ('=', 1, 5),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('sin', 2, 3), ('cos', 2, 4), ('tan', 2, 5),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('log', 3, 3), ('√', 3, 4), ('^', 3, 5),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('kg→lb', 4, 3), ('m→ft', 4, 4), ('°C→°F', 4, 5),
            ('0', 5, 0, 2), ('.', 5, 2), ('°C→K', 5, 3), ('°F→K', 5, 4), ('°F→°C', 5, 5)
        ]

        for (text, row, col, cs=1) in buttons:
            button = tk.Button(btns_frame, text=text, fg="white", width=10, height=3, bd=0, bg="#3e4451", cursor="hand2", command=lambda t=text: self.on_button_click(t))
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
            result = str(eval(self.expression, {"__builtins__": None}, {"sin": np.sin, "cos": np.cos, "tan": np.tan, "log": np.log, "sqrt": np.sqrt, "__builtins__": {}}))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

    def kg_to_lb(self):
        try:
            kg = float(self.expression)
            lb = kg * 2.20462
            self.input_text.set(f"{lb} lb")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def m_to_ft(self):
        try:
            m = float(self.expression)
            ft = m * 3.28084
            self.input_text.set(f"{ft} ft")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def c_to_f(self):
        try:
            c = float(self.expression)
            f = (c * 9/5) + 32
            self.input_text.set(f"{f} °F")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def c_to_k(self):
        try:
            c = float(self.expression)
            k = c + 273.15
            self.input_text.set(f"{k} K")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def f_to_k(self):
        try:
            f = float(self.expression)
            k = (f + 459.67) * 5/9
            self.input_text.set(f"{k} K")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def f_to_c(self):
        try:
            f = float(self.expression)
            c = (f - 32) * 5/9
            self.input_text.set(f"{c} °C")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

# Create the main window
root = tk.Tk()
Calculator(root)
root.mainloop()
