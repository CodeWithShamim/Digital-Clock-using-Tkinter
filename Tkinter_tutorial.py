from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('shamim')

'''
#Using image with tkinter...............................................................
my_image = ImageTk.PhotoImage(Image.open('icon1.jpg'))


label = Label(image=my_image)
label.pack()
 
button_quit = Button(root, text='End program', command=root.quit)
button_quit.pack()

#FrameLayout with tkinter.............................................................

frame = LabelFrame(root, text="This is a Frame", bg='red', padx=70, pady=70)
frame.pack()

button = Button(frame, text='button')
button.grid(row=0, column=0)

'''
#RadioButton with tkinter.............................................................
#root.geometry('500x500+10+10')
#label = Label(root, text='Hello shamim')
#label.pack()

'''
#Create new window using tkinter......................................................

root.geometry('500x500+350+100')
root.resizable(width=False, height=False)

def new_window():
    N_W = Toplevel()
    N_W.title('Hello shamim')
    N_W.geometry('300x300+10+50')
    N_W.resizable(False, False)

button = Button(root, text="Create new window", command=new_window)
button.pack()

'''

#Filedialog...(askopenfilename)........................................................
#import......

'''
from tkinter import filedialog

root.geometry('500x500+350+100')
root.resizable(width=False, height=False)

def new_window():

    N_W = Toplevel()
    N_W.title('Hello shamim')
    N_W.geometry('300x300+10+50')
  
    def fdb():
        global imgselect
        myFile = filedialog.askopenfilename(initialdir='C:', title="Open a File", 
        filetypes=(('jpg', '*.jpg'),
            ('All files', '*.*')
            ))
        imgselect = ImageTk.PhotoImage(Image.open(myFile))
        mylebel = Label(N_W, image=imgselect)
        mylebel.pack()

    button = Button(N_W, text="Open file", bg='yellow', command=fdb)
    button.pack()

    
    

button = Button(root, text="Create new window", bg='yellow', command=new_window)
button.pack()

'''
#Option menu.............................................................................

'''
root.geometry('500x500+350+100')
root.resizable(width=False, height=False)

var = StringVar()
var.set('Select')


def show():
    selected =var.get()
    if selected == 'Shamim':
        label = Label(root, text="You select Shamim item!!")
        label.pack()

    elif selected == 'Rezone':
        label = Label(root, text="You select Rezone item!!")
        label.pack()

    elif selected == 'Sahin':
        label = Label(root, text="You select Sahin item!!")
        label.pack()

    elif selected == 'Hasmot':
        label = Label(root, text="You select Hasmot item!!")
        label.pack()

    else:
        label = Label(root, text=selected)
        label.pack()

    

drop_menu = OptionMenu(root, var, 'Shamim', 'Rezone', 'Sahin', 'Hasmot', 'other')
drop_menu.pack()

button = Button(root, text="Show Result", command=show)
button.pack()


'''
#MessageBox............................................................................

'''
from tkinter import messagebox

root.geometry('500x500+100+100')
root.resizable(False, False)

def click():
    MessageBox = messagebox.showinfo("Hey", "How are you??")
    MessageBox = messagebox.showerror("Hey", "How are you??")
    MessageBox = messagebox.showwarning("Hey", "How are you??")
    MessageBox = messagebox.askquestion("Hey", "How are you??")
    MessageBox = messagebox.askokcancel("Hey", "How are you??")
    MessageBox = messagebox.askyesno("Hey", "How are you??")

button = Button(root, text='Click Now', command=click)
button.pack()


'''
#CheckBox..........................................................

'''
root.geometry('500x500+100+100')
root.resizable(False, False)

var = IntVar()

def result():
    label = Label(root, text=var.get())
    label.pack()


checkBox1 = Checkbutton(root, text='Male', variable=var, onvalue='on', offvalue='off')
checkBox1.pack()
checkBox2 = Checkbutton(root, text='Female', variable=var, onvalue='on', offvalue='off')
checkBox2.pack()


button = Button(root, text='Show result', command=result)
button.pack()

'''

root.mainloop()