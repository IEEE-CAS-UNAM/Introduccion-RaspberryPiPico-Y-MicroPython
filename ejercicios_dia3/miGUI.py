from tkinter import Tk, Scale, Label, Entry, Button, font
from tkinter.constants import COMMAND

import serial

ventana = Tk()

ventana.title("Control de motor a pasos")

#ventana.geometry("400x300")

ventana.iconbitmap(r"D:\52556\Downloads\ejercicios_dia3\cas.ico")

ventana.config(bg = "#3498db")#azul

ventana.resizable(0,0)

grande = "Arial 14"
mediana = "Arial 12"
chica = "Arial 10"

def conectar():
    if cajaTextoCom.get() != "":
        try:
            puerto = "COM" + cajaTextoCom.get()
            serial.Serial(puerto, 9600)
            etiqueta2["text"] = "Conectado"
            etiqueta2["bg"] = "#2ecc71"
            serial.Serial(puerto, 9600).write("u\n\r".encode("ascii"))
            mostrarWidgets()
        except serial.serialutil.SerialException:
            etiqueta2["text"] = "No se encuentra el puerto COM ingresado"
            etiqueta2["bg"] = "#e74c3c"
    else:
        etiqueta2["text"] = "No haz ingresado un valor"
        etiqueta2["bg"] = "#f1c40f"

def ocultarWidgets():
    etiqueta3.grid_forget()
    scl.grid_forget()
    etiqueta4.grid_forget()
    cajaGrados.grid_forget()
    botonConfirmar.grid_forget()

def mostrarWidgets():
    etiqueta3.grid(row=2, column=0, columnspan=3, padx=3, pady=3)
    scl.grid(row=3, column=0, columnspan=3, padx=3, pady=3)
    etiqueta4.grid(row=4, column=0, padx=3,pady=3)
    cajaGrados.grid(row=4, column=1, padx=3, pady=3)
    botonConfirmar.grid(row=4, column=2, padx=3, pady=3)

def cerrarPuerto():
    if cajaTextoCom.get() != "":
        puerto = "COM" + cajaTextoCom.get()
        serial.Serial(puerto, 9600).close()
    ventana.destroy()

def enviar():
    if cajaGrados.get() !="":
        grados = cajaGrados.get()+"\n\r"
        puerto = "COM" + cajaTextoCom.get()
        serial.Serial(puerto, 9600).write(grados.encode("ascii"))
        scl.set(int(grados))
        cajaGrados.delete("0", "end")
    else:
        grados = str(scl.get()) + "\n\r"
        puerto = "COM" + cajaTextoCom.get()
        serial.Serial(puerto, 9600).write(grados.encode("ascii"))
    

etiqueta1 = Label(ventana, text= "Ingresa el puerto COM: ", bg = "#3498db", font=grande)
etiqueta1.grid(row=0, column=0, padx=3, pady=3)

cajaTextoCom = Entry(ventana, width=3, font=grande)
cajaTextoCom.grid(row=0,column=1, padx=3, pady=3)

botonConectar = Button(ventana, text="Conectar", font=mediana, command = conectar)
botonConectar.grid(row=0, column=2, padx=3, pady=3)

etiqueta2 = Label(ventana, text="...", bg="#3498db",font=chica)
etiqueta2.grid(row=1, column=0, columnspan=3, padx=3, pady=3)

etiqueta3 = Label(ventana, text="Posición en grados", bg="#3498db", font= grande)
etiqueta3.grid(row=2, column=0, columnspan=3, padx=3, pady=3)

scl = Scale(ventana, from_=0, to=360, length=300, resolution=1, orient="horizontal", bg="#3498db",troughcolor="#ecf0f1", activebackground="#2c3e50", highlightbackground="#3498db", font=grande)
scl.grid(row=3, column=0, columnspan=3, padx=3, pady=3)

etiqueta4 = Label(ventana, text="Ingresa la posición angular:", bg="#3498db", font= grande)
etiqueta4.grid(row=4, column=0, padx=3,pady=3)

cajaGrados = Entry(ventana, width=3, font=grande)
cajaGrados.grid(row=4, column=1, padx=3, pady=3)

botonConfirmar = Button(ventana, text="Enviar", font=mediana, command=enviar)
botonConfirmar.grid(row=4, column=2, padx=3, pady=3)

ventana.protocol("WM_DELETE_WINDOW", cerrarPuerto)

ocultarWidgets()


ventana.mainloop()