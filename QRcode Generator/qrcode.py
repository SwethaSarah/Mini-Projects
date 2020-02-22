import pyqrcode
import tkinter
from pyqrcode import QRCode

def view_qr():
 d1=name.get()
 d2=manufacturer.get()
 d3=price.get()
 data=d1+' '+d2+' '+d3 
 code = pyqrcode.create(data)
 filename='qr.svg'
 code.svg(filename,scale=8)
 

top = tkinter.Tk()
top.title('QRCode Generator')
top.configure(bg='black')
top.geometry('400x400')
label1=tkinter.Label(text='Enter product name:',fg='white',bg='black')
label2=tkinter.Label(text='Enter Manufacturer:',fg='white',bg='black')
label3=tkinter.Label(text='Enter price:',fg='white',bg='black')
name=tkinter.Entry()
manufacturer=tkinter.Entry()
price=tkinter.Entry()
label1.grid(row=1,column=1)
label2.grid(row=2,column=1)
label3.grid(row=3,column=1)
name.grid(row=1,column=2)
manufacturer.grid(row=2,column=2)
price.grid(row=3,column=2)
button=tkinter.Button(text='Generate QRCODE',command=view_qr)
button.grid(row=4,column=1)
top.mainloop()
