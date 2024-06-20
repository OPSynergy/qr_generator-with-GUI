import tkinter as tk
import qrcode
from tkinter import PhotoImage

root = tk.Tk()
root.title("QR_CODE Generator By OP")

root.configure(bg="black")

tl = tk.Label(root,text="QR_CODE By OP", font=("Helvetica" , 30 , "bold" ),fg="#00FF00",bg="black")
tl.pack(pady=20)

bc = {'fg':'#00FF00','bg':'black','activeforeground':'#00FF00','activeforeground':'black','width':25}

label = tk.Label(root , text="Paste the link to Create QR : ",font=('Helvetica',14),fg="#00FF00",bg="black")
label.pack(padx=10,pady=10)

tb = tk.Entry(root)
tb.pack(padx=12,pady=12)

def create_QR():

    qr = qrcode.QRCode()

    data = tb.get()

    qr.add_data(data)

    qr.make(fit = True)

    img = qr.make_image(fill_color = '#00FF00' , back_color = 'black')

    img.save('1.png')

    photo = PhotoImage(file='1.png')

    pl = tk.Label(root, image = photo , bg = 'black')

    pl.image = photo

    pl.pack()


al = tk.Button(root, text="Create QR : ",command=create_QR)
al.pack(padx=15,pady=15)

root.mainloop()