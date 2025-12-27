import tkinter as tk

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window with black background
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='black')

# Display with black background and green text
display = tk.Entry(root, width=20, font=('Arial', 20), justify='right', bg='black', fg='green', insertbackground='green')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons with black background and green text
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, bg='black', fg='green', activebackground='green', activeforeground='black', command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, bg='black', fg='green', activebackground='green', activeforeground='black', command=clear_display)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, bg='black', fg='green', activebackground='green', activeforeground='black', command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
