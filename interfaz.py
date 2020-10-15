import Proyecto

sintomas_en_enfermedades = []

from tkinter import *
from tkinter import messagebox	

def agregarPudricion():
	global sintomas_en_enfermedades
	sintomas_en_enfermedades.append("pudricion")
	messagebox.showinfo(title = "Info", message = "El sintoma pudricion ha sido agregado")
	return

def agregarAmarillamiento():
	global sintomas_en_enfermedades
	sintomas_en_enfermedades.append(" amarillamiento")
	messagebox.showinfo(title = "Info", message = "El sintoma amarillamiento ha sido agregado")
	return

def agregarmalesclerocio():
	global sintomas_en_enfermedades
	sintomas_en_enfermedades.append("mal de esclerocio")
	messagebox.showinfo(title = "Info", message = "El sintoma mal de esclerocio ha sido agregado")
	return

def agregarManchaangular():
	global sintomas_en_enfermedades
	sintomas_en_enfermedades.append("mancha angular")
	messagebox.showinfo(title = "Info", message = "El sintoma mancha angular ha sido agregado")
	return

def agregarNematodos():
	global sintomas_en_enfermedades
	sintomas_en_enfermedades.append("nematodos falsa mancha angular")
	messagebox.showinfo(title = "Info", message = "El sintoma nematodos falsa mancha angular ha sido agregado")
	return

def agregarantracnosis():
	global sintomas_en_enfermedades
	sintomas.append("antracnosis")
	messagebox.showinfo(title = "Info", message = "El antracnosis ha sido agregado")
	return

sintomas_en_plagas = []

def agregaraRoya():
	global sintomas_en_plagas
	sintomas.append("Roya")
	messagebox.showinfo(title = "Info", message = "La plaga Roya ha sido agregado")
	return


def agregaraMildeopolvoso():
	global sintomas_en_plagas
	sintomas.append("Mildeo Polvoso")
	messagebox.showinfo(title = "Info", message = "La plaga de Mildeo Polvoso ha sido agregado")
	return

def agregarMoscablanca():
	global sintomas_en_plagas
	sintomas.append("Mosca blanca")
	messagebox.showinfo(title = "Info", message = "la plaga de la Mosca blanca ha sido agregado")
	return	


def enviarSintomas():
	global sintomas_en_enfermedades
	global sintomas_en_plagas
	global ventana
	if len(sintomas_en_enfermedades) != 0:
	         len(sintomas_en_plagas) != 0:
		ventanaEnfermedad = Tk()
		ventanaEnfermedad.geometry("600x300+0+0")
		ventanaEnfermedad.configure(background = 'gray60')
		ventanaEnfermedad.config(background = 'gray60')

		messagebox.showinfo(title = "Diagnostico", message = "La enfermedad mas notoria en el frijol  es: \n" + Proyecto.identificacionSintoma(sintomas))
		ventana.destroy()
		

		def close():
			sintomas_en_enfermedades = []
			ventanaEnfermedad.destroy()
		enfermedad = Proyecto.identificacionSintoma(sintomas)

		labelEnfermedad = Label(ventanaEnfermedad, text =  "ENFERMEDAD:    " + enfermedad, foreground="#F50743", background = "gray60", font = "Helvetica 16 bold").place(x = 116, y = 8)
		labelSintomas_en_enfermedad = Label(ventanaEnfermedad, text = "SINTOMAS ENFERMEDAD:    " + Proyecto.returnSintomas(enfermedad), background = "gray60", font = "Helvetica 12 bold").place(x = 5, y = 60)
		labelcondicion_enfermedad = Label(ventanaEnfermedad, text = "CONDICION ENFERMEDAD:    " + Proyecto.returnCondicion(enfermedad), background = "gray60", font = "Helvetica 12 bold").place(x = 5, y = 120)
		labelmanejo_en_enfermedad = Label(ventanaEnfermedad, text = "MANEJO EN ENFERMEDAD:    " + Proyecto.returnManejo(enfermedad), background = "gray60", font = "Helvetica 12 bold").place(x = 5, y = 240)
		btnVolver = Button(ventanaEnfermedad, text = "Salir", width = 5, height = 3, command = close,foreground="#F50643", background = "white", font = "Helvetica 12 bold").place(x = 510, y = 220)
		ventanaEnfermedad.mainloop()
	else:
		messagebox.showerror("Validacion", "Debe seleccionar algun sintoma")
	return

ventana  = Tk()
ventana.geometry("800x500+0+0")
ventana.title("SELECCIONE LOS SINTOMAS")

'''''##############################################################################################################

    
   ws = ventana.winfo_screenwidth() 
   hs = ventana.winfo_screenheight() 

       
def sintomas_en_enfermedades():
    
    enfermedades_del_frijol = tk.Tk()
    

    
    ws = sintomas_en_enfermedades.winfo_screenwidth() 
    hs = sintomas_en_enfermedades.winfo_screenheight() 

    #MENSAJE    
    var = tk.StringVar(manejo_en_enfermedades)                   
    mensaje = tk.Label(manejo_en_enfermedades, textvariable=var, font = "Courier10Pitch")
    mensaje.pack()

    
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    

def sintomas_en_plagas():
    root.withdraw()
    diagnostico = tk.Tk()
    w = 500 
    h = 300 

   
    ws = sintomas_en_plagas.winfo_screenwidth() 
    hs = sintomas_en_plagas.winfo_screenheight() 

#MENSAJE    
    var = tk.StringVar(manejo_en_plagas)                   
    mensaje = tk.Label(manejo_en_plagas, textvariable=var, font = "Courier10Pitch")
    mensaje.pack()

    var.set("hola")
    
    ws = dano_en_enfermedades.winfo_screenwidth() 
    hs = dano_en_enfermedades.winfo_screenheight() 

    #MENSAJE    
    
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)


#ENTRADA DE TEXTO
    e = tk.Entry(enfermedades_del_frijol)
    e.pack()
#ACCIONAR CON ENTER    
    enfermedades_del_frijol.bind('<Return>', lambda x:read_str(e.get()))
#BOTON
    b1 = tk.Button(enfermedades_del_frijol, text="REGRESAR", command =lambda:regresar(enfermedades_del_frijol) ,font = "Courier10Pitch")
    b1.pack()
    
    enfermedades_del_frijol.geometry('%dx%d+%d+%d' % (w, h, x, y))

root = tk.Tk()

photo = Image.open("ojo.jpg")
photo = photo.resize((350, 100), Image.ANTIALIAS)
photon = ImageTk.PhotoImage(photo)
    


