# Creacion de un editor de texto
from tkinter import *
from tkinter import filedialog as FileDialog  #Para poder abrir un fichero
from io import open 

ruta = '' #La utilizaremos para almacenar la ruta del fichero

#Funciones
def nuevo():
    global ruta
    mensaje.set('Nuevo fichero')
    ruta = ''   #Tenemos que darle un valor vacio porque es un nuevo archivo
    texto.delete(1.0, 'end') #Borramos el texto al abrir el nuevo texto, y borramos del primer caracter hasta el final
    root.title('Mi editor') #Cambiamos el titulo

def abrir():
    global ruta
    mensaje.set('Abrir fichero')
    ruta = FileDialog.askopenfilename(
        initialdir='.',     #Initialdir = directorio inicial; '.' abre el directorio actual       
        filetype=(('Ficheros de texto', '*.txt'),), #Filetype = el tipo de fichero (ej .txt)
        title='Abrir un fichero de texto')
    
    if ruta != '':
        fichero = open(ruta, 'r') #Abre el fichero en modo lectura
        contenido = fichero.read() #Lee el contenido
        texto.delete(1.0, 'end') #Borramos el texto de antes
        texto.insert('insert', contenido) #Insertamos el texto 
        fichero.close() #Cerramos el fichero
        root.title(ruta + ' - Mi editor') #Cambiamos el titulo

def guardar():
    mensaje.set('Guardar fichero')
    #Para un fichero que ya existe
    if ruta != '':
        contenido = texto.get(1.0, 'end-1c') #Recuperamos el contenido menos el ultimo caracter (es un salto de linea) que vamos a guardar
        fichero = open(ruta, 'w+') #Abrimos en modo escrituras + lectura
        fichero.write(contenido) #Escribimos el contenido
        fichero.close() #Cerramos el fichero
        mensaje.set('El fichero se guardo correctamente')
    
    #Para un nuevo fichero que creo con un nuevo nombre
    else:
        guardar_como() #Llamo directo a la funcion de guardar como

def guardar_como():
    global ruta
    mensaje.set('Guardar fichero como')
    fichero = FileDialog.asksaveasfile( title='Guardar fichero', mode='w', defaultextension='.txt') #Abrimos un fichero en modo escrituta y extension en .txt
    if fichero is not None:
        ruta = fichero.name #Le damos a ruta el valor que tiene el fichero que acabamos de abrir
        contenido = texto.get(1.0, 'end-1c') #Recuperamos el contenido menos el ultimo caracter (es un salto de linea) que vamos a guardar
        fichero = open(ruta, 'w+') #Abrimos en modo escrituras + lectura
        fichero.write(contenido) #Escribimos el contenido
        fichero.close() #Cerramos el fichero
        mensaje.set('El fichero se guardo correctamente')
    else:
         mensaje.set('Guardar cancelado')
         ruta = ''

# Configutacion de la raiz
root = Tk()
root.title('Editor de texto') #Titulo

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Nuevo', command=nuevo)
filemenu.add_command(label='Abrir',command=abrir)
filemenu.add_command(label='Guardar', command=guardar)
filemenu.add_command(label='Guardar como', command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit) #Al tocar se cierra todo
menubar.add_cascade(menu=filemenu, label='Archivo') #Al tocar se abre para abajo 

# Caja de texto central
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(bd=0, padx=6, pady=4, font=('Consulas',12))

# Barra inferior
mensaje = StringVar() #Variable de texto
mensaje.set('Bienvenido al editor de texto')
monitor = Label(root, textvar=mensaje, justify='left') #Textvar es un variable que podemos ir modificando para cambiar el contenido de una label
monitor.pack(side='left')


root.config(menu=menubar)
# Finalmente bucle de la aplicacion
root.mainloop()