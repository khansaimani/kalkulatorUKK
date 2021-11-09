from tkinter import*
import tkinter.font as font
import math

root = Tk()
root.title("Calculator")
root["bg"] = "#d1d1d1"
root.geometry("450x450")

myfont  = font.Font(size=20)

e = Entry(root,width=25,borderwidth=10)
e["font"] = myfont
e["bg"] = "white"
e.grid(row=0, columnspan=4, pady=20,padx=20)


def cetak(nilai):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(nilai))
def tambah():
    nomor_awal = e.get()
    global n_awal
    global mathematics
    mathematics = "penjumlahan"
    n_awal = float(nomor_awal)
    e.delete(0,END)
def kurang():
    nomor_awal = e.get()
    global n_awal
    global mathematics
    mathematics = "pengurangan"
    n_awal = float(nomor_awal)
    e.delete(0,END)
def bagi():
    nomor_awal = e.get()
    global n_awal
    global mathematics
    mathematics = "pembagian"
    n_awal = float(nomor_awal)
    e.delete(0,END)
def kali():
    nomor_awal = e.get()
    global n_awal
    global mathematics
    mathematics = "perkalian"
    n_awal = float(nomor_awal)
    e.delete(0,END)
def akar():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0,END)
    e.insert(0,math.sqrt(n_awal))
def sisabagi():
    nomor_awal = e.get()
    global n_awal
    global mathematics
    mathematics = "sisabagi"
    n_awal = int(nomor_awal)
    e.delete(0,END)

def hapus():
    e.delete(0,END)
def samadengan():
    nomor_akhir = e.get()
    e.delete(0,END)
    if mathematics == "penjumlahan":
        e.insert(0,n_awal + float(nomor_akhir))
    elif mathematics == "pengurangan":
        e.insert(0,n_awal - float(nomor_akhir))
    elif mathematics == "perkalian":
        e.insert(0,n_awal * float(nomor_akhir))
    elif mathematics == "pembagian":
        try:
            hitung = n_awal / float(nomor_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError:
            e.insert(0,"ERROR")
    elif mathematics == "sisabagi":
        e.insert(0,n_awal % float(nomor_akhir))
    
btn1  = Button(root,text="1",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(1))
btn2  = Button(root,text="2",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(2))
btn3  = Button(root,text="3",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(3))
btn4  = Button(root,text="4",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(4))
btn5  = Button(root,text="5",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(5))
btn6  = Button(root,text="6",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(6))
btn7  = Button(root,text="7",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(7))
btn8  = Button(root,text="8",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(8))
btn9  = Button(root,text="9",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(9))
btn0  = Button(root,text="0",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak(0))
koma  = Button(root,text=",",padx = 45,bg="#3d3d3d",fg="white", pady = 20,command=lambda:cetak("."))

plus     = Button(root,text="+",padx=45,pady=20,command=tambah)
akar     = Button(root,text="√",padx=45,pady=20,command=akar)
min      = Button(root,text="-",padx=45,pady=20,command=kurang)
times    = Button(root,text="x",padx=45,pady=20,command=kali)
dev      = Button(root,text=":",padx=45,pady=20,command=bagi)
delete   = Button(root,text="C",padx=45,pady=20,command=hapus)
sisabagi = Button(root,text="%",padx=45,pady=20,command=sisabagi)
equal    = Button(root,text="=",bg="orange",padx=100,pady=20,command=samadengan)

btn1.grid(row=4,column=0,pady=2)
btn2.grid(row=4,column=1,pady=2)
btn3.grid(row=4,column=2,pady=2)
btn4.grid(row=3,column=0,pady=2)
btn5.grid(row=3,column=1,pady=2)
btn6.grid(row=3,column=2,pady=2)
btn7.grid(row=2,column=0,pady=2)
btn8.grid(row=2,column=1,pady=2)
btn9.grid(row=2,column=2,pady=2)
btn0.grid(row=5,column=0,pady=2)
koma.grid(row=5,column=1,pady=2)

plus.grid(row=4,column=3,pady=2)
min.grid(row=3,column=3,pady=2)
dev.grid(row=1,column=3,pady=2)
times.grid(row=2,column=3,pady=2)
delete.grid(row=1,column=0,pady=2)
akar.grid(row=1,column=1,pady=2)
sisabagi.grid(row=1,column=2,pady=2)
equal.grid(row=5,column=2,pady=2,columnspan=10)

root.mainloop()