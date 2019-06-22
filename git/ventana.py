# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 19:02:10 2019

@author: Oscar, Edgar, Fernando
"""
import math
import tkinter as tk
from tkinter import *

#Ventana principal
ventana=tk.Tk()
ventana.title("Cálculos")
ventana.geometry('380x300+500+200')
ventana.configure(background='dark turquoise')
l1=tk.Label(ventana,text="Escoja lo que desee calcular",bg="light blue", fg="black")
l1.pack(padx=5, pady=5,ipadx=5, ipady=5)


#Comandos que hará cada botón
def abrirventana1():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('300x300+500+200')
    win.configure(background='dark turquoise')
    def borrar():
        datoa.delete(0, tk.END)
        datob.delete(0, tk.END)
        datoc.delete(0, tk.END)
    def superficie():
        a=float(datoa.get())
        b=float(datob.get())
        c=float(datoc.get())
        s=(a+b+c)/2
        p=s*((s-a)*(s-b)*(s-c))
        if p<0:
            return var.set("La raíz cuadrada dio numeros imaginarios")
        else:
            superficie=float(math.sqrt(p))
            return var.set(superficie)
    e1=tk.Label(win,text="Ingrese los parámetros a, b y c",bg="light blue", fg="black")
    e1.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    datoa=tk.Entry(win, width="20")
    datoa.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    datob=tk.Entry(win, width="20")
    datob.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    datoc=tk.Entry(win, width="20")
    datoc.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    bing=tk.Button(win, text="Ingresar",fg="dark slate grey", bg="azure",width="10",command=superficie)
    bing.pack(side=tk.TOP)
    var=tk.StringVar()
    e2=tk.Label(win,textvariable=var,bg="slate gray", fg="black",padx=5, pady=5, width=50)
    e2.pack()
    bog=tk.Button(win, text="Borrar",fg="dark slate grey", bg="azure",width="10",command=borrar)
    bog.pack(side=tk.TOP)
    
def abrirventana2():
    ventana.withdraw()
    pop=tk.Toplevel()
    pop.geometry('300x300+500+200')
    pop.configure(background='dark turquoise')
    def borrar():
        coorx1.delete(0, tk.END)
        coorx2.delete(0, tk.END)
        coory1.delete(0, tk.END)
        coory2.delete(0, tk.END)
    def distancia():
        x1=float(coorx1.get())
        x2=float(coorx2.get())
        y1=float(coory1.get())
        y2=float(coory2.get())
        d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return var.set(d)
    f1=tk.Label(pop,text="Distancia: Ingrese las coordenadas X1, X2, Y1 y Y2",bg="light blue", fg="black")
    f1.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    coorx1=tk.Entry(pop, width="20")
    coorx1.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    coorx2=tk.Entry(pop, width="20")
    coorx2.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    coory1=tk.Entry(pop, width="20")
    coory1.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    coory2=tk.Entry(pop, width="20")
    coory2.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    bog=tk.Button(pop, text="Ingresar",fg="dark slate grey", bg="azure",width="10",command=distancia)
    bog.pack(side=tk.TOP)
    var=tk.StringVar()
    f2=tk.Label(pop,textvariable=var,bg="slate gray", fg="black",padx=5, pady=5, width=50)
    f2.pack()
    bog=tk.Button(pop, text="Borrar",fg="dark slate grey", bg="azure",width="10",command=borrar)
    bog.pack(side=tk.TOP)
    
def abrirventana3():
    ventana.withdraw()
    gag=tk.Toplevel()
    gag.geometry('300x300+500+200')
    gag.configure(background='dark turquoise')
    def borrar():
        coorx1.delete(0, tk.END)
        coorx2.delete(0, tk.END)
        coory1.delete(0, tk.END)
        coory2.delete(0, tk.END)
    def azimut():
        x1=float(coorx1.get())
        x2=float(coorx2.get())
        y1=float(coory1.get())
        y2=float(coory2.get())
        azi1 = math.atan(x2 - x1 / y2 - y1)
        azi2 = (math.degrees(azi1)*400) / 360
        return var.set(azi2)
    f1=tk.Label(gag,text="Azimut: Ingrese las coordenadas X1, X2, Y1 y Y2",bg="light blue", fg="black")
    f1.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    coorx1=tk.Entry(gag, width="20")
    coorx1.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    coorx2=tk.Entry(gag, width="20")
    coorx2.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    coory1=tk.Entry(gag, width="20")
    coory1.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    coory2=tk.Entry(gag, width="20")
    coory2.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)
    bog=tk.Button(gag, text="Ingresar",fg="dark slate grey", bg="azure",width="10",command=azimut)
    bog.pack(side=tk.TOP)
    var=tk.StringVar()
    f2=tk.Label(gag,textvariable=var,bg="slate gray", fg="black",padx=5, pady=5, width=50)
    f2.pack()
    bog=tk.Button(gag, text="Borrar",fg="dark slate grey", bg="azure",width="10",command=borrar)
    bog.pack(side=tk.TOP)


#Botones de superficie, distancia y azimut
bs=tk.Button(ventana, text="Superficie",fg="black", bg="rosy brown",width="10", command=abrirventana1)
bs.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)

bd=tk.Button(ventana, text="Distancia",fg="black",bg="rosy brown",width="10",command=abrirventana2)
bd.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)

ba=tk.Button(ventana, text="Azimut",fg="black",bg="rosy brown",width="10",command=abrirventana3)
ba.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)

bsal=tk.Button(ventana, text="Salir",fg="black",bg="rosy brown",width="10",command=ventana.destroy)
bsal.pack(padx=5, pady=5,ipadx=5, ipady=5, fill=tk.X)

ventana.mainloop()