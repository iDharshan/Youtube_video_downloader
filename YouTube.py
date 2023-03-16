from tkinter import *
from pytube import YouTube

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("350x100")
root.columnconfigure(0,weight=1)

ytdlabel = Label(root,text="YouTube Link",font=("Helvetica",15))
ytdlabel.grid()

link = StringVar()
ytEntry = Entry(root,width=50,textvariable=link)
ytEntry.grid()

def Download():
    url= YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()

ytbutton = Button(root,width=10,bg="grey",fg="white",text="Download",command= Download)
ytbutton.grid()


root.mainloop()