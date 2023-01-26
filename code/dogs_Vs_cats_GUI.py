#!/home/mrpinformcc/anaconda3/bin/python

#####################################################################################################################################################
 #
 # [Author]:(WASCAL CCI, 2021)  BOUBAKAR Zourkalaini
 # [Date]: Fri Oct 7, 2021 
 # [Goal]: Modelling Project (User interface)
 # [Version]: 4.0 (last version)
 # [Execution]: /bin/python
 #
 #######################################################################################################################################################
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

#load the trained model to classify the images

from keras.models import load_model
model = load_model('cats_Vs_dogs_model.h5')


#dictionary to label all dataset classes.

classes = { 
    0:'Cat',
    1:'Dog'
}


#initialise GUI

top=tk.Tk()

#root = tk.Tk()
logo = tk.PhotoImage(file="wascal_logo.png")
w1 = tk.Label(top, image=logo).pack(side="top")


top.geometry('800x600')
top.title('Cats and Dogs Classification ')
top.configure(background='#FFFFFF')
label=Label(top,background='#CCCCCC', font=('Times',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((150,150))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = ((model.predict(image) > 0.5).astype("int32"))
    sign = classes[pred[0][0]]
    label.configure(background='#FFFFFF', font=('Times',20,'bold'),foreground='#FF0000',text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
    command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#0000FF', foreground='#FFFFFF',
    font=('Times',15,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
                            (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,
  padx=10,pady=5)

upload.configure(background='#0000FF', foreground='#FFFFFF',
    font=('Times',15,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="WASCAL ICC Batch 2 - BOUBAKAR Zourkalaini",pady=20, font=('Times',20,'bold'))

heading.configure(background='#FFFFFF', foreground='#000080')
heading.pack()
top.mainloop()