import tkinter as tk
from tkinter import ttk
from tkinter import *
from tinydb import TinyDB, Query
import csv, operator
from tkinter import messagebox
from tkinter.font import Font
from os import listdir
from PIL import ImageTk, Image
import cv2
import imutils
import numpy as np
import os
import BDD

class UI(tk.Frame):
    """Docstring."""

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Aqui colocariamos los widgets."""
        self.parent.title("Diccionarios")
        self.parent.configure(bg='black')

        image = cv2.imread(filename="imagenes/portada.png")
        image = imutils.resize(image, height=500)
        imageToShow = imutils.resize(image, width=500)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)
        lblInputImage = Label()
        lblInputImage.configure(image=img)
        lblInputImage.image = img
        lblInputImage.place(x=0,y=0)
        lblInputImage.config(relief="flat", highlightbackground="black")

        scrollbar = ttk.Scrollbar(orient=tk.VERTICAL)
        lista_dics = tk.Listbox(yscrollcommand=scrollbar.set)
        lista_archivos = listdir("bdds")
        for archivo in lista_archivos:
            a = archivo.replace(".csv", "")
            lista_dics.insert(tk.END, a)
        lista_dics.pack(side=RIGHT, fill=BOTH)
        lista_dics.config(justify=LEFT,fg="#ffffff", bg="#131c46", selectbackground="#3c4c8f", font=Font(family="Arial", size=12), width=22, relief="flat", highlightbackground="black")

        bded = TinyDB("Diccionario.json")
        bded.drop_tables()

        def Diccionario_elec():
            items = lista_dics.curselection()  # esto es el indice, osea nos dice cual numero de texto seleccionamos
            archivo_dic = "bdds/" + lista_dics.get(ACTIVE) + ".csv"  # esto nos dice cual es el texto
            BDD.crear(archivo_dic, bded)

        def on_selection(event):
            Diccionario_elec()

        lista_dics.bind('<Double-1>', on_selection)


if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("700x500")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
