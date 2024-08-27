import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)            
        
        logo = utl.leer_imagen(".\imagenes\logo.jpg", (600, 600))
        label = tk.Label(self.ventana, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Sección para los inputs de las mesas
        self.frame_mesapanel = tk.Frame(self.ventana, bg='#fcfcfc')
        self.frame_mesapanel.place(x=100, y=50, width=300, height=600)
        
        self.label_numero_mesa = tk.Label(self.frame_mesapanel, text="Número de Mesa:", bg='#fcfcfc', font=('Arial', 12, BOLD))
        self.label_numero_mesa.pack(pady=10)
        self.entry_numero_mesa = tk.Entry(self.frame_mesapanel, font=('Arial', 12))
        self.entry_numero_mesa.pack(pady=10)

        self.label_capacidad_mesa = tk.Label(self.frame_mesapanel, text="Capacidad:", bg='#fcfcfc', font=('Arial', 12, BOLD))
        self.label_capacidad_mesa.pack(pady=10)
        self.entry_capacidad_mesa = tk.Entry(self.frame_mesapanel, font=('Arial', 12))
        self.entry_capacidad_mesa.pack(pady=10)

        self.label_ubicacion_mesa = tk.Label(self.frame_mesapanel, text="Ubicación:", bg='#fcfcfc', font=('Arial', 12, BOLD))
        self.label_ubicacion_mesa.pack(pady=10)
        self.entry_ubicacion_mesa = tk.Entry(self.frame_mesapanel, font=('Arial', 12))
        self.entry_ubicacion_mesa.pack(pady=10)

        # Botones para añadir, borrar y modificar mesas
        self.btn_agregar_mesa = tk.Button(self.frame_mesapanel, text="Agregar Mesa", command=self.agregar_mesa, font=('Arial', 12, BOLD), bg='#3a7ff6', fg='#fcfcfc')
        self.btn_agregar_mesa.pack(pady=10)
        
        self.btn_borrar_mesa = tk.Button(self.frame_mesapanel, text="Borrar Mesa", command=self.borrar_mesa, font=('Arial', 12, BOLD), bg='#3a7ff6', fg='#fcfcfc')
        self.btn_borrar_mesa.pack(pady=10)
        
        self.btn_modificar_mesa = tk.Button(self.frame_mesapanel, text="Modificar Mesa", command=self.modificar_mesa, font=('Arial', 12, BOLD), bg='#3a7ff6', fg='#fcfcfc')
        self.btn_modificar_mesa.pack(pady=10)

        # Sección para mostrar las mesas
        self.frame_lista_mesas = tk.Frame(self.ventana, bg='#fcfcfc')
        self.frame_lista_mesas.place(x=1000, y=40, width=700, height=500)
        
        self.lista_mesas = ttk.Treeview(self.frame_lista_mesas, columns=('Número', 'Capacidad', 'Ubicación'), show='headings')
        self.lista_mesas.heading('Número', text='Número de Mesa')
        self.lista_mesas.heading('Capacidad', text='Capacidad')
        self.lista_mesas.heading('Ubicación', text='Ubicación')
        self.lista_mesas.pack(fill=tk.BOTH, expand=True)
        
        self.ventana.mainloop()

    def agregar_mesa(self):
        numero = self.entry_numero_mesa.get()
        capacidad = self.entry_capacidad_mesa.get()
        ubicacion = self.entry_ubicacion_mesa.get()
        
        if numero and capacidad and ubicacion:
            self.lista_mesas.insert('', 'end', values=(numero, capacidad, ubicacion))
            self.entry_numero_mesa.delete(0, tk.END)
            self.entry_capacidad_mesa.delete(0, tk.END)
            self.entry_ubicacion_mesa.delete(0, tk.END)

    def borrar_mesa(self):
        selected_item = self.lista_mesas.selection()
        if selected_item:
            self.lista_mesas.delete(selected_item)

    def modificar_mesa(self):
        selected_item = self.lista_mesas.selection()
        if selected_item:
            numero = self.entry_numero_mesa.get()
            capacidad = self.entry_capacidad_mesa.get()
            ubicacion = self.entry_ubicacion_mesa.get()

            if numero and capacidad and ubicacion:
                self.lista_mesas.item(selected_item, values=(numero, capacidad, ubicacion))
                self.entry_numero_mesa.delete(0, tk.END)
                self.entry_capacidad_mesa.delete(0, tk.END)
                self.entry_ubicacion_mesa.delete(0, tk.END)



import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl

