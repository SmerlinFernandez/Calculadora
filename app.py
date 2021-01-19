import tkinter as tk
from tkinter.constants import END

class Aplicacion(tk.Frame):

    def __init__(self,master = None):

        self.master = master
        super().__init__(self.master)
        self.pack()
        self.crear_Widgets()
        self.resulActual = 0
        self.operacion = ""
        

    def colocar_Numero(self,numero):
        self.pnumero.set(self.pantalla.get() + numero)
    
    def punto(self):
        if "." not in self.pnumero.get():
            self.pnumero.set(self.pantalla.get() + '.')
        else:
            pass

    def sumar(self):
        self.resulActual += float(self.pantalla.get())
        self.pantalla.delete(0,END)
        self.operacion = "Suma"
    
    def restar(self):
        self.resulActual = 0
        self.resulActual = self.resulActual + float(self.pantalla.get()) 
        self.pantalla.delete(0,END)
        self.operacion = "Resta"
        
    def dividir(self):
        self.resulActual = self.resulActual + float(self.pantalla.get())
        self.pantalla.delete(0,END)
        self.operacion = "Division"

    def multiplicar(self):
        self.resulActual = self.resulActual + float(self.pantalla.get())
        self.pantalla.delete(0,END)
        self.operacion = "Multiplicacion"

    def porcentaje(self):
        self.resulActual = self.resulActual + float(self.pantalla.get())
        self.pantalla.delete(0,END)
        self.operacion = "Porcentaje"
        
    def resul_Igual(self):

        if self.operacion == 'Resta':
            self.pnumero.set(self.resulActual - float(self.pantalla.get()))
            self.operacion = ""
        elif self.operacion == 'Suma':
            self.pnumero.set(self.resulActual + float(self.pantalla.get()))
            self.operacion = ""
        elif self.operacion == 'Division':
            self.pnumero.set(self.resulActual / float(self.pantalla.get()))
            self.operacion = ""
        elif self.operacion == "Multiplicacion":
            self.pnumero.set(self.resulActual * float(self.pantalla.get()))
            self.operacion = ""
        elif self.operacion == "Porcentaje":
            self.pnumero.set(100 * self.resulActual / float(self.pantalla.get()))
            self.operacion = ""    
        
        self.resulActual = 0
    
    def borrar(self):
        self.pnumero.set('')

    def eliminar(self):
        
        self.pantalla.delete(len(self.pantalla.get()) - 1)


    def crear_Widgets(self):

        self.pnumero = tk.StringVar()
        self.pantalla = tk.Entry(self,justify="right", bg="grey",textvariable=self.pnumero)
        self.pantalla.grid(row = 0, column = 0, columnspan=5)

        self.botonC = tk.Button(self,text = 'C',width=3,command= lambda: self.borrar())
        self.botonC.grid(row=1,column=0, sticky='w')

        self.botonDiv = tk.Button(self,text = '÷',width=3, command= lambda: self.dividir())
        self.botonDiv.grid(row=1,column=1)

        self.botonMul= tk.Button(self,text='*',width=3, command= lambda: self.multiplicar())
        self.botonMul.grid(row=1,column =2)

        self.botonDel= tk.Button(self,text='Del',width=3,command= lambda : self.eliminar())
        self.botonDel.grid(row=1,column =3)

        self.boton7= tk.Button(self,text='7',width=3,command= lambda: self.colocar_Numero("7"))
        self.boton7.grid(row=2,column =0)

        self.boton8= tk.Button(self,text='8',width=3, command= lambda: self.colocar_Numero('8'))
        self.boton8.grid(row=2,column =1)

        self.boton9= tk.Button(self,text='9',width=3,command=lambda: self.colocar_Numero('9'))
        self.boton9.grid(row=2,column =2)

        self.botonMenos= tk.Button(self,text='-',width=3,command= lambda: self.restar())
        self.botonMenos.grid(row=2,column =3)

        self.boton4= tk.Button(self,text='4',width=3,command=lambda: self.colocar_Numero('4'))
        self.boton4.grid(row=3,column =0)

        self.boton5= tk.Button(self,text='5',width=3,command=lambda: self.colocar_Numero('5'))
        self.boton5.grid(row=3,column =1)

        self.boton6= tk.Button(self,text='6',width=3,command=lambda: self.colocar_Numero('6'))
        self.boton6.grid(row=3,column =2)

        self.botonMas= tk.Button(self,text='+',width=3,command= lambda: self.sumar())
        self.botonMas.grid(row=3,column =3)

        self.boton1= tk.Button(self,text='1',width=3,command=lambda: self.colocar_Numero('1'))
        self.boton1.grid(row=4,column =0)

        self.boton2= tk.Button(self,text='2',width=3,command=lambda: self.colocar_Numero('2'))
        self.boton2.grid(row=4,column =1)

        self.boton3= tk.Button(self,text='3',width=3,command=lambda: self.colocar_Numero('3'))
        self.boton3.grid(row=4,column =2)

        self.botonIgual= tk.Button(self,text='=',width=3, command= lambda: self.resul_Igual())
        self.botonIgual.grid(row=4,column=3)

        self.botonPorc= tk.Button(self,text='%',width=3,command= lambda: self.porcentaje())
        self.botonPorc.grid(row=5,column=0)

        self.boton0= tk.Button(self,text='0',width=3,command=lambda: self.colocar_Numero('0'))
        self.boton0.grid(row=5,column=1)

        self.botonPunto= tk.Button(self,text='.',width=3,command=lambda: self.punto())
        self.botonPunto.grid(row=5,column=2)

root = tk.Tk()

app = Aplicacion(master=root)
app.mainloop()