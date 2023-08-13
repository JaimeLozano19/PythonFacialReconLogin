import tkinter as tk

def agregar_usuario():
    # Lógica para agregar usuario
    pass

def borrar_usuario():
    # Lógica para borrar usuario
    pass

def editar_usuario():
    # Lógica para editar usuario
    pass

def consultar_usuario():
    # Lógica para consultar usuario
    pass

def salir():
    root.destroy()

root = tk.Tk()
root.title("User Management")

login_label = tk.Label(root, text="Login")
login_label.pack()

agregar_button = tk.Button(root, text="Add User", command=agregar_usuario)
agregar_button.pack()

borrar_button = tk.Button(root, text="Delete User", command=borrar_usuario)
borrar_button.pack()

editar_button = tk.Button(root, text="Edit User", command=editar_usuario)
editar_button.pack()

consultar_button = tk.Button(root, text="Query User", command=consultar_usuario)
consultar_button.pack()

salir_button = tk.Button(root, text="Exit", command=salir)
salir_button.pack()

root.mainloop()
