import tkinter as tk
import csv
from itertools import zip_longest

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
    money_entry.delete(0,tk.END)

    save_all()


def remove_money_item():
    m_selected = money_listbox.curselection()
    for m_selected in m_selected[::-1]:
        money_listbox.delete(m_selected)
    
    save_all()

money_button_add = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center", command=money_submit)
money_button_add.grid(row=3, column=0)
money_button_remove = tk.Button(window, text="Remove", bd=3, height=5, width=10, justify="center", command=remove_money_item)
money_button_remove.grid(row=4, column=0)

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
    passion_entry.delete(0,tk.END)

    save_all()


def remove_passion_item():
    m_selected = passion_listbox.curselection()
    for m_selected in m_selected[::-1]:
        passion_listbox.delete(m_selected)
    
    save_all()

passion_button = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center", command=passion_submit)
passion_button.grid(row=3, column=1)
passion_button_remove = tk.Button(window, text="Remove", bd=3, height=5, width=10, justify="center", command=remove_passion_item)
passion_button_remove.grid(row=4, column=1)

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
    learning_entry.delete(0,tk.END)

    save_all()

def remove_learning_item():
    m_selected = learning_listbox.curselection()
    for m_selected in m_selected[::-1]:
        learning_listbox.delete(m_selected)
    save_all()

learning_button = tk.Button(window, text="Add", bd=3, height=5, width=10, justify="center", command=learning_submit)
learning_button.grid(row=3, column=2)
learning_button_remove = tk.Button(window, text="Remove", bd=3, height=5, width=10, justify="center", command=remove_learning_item)
learning_button_remove.grid(row=4, column=2)

def load_all():
    with open("bucket.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
            if row[0]: money_listbox.insert(tk.END, row[0])
            if row[1]: passion_listbox.insert(tk.END, row[1])
            if row[2]:learning_listbox.insert(tk.END, row[2])
       

def save_all():
    money = money_listbox.get(0, tk.END)
    passion = passion_listbox.get(0, tk.END)
    learning = learning_listbox.get(0, tk.END)

    with open("bucket.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["money", "passion", "learning"])  
        for row in zip_longest(money, passion, learning, fillvalue=""):
            writer.writerow(row)

load_all()
window.mainloop()