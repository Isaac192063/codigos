from tkinter import Label, Canvas, Button, Frame, Entry, TRUE, BOTH, END, Tk, PhotoImage
from tkinter import ttk
from tkinter import messagebox


def switch_range(select):
    cods = {
        "kΩ":'1000',
        'MΩ':'1000000',
        'GΩ':'1000000000',
        'Ω':'1'
    }
    return cods[select]

# pyinstaller --onefile --noconsole exp.py
class Ventana:
    def __init__(self, master):
        self.frame = Frame(master, bg='#202020')
        self.inp = Entry(self.frame, font=('helvetica', 12))
        self.lbl_valor = Label(self.frame, text="ingrese valor: ", font=('helvetica',11), bg='#202020', fg='white')
        self.lbl_pre = Label(self.frame, text="seleccione prefijo: ", font=('helvetica',11), bg='#202020', fg='white')
        self.lbl_tol= Label(self.frame, text="seleccione tolerancia: ", font=('helvetica',11), bg='#202020', fg='white')
        self.valor_tolerancia = "valor minimo: 0\n valor comercial: 0\nvalor maximo: 0"
        self.btn = Button(self.frame, text="calcular", font=('helvetica',12), command=self.funcion)
        self.lbl_Resul = Label(self.frame, text=self.valor_tolerancia, font=('helvetica', 11))
        self.opciones = ['kΩ', 'MΩ', 'GΩ', 'Ω']
        self.list = ttk.Combobox(self.frame, values=self.opciones, width=5, state="readonly",font=('helvetica',13))
        self.list.set('Ω')
        self.tolerancia = ttk.Combobox(self.frame, values=['5%', '10%'], width=5, state="readonly",font=('helvetica',13))
        self.canvas = Canvas(self.frame,width=300, height=200, bg='white')
        self.tolerancia.set('5%')
        self.cod = ["black", "#7F2F2F", "red", "#FF5900", "#FBFF00", "green", "blue", "#BD00FF", "gray", "white"]
        for i in range(4):
            self.frame.rowconfigure(i, weight=1)  # Primera fila
            self.frame.columnconfigure(i, weight=1)  # Primera columna
        self.frame.pack(expand=TRUE, fill=BOTH)

        self.lbl_valor.grid(row=0, column=0, sticky='e', padx=5)
        self.inp.grid(ipadx=2, ipady=6, row=0, column=1)

        self.lbl_pre.grid(row=1, column=0, sticky='e', padx=5)
        self.list.grid(row=1, column=1, sticky='w')

        self.lbl_tol.grid(row=2, column=0, sticky='e', padx=5)
        self.tolerancia.grid(row=2, column=1, sticky='w')

        self.btn.grid(row=3, column=0, columnspan=2)

        self.canvas.grid(row=4, column=0, sticky='w',padx=5,pady=5)

        self.lbl_Resul.grid(row=4, column=1, sticky='we', columnspan=2, pady=5)
        self.create_poligon('white', 'white', 'white', 'white')
    
    def create_poligon(self, c1, c2, c3, c4):

        print(f'{c1} y {c2} y {c3} y {c4}')
        color = '#9DA3FF'
        self.canvas.create_rectangle(90.87,146.44, 208.57,55.47, fill=color, outline=color)
        self.canvas.create_oval(4.3,44.3, 115.7,155.7, fill=color, outline=color)
        self.canvas.create_oval(184.3,44.3, 295.7,155.7, fill=color, outline=color)

        self.canvas.create_polygon(
           30.46,147.3,
            30.46,52.7,
            45.79,45,
            45.79,155,
            fill=c1
        )
        self.canvas.create_polygon(
           71.37,154.6,
            86.71,148.96,
            86.71,51.04,
            71.37,45.4,
            fill=c2
        )
        self.canvas.create_polygon(
           112.32,146.44,
            127.85,146.44,
            127.85,55.46,
            112.32,55.46,
            fill=c3
        )
        self.canvas.create_polygon(
           229.83,154.83,
            245.37,155.51,
            245.38,44.49,
            229.83,45.17,
            fill=c4
        )

    def funcion(self):
        if not self.validators(self.inp.get()): 
            messagebox.showinfo('Alerta', 'ingrese correctamente el valor')
            self.inp.delete(0, END) 
        else: 
            colores = self.calcular_colors()
            # label para porcentaje de tolereancia
            seleccion = self.list.get()
            data = float(self.inp.get())*int(switch_range(seleccion))

            c4 = 0
            if self.tolerancia.get() == '5%':
                c4 = 0.05
            else:
                c4 = 0.10

            min = data - data*c4
            max = data + data*c4

            self.valor_tolerancia = f"valor minimo: {str(min)}\n valor comercial: {str(data)}\nvalor maximo: {max}"
            self.lbl_Resul.config(text=self.valor_tolerancia) 
            self.create_poligon(colores[0], colores[1], colores[2], colores[3])
            # self.lbl_Resul.pack()



    def busc(self,n):
        for i, data in enumerate(self.cod):
            if int(n) == i:
                return data
            
    def validators(self, cad):
        if cad.strip() == "":
            return False
            
        if '.' in cad and self.list.get() != 'Ω':
            parts = cad.split('.')
            if  parts[0].isdigit() and parts[1].isdigit():
                return True
            return False
        
        if cad.isdigit():
            a =cad[2:len(cad)]
            for i in a:
                if i!='0':
                    return False
            return True
    
    def calcular_colors(self):
        valorIngresado = self.inp.get()
        seleccion = self.list.get()

        mul = int(switch_range(seleccion))
        con = 0
        c3 = ''
        c1 = ''
        c2 = ''

  
        if '.' in self.inp.get():
            valorIngresado = str(float(valorIngresado)*mul)
            con = len(valorIngresado)-4
        else:
            valorIngresado = str(int(valorIngresado)*mul)
            con = len(valorIngresado)-2
        s = ''
        if len(valorIngresado) == 1:
            c1= 'black'
            c2 = self.busc(valorIngresado)
            c3 = 'black'
        else:
            if con>=1:
                s = ''.join('0' for i in range(con))
            print(s)
            s = '1'+s
            c1 = self.busc(valorIngresado[0])
            c2 = self.busc(valorIngresado[1])
            c3 = self.cod[(len(s)-1)]

        tol = self.tolerancia.get()
        c4 = ''
        if tol == '5%':
            c4 = '#D4AF37'
        else:
            c4 = '#C0C0C0'

        return [c1, c2,c3,c4]

# def centrar_ventana(ventana):
#     ventana.update_idletasks()
#     ancho_ventana = ventana.winfo_width()
#     altura_ventana = ventana.winfo_height()
#     x = (ventana.winfo_screenwidth() - ancho_ventana) // 2
#     y = (ventana.winfo_screenheight() - altura_ventana) // 2
#     ventana.geometry(f"{ancho_ventana}x{altura_ventana}+{x}+{y}")
        
root = Tk()
root.title('calcular colores de una resistencia')
root.geometry("510x520")
# icono = PhotoImage(file='res.png')
# iconoGrande = PhotoImage(file='resGrande.png')
# root.iconphoto(False,icono)
root.resizable(width=False, height=False)

# root.call('wm', 'iconphoto', root._w, icono)

# centrar_ventana(root)
aplicacion = Ventana(root)
root.mainloop()