#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def openChatWindow():

   
    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("500x350")
    window.configure(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectlabel = Label(window, text= "Select Song", bg = 'LightSkyBlue',font = ("Calibri",0))
    selectlabel.place(x=10, y=8)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    refresh=Button(window,text="Refresh",bd=1, font = ("Calibri",10))
    refresh.place(x=435,y=160)

    PlayButton=Button(window,text="Play",bd=1,width=10,bg = 'SkyBlue' ,font = ("Calibri",10))
    PlayButton.place(x=30,y=200)

    Stop=Button(window,text="Stop",bd=1,width=10,bg = 'SkyBlue' ,font = ("Calibri",10))
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",bd=1,width=10,bg = 'SkyBlue', font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download=Button(window,text="Download",bd=1,width=10,bg = 'SkyBlue', font = ("Calibri",10))
    Download.place(x=200,y=250)

    infolabel = Label(window, text= "", bg = 'blue',font = ("Calibri",8))
    infolabel.place(x=4, y=280)
  
  
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    openChatWindow()

setup()
