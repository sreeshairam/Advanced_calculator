import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Basic eval-based calculation
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

def binary_operations(op):
    try:
        num = int(entry.get())
        result = ""
        if op == "bin":
            for i in range(2, len(bin(num))):  # Inefficient looping
                result += bin(num)[i]
        elif op == "oct":
            for i in range(2, len(oct(num))):
                result += oct(num)[i]
        elif op == "hex":
            for i in range(2, len(hex(num))):
                result += hex(num)[i]
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def fibonacci():
    try:
        n = int(entry.get())
        fib_series = []
        a, b = 0, 1
        for _ in range(n):  # Redundant looping
            fib_series.append(a)
            temp = a
            a = b
            b = temp + b
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(fib_series))
    except:
        messagebox.showerror("Error", "Invalid Input")

def probability():
    try:
        n, r = map(int, entry.get().split(','))
        fact_n = 1
        for i in range(1, n+1):  # Long factorial computation
            fact_n *= i
        fact_r = 1
        for i in range(1, r+1):
            fact_r *= i
        fact_nr = 1
        for i in range(1, n-r+1):
            fact_nr *= i
        result = fact_n // (fact_r * fact_nr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Enter values as n,r")

def log_base_10():
    try:
        num = float(entry.get())
        result = math.log10(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def factorial():
    try:
        num = int(entry.get())
        result = 1
        for i in range(1, num + 1):  # Inefficient factorial computation
            result *= i
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Advanced Calculator")
root.configure(bg='lightgray')

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, width=10, height=2, command=lambda t=text: entry.insert(tk.END, t) if t != '=' else calculate()).grid(row=row, column=col)

special_buttons = [
    ("Bin", lambda: binary_operations("bin"), 5, 0),
    ("Oct", lambda: binary_operations("oct"), 5, 1),
    ("Hex", lambda: binary_operations("hex"), 5, 2),
    ("Fib", fibonacci, 5, 3),
    ("Prob", probability, 6, 0),
    ("Log10", log_base_10, 6, 1),
    ("Fact", factorial, 6, 2)
]

for text, cmd, row, col in special_buttons:
    tk.Button(root, text=text, width=10, height=2, command=cmd).grid(row=row, column=col)

tk.Button(root, text="Clear", width=10, height=2, command=lambda: entry.delete(0, tk.END)).grid(row=6, column=3)
tk.Button(root, text="Exit", width=10, height=2, command=root.quit).grid(row=7, column=1)

root.mainloop()
