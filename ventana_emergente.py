import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print(file_path)


with open(file_path, 'r') as f:
    enlaces = f.read()
    f.close()

lista_enlaces = enlaces.split('\n')
print(lista_enlaces)