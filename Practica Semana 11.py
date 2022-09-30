#Gabriel Eduardo Henriquez Gonzalez
#Salvador Mauricio Chavarria Carranza
from tkinter import Label,Button,filedialog,Tk,messagebox
from PIL import Image,ImageTk,ImageFilter


class carga():

    def __init__(self):
        self.archivo=""

    def cargarmeto(self):
        self.archivo = filedialog.askopenfilename()
        imagen2 = Image.open(self.archivo)
        imagen2resiz = imagen2.resize((200,200),Image.Resampling.LANCZOS)
        render2 = ImageTk.PhotoImage(imagen2resiz)
        lbl1.configure(image=render2)
        lbl1.image = render2


    def blanco(self):
        if self.archivo !="":
            imagen4 = Image.open(self.archivo)
            imagenbn = imagen4.convert("L")
            imagenbnresiz = imagenbn.resize((200,200),Image.Resampling.LANCZOS)
            render4 = ImageTk.PhotoImage(imagenbnresiz)
            lbl1.configure(image=render4)
            lbl1.image = render4
            imagenbn.save("blancoynegro.jpg")
            messagebox.showinfo("Imagen","Se aplico el efecto de blanco y negro")
        else:
            messagebox.showerror("Imagen","Se necesita cargar la imagen")


    def desenfocar(self):
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            imagendes = imagen3.filter(ImageFilter.BLUR)
            imagenbnresiz = imagendes.resize((200,200),Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(imagenbnresiz)
            lbl1.configure(image=render3)
            lbl1.image = render3
            imagendes.save("desenfoque.jpg")
            messagebox.showinfo("Imagen","Se aplico el efecto de desenfoque")
        else:
            messagebox.showerror("Imagen","Se necesita cargar la imagen")

    def contorno(self): 
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            imagencon = imagen3.filter(ImageFilter.CONTOUR)
            imagenbnresiz = imagencon.resize((200,200),Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(imagenbnresiz)
            lbl1.configure(image=render3)
            lbl1.image = render3
            imagencon.save("contorno.jpg")
            messagebox.showinfo("Imagen","Se aplico el efecto de contorno")
        else:
            messagebox.showerror("Imagen","Se necesita cargar la imagen")

    def resal(self):
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            imagenresal = imagen3.filter(ImageFilter.EMBOSS)
            imagenbnresiz = imagenresal.resize((200,200),Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(imagenbnresiz)
            lbl1.configure(image=render3)
            lbl1.image = render3
            imagenresal.save("resaltar.jpg")
            messagebox.showinfo("Imagen","Se aplico el efecto de resaltar")
        else:
            messagebox.showerror("Imagen","Se necesita cargar la imagen")

ven = Tk()
ven.title("Visualizador de Imagenes")
ven.geometry('550x500')
ven.resizable(0,0)
lbl1 = Label(ven,text="Imagen: ",bg = "blue")
lbl1.place(x= 40,y=40, width=300,height=300)

claseone = carga()
boton = Button(ven,text="Cargar Imagen",command= claseone.cargarmeto)
boton.place(x=360,y=50,width=150,height=40)
botonnegro = Button(ven,text="Blanco/Negro",command=claseone.blanco)
botonnegro.place(x= 40, y= 400,width=100, height=40)
botondese = Button(ven,text="Desenfocar",command=claseone.desenfocar)
botondese.place(x= 150, y= 400,width=100, height=40)
botoncon = Button(ven,text="Contorno",command=claseone.contorno)
botoncon.place(x= 260, y= 400,width=100, height=40)
botonres = Button(ven,text="Resaltar",command=claseone.resal)
botonres.place(x= 370, y= 400,width=100, height=40)
ven.mainloop()