from tkinter import *
import os


window = Tk()

window.title("Proyecto")
#window.geometry("500x500")
selected = IntVar()

rad1 = Radiobutton(window,text='IMAGEN', value=1, variable=selected)

rad2 = Radiobutton(window,text='VIDEO', value=2, variable=selected)

rad3 = Radiobutton(window,text='CAMARA', value=3, variable=selected)

os.system('python ejemplo.py')

def clicked():
   path = str("python Object_detection_image.py --ruta={}".format(entry2.get()))

   if (selected.get()==1):
      #window.destroy()
      print(path)
      os.system(path)
   if (selected.get()==2):
      #window.destroy()
      os.system('python Object_detection_video.py')
   if (selected.get()==3):
      #window.destroy()
      os.system('python Object_detection_webcam.py')






label2 = Label(window, text="RUTA")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(window)
entry2.grid(row=1, column=1, ipadx=100, pady=5)
entry2.config(justify="center")




btn = Button(window, text="PRUEBA", command=clicked)

lblInfo1 = Label(window, text="Detección de Placas", font="courier", bg="azure")
lblInfo1.grid(column=1, row=0, columnspan=2)

rad1.grid(column=0, row=2)

rad2.grid(column=1, row=2)

rad3.grid(column=2, row=2)

btn.grid(column=3, row=1)


#Label(window, image=image)



window.mainloop()