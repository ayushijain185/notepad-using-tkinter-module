from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo
from tkinter.TextArea import TextArea
import os

def newe():
    global file
    root.title("Untitled-Notepad")
    file=None
    textarea.delete(1.0,END)

def opene():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("ALL FILES","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def savee():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def save_as():
    print("rtryyt")


def exite():
    root.destroy()

def cute():
    TextArea.event_generate(("<crtl+x>"))


def copee():
    TextArea.event_generate(("<crtl+c>"))

def pastee():
    TextArea.event_generate(("<crtl+v>"))

def undoe():
    TextArea.event_generate(("<crtl+x>"))

def deletee():
    TextArea.event_generate(("<delete>"))


def statusbare():
    status = StringVar()
    status.set("100% | windows | UTF-8 ")
    bar = Label(root, textvariable=status, borderwidth=7, relief=SUNKEN, anchor="se", padx=5, pady=5)
    bar.pack(side=BOTTOM, fill=X)

def aboute():
    showinfo("Notepad", "created by Ayushi on 18 march")

root = Tk()
root.geometry("600x400")
# root.minsize("200", "200")
root.title("Untitled-Notepad")

textarea = Text(root, font="lucida 13")
file = None
textarea.pack(expand=True, fill=BOTH)

# root.wm_iconify(1.)

minubar = Menu(root)
m = Menu(minubar, tearoff=0)
m.add_command(label="New", command=newe)
m.add_command(label="Open", command=opene)
m.add_command(label="Save", command=savee)
m.add_command(label="Save As", command=save_as)
m.add_separator()
m.add_command(label="Exit", command=exite)
minubar.add_cascade(label="File", menu=m)

edite = Menu(minubar, tearoff=0)
edite.add_command(label="Undo", command=undoe)
edite.add_separator()
edite.add_command(label="Cut", command=cute)
edite.add_command(label="Copy", command=copee)
edite.add_command(label="Paste", command=pastee)
edite.add_command(label="Delete", command=deletee)
edite.add_separator()
edite.add_command(label="Staus bar", command=statusbare)
minubar.add_cascade(label="Edit", menu=edite)

about = Menu(minubar, tearoff=0)
minubar.add_cascade(label="about", menu=about , command=aboute)
root.config(menu=minubar)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)


root.mainloop()
