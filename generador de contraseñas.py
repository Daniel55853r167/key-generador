import tkinter as tk
from tkinter import messagebox
import random
import string
import os

def generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ''
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if caracteres == '':
        raise ValueError("Debe seleccionar al menos un tipo de caracter para generar contraseñas.")

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def generar_varias_contraseñas():
    try:
        cantidad = int(entry_cantidad.get())
        longitud = int(entry_longitud.get())
        usar_mayusculas = var_mayusculas.get()
        usar_minusculas = var_minusculas.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        contraseñas = []
        for _ in range(cantidad):
            contraseñas.append(generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_simbolos))

        escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        archivo_path = os.path.join(escritorio, "contraseñas.txt")
        
        with open(archivo_path, "w") as file:
            for contraseña in contraseñas:
                file.write(contraseña + "\n")

        messagebox.showinfo("Éxito", f"Se han generado {cantidad} contraseñas y se han guardado en {archivo_path}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Generador de Contraseñas")

# Variables de control
var_mayusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

# Elementos de la interfaz
label_cantidad = tk.Label(root, text="Cantidad de Contraseñas:")
label_cantidad.grid(row=0, column=0, padx=10, pady=5)

entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=0, column=1, padx=10, pady=5)
entry_cantidad.insert(0, "200")

label_longitud = tk.Label(root, text="Longitud de las Contraseñas:")
label_longitud.grid(row=1, column=0, padx=10, pady=5)

entry_longitud = tk.Entry(root)
entry_longitud.grid(row=1, column=1, padx=10, pady=5)
entry_longitud.insert(0, "12")

check_mayusculas = tk.Checkbutton(root, text="Incluir Mayúsculas", variable=var_mayusculas)
check_mayusculas.grid(row=2, column=0, padx=10, pady=5)

check_minusculas = tk.Checkbutton(root, text="Incluir Minúsculas", variable=var_minusculas)
check_minusculas.grid(row=2, column=1, padx=10, pady=5)

check_numeros = tk.Checkbutton(root, text="Incluir Números", variable=var_numeros)
check_numeros.grid(row=3, column=0, padx=10, pady=5)

check_simbolos = tk.Checkbutton(root, text="Incluir Símbolos", variable=var_simbolos)
check_simbolos.grid(row=3, column=1, padx=10, pady=5)

boton_generar = tk.Button(root, text="Generar Contraseñas", command=generar_varias_contraseñas)
boton_generar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

root.mainloop()
