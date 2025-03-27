from tkinter import *
from tkinter import ttk
import pandas as pd
 
archivo1 = pd.read_csv("Sacramentorealestatetransactions.csv")
filtro = archivo1.query("city == 'SACRAMENTO' & type == 'Residential' & price <= 100000")
filtros = [
            "city == 'SACRAMENTO' & type == 'Residential' & price <= 100000",
            "beds >= 2 & type == 'Condo'",
            "baths == 1 & city == 'RIO LINDA'",
            "city == 'ELK GROVE' & sq__ft >= 1500",
            "sale_date == 'Wed May 21 00:00:00 EDT 2008' & sq__ft <= 2000 & city == 'SACRAMENTO'",
            "sale_date == 'Thu May 15 00:00:00 EDT 2008' & type == 'Condo'",
            "type == 'Multi-Family' & price <= 250000",
            "baths == 0 & price >= 150000",
            "city == 'ANTELOPE' & sale_date == 'Mon May 19 00:00:00 EDT 2008'",
            "beds >= 2 & baths >= 2 & price <= 150000",
          ]
datosFilt = [archivo1.query(filtro) for filtro in filtros]

root= Tk()

root.title("Inicio de sesión")
root.geometry("250x200")

name_var= StringVar()
passw_var= StringVar()

fichero = open("credenciales.txt")

#Lee las líneas del archivo de texto y le quita los saltos de línea
usuario = fichero.readline().strip()
clave = fichero.readline().strip()

def cerrar_sec(ventana):
    ventana.destroy()
    root.deiconify()

def ventana_secundaria():
    root.withdraw()
    v_sec = Toplevel()
    v_sec.title("Inicial")
    v_sec.geometry("600x550")
    v_secbtn_cerrar = Button(v_sec, text="Cerrar", command=lambda: cerrar_sec(v_sec))
    v_seclabel_casas = Label(v_sec, text="Datos de Casas")
    v_seclabel_casas.pack()
    for i, filtro in enumerate(filtros):
        v_seclabel = Label(v_sec, text=filtro)
        v_secbtn = Button(v_sec, text=f"Consulta {i+1}", command=lambda i=i: ventana_terciaria(i))
        v_seclabel.pack()
        v_secbtn.pack()
    v_secbtn_cerrar.pack()

def ventana_terciaria(num):
    v_tri = Toplevel()
    v_tri.title("Consultas")
    v_tri.geometry("600x550")
    columnas = list(datosFilt[num].columns)
    treeview = ttk.Treeview(v_tri, columns=columnas, show="headings")
    for col in columnas:
        treeview.heading(col, text=col)
    for _, fila in datosFilt[num].iterrows():
        treeview.insert("", "end", values=tuple(fila))
    treeview.pack(expand=TRUE, fill="both")

def verificar():
    nombre=name_var.get()
    password=passw_var.get()
    
    if usuario == nombre and clave == password:
        print("Bien")
        ventana_secundaria()
    else:
        print("Mal")
    
    name_var.set("")
    passw_var.set("")
    

name_label = Label(root, text = 'Nombre', font=('calibre',10, 'bold'))
name_entry = Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
passw_label = Label(root, text = 'Contraseña', font = ('calibre',10,'bold'))
passw_entry= Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'))
sub_btn= Button(root,text = 'Enviar', command = verificar)
 
name_label.pack()
name_entry.pack()
passw_label.pack()
passw_entry.pack()
sub_btn.pack()
 
root.mainloop()