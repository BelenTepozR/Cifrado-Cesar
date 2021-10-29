from tkinter import Entry, Tk, Label, Button,Text, messagebox
from tkinter.constants import END

from codificacion_de_cesar import CodigoCesar

class VentanaEjemplo:
    #inicializamos nuestras variables de entorno
    def __init__(self, ventana, codigo):
        self.master = ventana
        self.codigo = codigo
        ventana.geometry('700x320')
        ventana.resizable(width=False,height=False)
        ventana.title("Código de Cesar")
        ventana.configure(bg='azure')
        bgc = 'white'
        self.lbtexto_llano = Label(ventana, text="Texto LLano",width= 17, height=2)
        self.lbtexto_llano.config(fg="blue",bg='azure', font=("Verdana",13)) 
        self.lbtexto_llano.place(x=50,y=60)

        self.txttexto_llano = Text(ventana, width=50, height=3)
        self.txttexto_llano.config(fg="blue",bg=bgc, font=("Verdana",10)) 
        self.txttexto_llano.place(x=250,y=50)

        self.lbdesplazamientos = Label(ventana, text="Número de Dezplazamientos:",width= 30, height=2)
        self.lbdesplazamientos.config(fg="blue",bg='azure', font=("Verdana",11)) 
        self.lbdesplazamientos.place(x=50,y=120)

        self.txtdesplazamientos = Entry(ventana)
        self.txtdesplazamientos.config(fg="blue",bg=bgc, font=("Verdana",10)) 
        self.txtdesplazamientos.place(x=300,y=130,width=50,height=25)

        self.lbtexto_codificado = Label(ventana, text="Texto Codificado", width= 17, height=2)
        self.lbtexto_codificado.config(fg="blue",bg='azure', font=("Verdana",12)) 

        self.txttexto_codificado = Text(ventana, width=50, height=3)
        self.txttexto_codificado.config(fg="blue",bg=bgc, font=("Verdana",10)) 
        

        self.lbtexto_descodificado = Label(ventana, text="Texto Sin codificar",width= 17, height=2)
        self.lbtexto_descodificado.config(fg="blue",bg='azure', font=("Verdana",12)) 
        self.lbtexto_descodificado.place(x=50,y=360)

        self.txttexto_decodificado = Text(ventana, width=50, height=3)
        self.txttexto_decodificado.configure(state='disabled')
        self.txttexto_decodificado.config(fg="blue",bg=bgc, font=("Verdana",10)) 
        self.txttexto_decodificado.place(x=250,y=350)
        
        self.botonCodificar = Button(ventana, text="Codificar", command=self.codificar)
        self.botonCodificar.place(x=460,y=140,width=100, height=30)
        self.botonCodificar.config(fg="white",bg='blue', font=("Verdana",10)) 
        
        self.botonSalir = Button(ventana, text="Salir", command=ventana.quit)
        self.botonSalir.place(x=580,y=140,width=100, height=30)
        self.botonSalir.config(fg="white",bg='red', font=("Verdana",10)) 

        self.botonDecodificar = Button(ventana, text="Decodificar", command=self.decodificar)
        self.botonDecodificar.place(x=480,y=270,width=100, height=30)
        self.botonDecodificar.config(fg="white",bg='blue', font=("Verdana",10)) 

        self.botonLimpiar = Button(ventana, text="Limpiar", command=self.limpiar)
        self.botonLimpiar.place(x=280,y=450,width=100, height=30)
        self.botonLimpiar.config(fg="white",bg='blue', font=("Verdana",10)) 
        self.lbtexto_codificado.place(x=50,y=200)
        self.txttexto_codificado.place(x=250,y=190)
        self.txttexto_llano.focus()
    #Cuando se manda a codificar el texto que ingreso el usuario
    #se manda a llamar al metodo codificar
    def codificar(self):
        if(len(self.txttexto_llano.get("1.0",'end-1c')) > 0) &  (len(self.txtdesplazamientos.get()) > 0 ):     
            if (self.txtdesplazamientos.get().isnumeric()):
                self.txttexto_codificado.configure(state='normal')
                self.textoCodificado = self.codigo.codificar(int(self.txtdesplazamientos.get()),self.txttexto_llano.get("1.0",'end-1c'))
                self.txttexto_codificado.insert("1.0",self.textoCodificado )
                self.botonCodificar.configure(state="disabled")
            else:
                messagebox.showinfo(message="Ingrese un número en el Campo 'Número de Desplazamientos'", title="ADVERTENCIA")
        else:
            messagebox.showinfo(message="Complete todos los campos", title="ADVERTENCIA")

    def decodificar(self):
        if(len(self.txttexto_codificado.get("1.0",'end-1c')) > 0) &  (len(self.txtdesplazamientos.get()) > 0 ):     
            if (self.txtdesplazamientos.get().isnumeric()):
                self.master.resizable(width=True,height=True)
                self.master.geometry('700x500')
                self.master.resizable(width=False,height=False)
                self.txttexto_decodificado.configure(state='normal')
                self.textoDecodificado = self.codigo.decodificar(int(self.txtdesplazamientos.get()),self.txttexto_codificado.get("1.0",'end-1c'))
                self.txttexto_decodificado.insert("1.0", self.textoDecodificado)
                self.txttexto_decodificado.configure(state='disabled')
                self.botonDecodificar.configure(state="disabled")
            else:
                messagebox.showinfo(message="Ingrese un número en el Campo 'Número de Desplazamientos'", title="ADVERTENCIA")
        else:
            messagebox.showinfo(message="Complete todos los campos", title="ADVERTENCIA")

    #limpiuamos las cajas de texto
    def limpiar(self):
        self.master.resizable(width=True,height=True)
        self.master.geometry('700x320')
        self.master.resizable(width=False,height=False)
        self.txttexto_llano.delete("1.0",END)
        self.txttexto_decodificado.configure(state='normal')
        self.txttexto_codificado.configure(state='normal')
        self.txtdesplazamientos.delete(0,END)
        self.txttexto_decodificado.delete("1.0",END)
        self.txttexto_codificado.delete("1.0",END)
        self.txttexto_decodificado.configure(state='disabled')
        self.botonCodificar.configure(state="normal")
        self.botonDecodificar.configure(state="normal")
        self.txttexto_llano.focus()

def main():
    root = Tk()
    miCodigo = CodigoCesar()
    miVentana = VentanaEjemplo(root,miCodigo)
    
    root.mainloop()
if __name__ == '__main__':
    main()
