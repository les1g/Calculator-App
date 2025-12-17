import tkinter as tk # GUI library
from core import add, subtract, multiply, divide # import calculator functions from core.py module

def on_click(symbol): # handle button clicks
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear(): # clear the entry widget
    entry.delete(0, tk.END) 

def backspace():
    current = entry.get()
    if current:  # only delete if there's something
        entry.delete(len(current)-1, tk.END)

def calculate(): # perform calculation based on the expression in the entry widget
    try:
        expression = entry.get()

        if '+' in expression: # check for addition
            a, b = map(float, expression.split('+'))
            result = add(a, b)
        elif '-' in expression: # check for subtraction
            a, b = map(float, expression.split('-'))
            result = subtract(a, b)
        elif '*' in expression: # check for multiplication
            a, b = map(float, expression.split('*'))
            result = multiply(a, b)
        elif '/' in expression: # check for division
            a, b = map(float, expression.split('/'))
            result = divide(a, b)
        else:
            result = "Error" # unsupported operation

        entry.delete(0, tk.END) 

        #  no decimal for whole numbers
        if isinstance(result, float) and result.is_integer():
            entry.insert(0, str(int(result)))
        else:
            entry.insert(0, str(result))

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# GUI setup
root = tk.Tk() # create main window
root.title("Calculator") # window title
root.bind('<Return>', lambda event: calculate()) # allows you to click enter with peripheral keyboard
root.bind('<Escape>', lambda event: clear())   # Press Esc to clear

# Styling
root.configure(bg="#ffe6f0") # light pink background

entry = tk.Entry( # input field for expressions and results
    root, width=20, font=('Comic Neue', 18, 'bold'), 
    borderwidth=3, relief="groove", justify='right', 
    bg="#fff0f5", fg="#333" 
)

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10) # position the entry widget in the grid

entry.focus_set() # Set focus to the entry widget

# Buttons layout
buttons = [ # list of buttons with their text and grid positions
    ('C', 1, 0), ('DEL',1, 1),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3)
]

for (text, row, col) in buttons: # create and place buttons in the grid
    if text == '=': # bind equals to calculate function
        action = calculate
    elif text == 'C': # bind clear to clear function
        action = clear
    elif text == 'DEL': # bind delete to backspace function
        action = backspace
    else:
        action = lambda t=text: on_click(t) # default button action
    
    tk.Button( 
        root, text=text, width=5, height=2, 
        font=('Comic Neue', 14, 'bold'),
        bg="#ffd0e6", fg="#333", activebackground="#fabada",
        relief="raised", bd=3, command=action
    ).grid(row=row, column=col, padx=5, pady=5)

root.mainloop() 

    