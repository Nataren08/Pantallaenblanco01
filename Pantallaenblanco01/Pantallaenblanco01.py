from tkinter import*
from tkinter import ttk
ventana = Tk()
ventana.title("Primer ventana en blanco 3M")#cambiar el nombre de la ventana
ventana.geometry("520x480")#configurar tamaño

boton1 = ttk.Button(text="Hola, mundo")
boton1.place(x=50, y=50)
entrada = ttk.Entry()
entrada.place(x=50, y=80, width =150)

ventana.mainloop()
