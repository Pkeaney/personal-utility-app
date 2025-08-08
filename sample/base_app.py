

import tkinter as tk
from tkinter import ttk
from calculator_app import launch_calculator

def main():
    root = tk.Tk()
    root.title("My Personal Utilities Application")
    root.geometry("400x300")
    root.resizable(False, False)

    #main app frame which will be used to assign padding and central alignment to the base app
    app_frame = ttk.Frame(root, padding=20)
    app_frame.pack(expand=True)

    # Title
    title_label = ttk.Label(app_frame, text="My Utilities App", font=("Helvetica", 18, "bold"))
    title_label.pack(pady=(0,20))

    #Utility buttons
    utilities = [
        ("Calculator", launch_calculator),
        ("Notes (Coming soon)", None),
        ("Timer (Coming soon)", None),
        ("AI Assistant (Coming soon)", None)
    ]

    for label, command in utilities:
        if command:
            btn = ttk.Button(app_frame, text=label, command=command)
        else:
            btn = ttk.Button(app_frame, text=label, state="disabled")
        btn.pack(pady=5, fill='x')
    

    # Footer
    footer = ttk.Label(app_frame, text = "v1.0", font=("Arial", 8))
    footer.pack(pady=(30,0))

    root.mainloop()

if __name__ == "__main__":
    main()

