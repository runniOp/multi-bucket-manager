import tkinter as tk

window = tk.Tk()
window.title("Multi Bucket")
window.geometry("400x400")


# money
money_lbl_title = tk.Label(window, text="Money Bucket")
money_lbl_title.grid(row=0, column=0)
money_list_itens = []
money_listbox = tk.Listbox()
money_listbox.grid(row=1, column=0)
money_entry = tk.Entry()
money_entry.grid(row=2,column=0)

def money_submit():
    money_item = money_entry.get()
    money_listbox.insert(tk.END,money_item)

money_button = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center", command=money_submit)
money_button.grid(row=3, column=0)


# passion
passion_lbl_title = tk.Label(window, text="Passion Bucket")
passion_lbl_title.grid(row=0, column=1)
passion_list_itens = []
passion_listbox = tk.Listbox()
passion_listbox.grid(row=1, column=1)
passion_entry = tk.Entry()
passion_entry.grid(row=2,column=1)

def passion_submit():
    passion_item = passion_entry.get()
    passion_listbox.insert(tk.END,passion_item)

passion_button = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center", command=passion_submit)
passion_button.grid(row=3, column=1)

# learning
learning_lbl_title = tk.Label(window, text="Learning Bucket")
learning_lbl_title.grid(row=0, column=2)
learning_list_itens = []
learning_listbox = tk.Listbox()
learning_listbox.grid(row=1, column=2)
learning_entry = tk.Entry()
learning_entry.grid(row=2,column=2)

def learning_submit():
    learning_item = learning_entry.get()
    learning_listbox.insert(tk.END,learning_item)

learning_button = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center", command=learning_submit)
learning_button.grid(row=3, column=2)

window.mainloop()