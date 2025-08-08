import tkinter as tk

def launch_calculator():
    print("Launching Calculator")
    window = tk.Toplevel()
    window.title("Calculator")
    window.geometry("300x400")
    window.resizable(False, False)

    expression = ""

    # Display
    display_var = tk.StringVar()
    display = tk.Entry(window, textvariable=display_var, font=("Arial", 20), justify='right', bd=10, relief='sunken', state='readonly')
    display.pack(fill='both', padx=10, pady=10, ipady=10)

    def update_display(value):
        nonlocal expression
        expression += str(value)
        display_var.set(expression)

    def calculate():
        nonlocal expression
        try:
            result = str(eval(expression))
            display_var.set(result)
            expression = result
        except Exception:
            display_var.set("Error")
            expression = ""
    
    def clear():
        nonlocal expression
        expression = ""
        display_var.set("")

    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', 'C', '=', '+']
    ]

    button_frame = tk.Frame(window)
    button_frame.pack(expand=True, fill='both')

    #required to ensure each button is expanding as it should
    for i in range(4):
        button_frame.columnconfigure(i, weight=1)
        button_frame.rowconfigure(i, weight=1)

    # iterating over each item of the list of arrays above
    for r, row in enumerate(buttons):
        for c, btn_text in enumerate(row):
            if btn_text == 'C':
                action = clear
            elif btn_text == '=':
                action = calculate
            else:
                action = lambda val=btn_text: update_display(val)

            btn = tk.Button(
                button_frame, text=btn_text, font=("Helvetica", 16), height=2, width=5, command=action
            )

            btn.grid(row=r, column=c, sticky='nsew', padx=2, pady=2)