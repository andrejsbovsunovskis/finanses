import csv
import tkinter as tk
from tkinter import ttk
from datetime import datetime

def load_data():
    try:
        with open("data.csv", newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tree.insert("", tk.END, values=(row["Datums"], row["Apraksts"], row["Tips"], row["Summa"]), tags=(row["Tips"],))
    except FileNotFoundError:
        with open("data.csv", mode="w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["Datums", "Apraksts", "Tips", "Summa"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

def add_record_window():
    add_window = tk.Toplevel(root)
    add_window.title("Pievienot ierakstu")

    # Definējam mainīgos, lai saglabātu ievadītos datus
    date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
    description_var = tk.StringVar()
    type_var = tk.StringVar(value="Ienākumi")
    amount_var = tk.StringVar()

    # Funkcija, lai saglabātu jaunu ierakstu
    def save_record():
        with open("data.csv", mode="a", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date_var.get(), description_var.get(), type_var.get(), amount_var.get()])
        load_data()
        add_window.destroy()

    # Izveidojam un pievienojam ievades laukus
    tk.Label(add_window, text="Datums:").grid(row=0, column=0)
    date_entry = tk.Entry(add_window, textvariable=date_var)
    date_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Apraksts:").grid(row=1, column=0)
    tk.Entry(add_window, textvariable=description_var).grid(row=1, column=1)

    tk.Label(add_window, text="Tips:").grid(row=2, column=0)
    type_combobox = ttk.Combobox(add_window, textvariable=type_var, values=["Ienākumi", "Izmaksas"])
    type_combobox.grid(row=2, column=1)

    tk.Label(add_window, text="Summa:").grid(row=3, column=0)
    tk.Entry(add_window, textvariable=amount_var).grid(row=3, column=1)

    # Pievienojam pogu ieraksta saglabāšanai
    tk.Button(add_window, text="Saglabāt", command=save_record).grid(row=4, column=0, columnspan=2)

# Veidojam programmas logu
root = tk.Tk()
root.geometry("1000x800")
root.title("Finanses")

# Veidojam Treeview
tree = ttk.Treeview(root, columns=("Datums", "Apraksts", "Tips", "Summa"), show="headings")
tree.heading("Datums", text="Datums")
tree.heading("Apraksts", text="Apraksts")
tree.heading("Tips", text="Tips")
tree.heading("Summa", text="Summa")
tree.pack(padx=10, pady=10)

# Iemaksu un izmaksu krāsošana
tree.tag_configure("Ienākumi", background="pale green")
tree.tag_configure("Izmaksas", background="light coral")

# Ielādējam datus no CSV faila
load_data()

# Pievienojam pogu jauna ieraksta pievienošanai
tk.Button(root, text="Pievienot ierakstu", command=add_record_window).pack(pady=10)

# Palaižam programmas galveno ciklu
root.mainloop()