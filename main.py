import csv
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os

current_directory = os.getcwd()
file_path = os.path.join(current_directory, "data.csv")

def load_data():
    total_income = 0
    total_expenses = 0
    # Iztukšot koku, lai korekti strādātu datu atjaunošana
    for item in tree.get_children():
        tree.delete(item)

    # Mēģinam atvērt datni, ja tās nav, izveidojam jaunu
    try:
        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tree.insert("", 0, values=(row["Datums"], row["Apraksts"], row["Tips"], row["Summa"]), tags=(row["Tips"],))
                if row["Tips"] == "Ienākumi":
                    total_income += float(row["Summa"])
                elif row["Tips"] == "Izmaksas":
                    total_expenses += float(row["Summa"])
    except FileNotFoundError:
        with open(file_path, mode="w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["Datums", "Apraksts", "Tips", "Summa"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    # Bilances skaitīšana
    balance = total_income - total_expenses
    balance_label.config(text=f"Bilance: {balance:.2f} €")
    if balance >= 0:
        balance_label.config(foreground="green")
    else:
        balance_label.config(foreground="red")

# Dzēšana
def delete_record():
    selected_item = tree.selection()
    if not selected_item:
        return  # Kad nekas netiek izvēlēts, nekas nenotiks
    else:
        with open(file_path, mode="r", newline='', encoding="utf-8") as csvfile:
            rows = list(csv.DictReader(csvfile))

        index = tree.index(selected_item)
        del rows[index]

        with open(file_path, mode="w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["Datums", "Apraksts", "Tips", "Summa"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        load_data()

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
        with open(file_path, mode="a", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["Datums", "Apraksts", "Tips", "Summa"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Pievienojam header, ja tā nav
            if csvfile.tell() == 0:
                writer.writeheader()

            # Pievienojam jaunu ierakstu datnē
            writer.writerow({
                "Datums": date_var.get(),
                "Apraksts": description_var.get(),
                "Tips": type_var.get(),
                "Summa": amount_var.get()
            })

        add_window.destroy()
        load_data()
        
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

    tk.Button(add_window, text="Saglabāt", command=save_record).grid(row=4, column=0, columnspan=2)

# Veidojam programmas logu
root = tk.Tk()
root.geometry("800x800")
root.title("Finanses")

balance_label = tk.Label(root, text="Bilance: 0.00 €", font=("Helvetica", 16, "bold"))
balance_label.pack(side=tk.TOP, pady=10)

# Veidojam Treeview
tree_frame = ttk.Frame(root)
tree_frame.pack(expand=True, fill='both')
vsb = ttk.Scrollbar(tree_frame, orient="vertical")
vsb.pack(side='right', fill='y')
tree = ttk.Treeview(tree_frame, columns=("Datums", "Apraksts", "Tips", "Summa"), show="headings")
tree.heading("Datums", text="Datums")
tree.heading("Apraksts", text="Apraksts")
tree.heading("Tips", text="Tips")
tree.heading("Summa", text="Summa")
tree.pack(expand=True, fill='both')
vsb.config(command=tree.yview)

# Iemaksu un izmaksu krāsošana
tree.tag_configure("Ienākumi", background="pale green")
tree.tag_configure("Izmaksas", background="light coral")

# Ielādējam datus no CSV faila
load_data()

add_button = tk.Button(root, text="Pievienot ierakstu", command=add_record_window, bg="pale green")
add_button.pack(side=tk.TOP, padx=5)
delete_button = tk.Button(root, text="Dzēst ierakstu", command=delete_record, bg="lightcoral")
delete_button.pack(side=tk.TOP, padx=5)

# Palaižam programmas galveno ciklu
root.mainloop()
