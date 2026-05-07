import tkinter as tk

window = tk.Tk()
window.title("Multi Bucket")
window.geometry("400x400")

# money
money_lbl_title = tk.Label(window, text="Money Bucket")
money_lbl_title.grid(row=0, column=0)
money_frame = tk.Frame(window, bg="#e7e8e6", width=100, height=100, bd=3, relief=tk.RIDGE)
money_frame.grid(row=1, column=0)
money_lbl = tk.Label(money_frame, text="COBOL")
money_lbl.grid(row=0, column=0)
money_button = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center")
money_button.grid(row=2, column=0)

# passion
passion_lbl_title = tk.Label(window, text="Passion Bucket")
passion_lbl_title.grid(row=0, column=1)
passion_frame = tk.Frame(window, bg="#e7e8e6", width=100, height=100, bd=3, relief=tk.RIDGE)
passion_frame.grid(row=1, column=1)
passion_lbl = tk.Label(passion_frame, text="Blender")
passion_lbl.grid(row=0, column=0)
passion_button = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center")
passion_button.grid(row=2, column=1)

# learning
learning_lbl_title = tk.Label(window, text="Learning Bucket")
learning_lbl_title.grid(row=0, column=2)
learning_frame = tk.Frame(window, bg="#e7e8e6", width=100, height=100, bd=3, relief=tk.RIDGE)
learning_frame.grid(row=1, column=2)
learning_lbl = tk.Label(learning_frame, text="Guitarra")
learning_lbl.grid(row=0, column=0)
learning_button = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center")
learning_button.grid(row=2, column=2)

window.mainloop()