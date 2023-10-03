import tkinter as tk

#Creacion de ventana
ventana = tk.Tk()
ventana.title("Hospital Naval Puerto Belgrano")
ventana.geometry("400x400")
ventana.resizable(0,0)

#Creacion de texto
Label = tk.Label(ventana, text = "Cuidados Intensivos" )
Label.pack()
Label.config(font=("Arial", 25))

Label2 = tk.Label(ventana, text = "Cálculo de PaO2/FiO2")
Label2.pack()
Label2.config(font=("Arial",19))

Label3 = tk.Label(ventana, text = "PO2 mmHg")
Label3.pack()
Label3.config(font=("Arial",19))

#Entry: 
Entry = tk.Entry(ventana)
Entry.pack()

Label4 = tk.Label(ventana, text = "FiO2(%)")
Label4.pack()
Label4.config(font=("Arial",19))

Entry2 = tk.Entry(ventana)
Entry2.pack()

#Place
LabelH5 = tk.Label(ventana, text= "Resultado")
LabelH5.config(font=("Arial",20))
LabelH5.place(x=50, y=200)

EntryH5 = tk.Entry(ventana)
EntryH5.place(x=150,y=200)



ventana.mainloop()
