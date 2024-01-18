import csv #datu ierakstīšanai un nolasīšanai
import tkinter as tk #programmas grafiskā saskarne
from tkinter import ttk #treeview izmantošanai
from datetime import datetime #ierakstu datuma un laika fiksēšana

# Mēginam piekļūt datnei ar informāciju, ja tā neeksistē, tā tiek izveidota
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

# Palaižam programmas galveno ciklu
root.mainloop()

