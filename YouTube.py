from tkinter import *
from pytube import YouTube
#Configuring Tkinter
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("350x100")
root.columnconfigure(0,weight=1)
#Add the desired Youtube video link in the "Youtube Link" space
ytdlabel = Label(root,text="YouTube Link",font=("Helvetica",15))
ytdlabel.grid()

link = StringVar()
ytEntry = Entry(root,width=50,textvariable=link)
ytEntry.grid()

#This function downloads the video in highest resolution possible
def Download():
    url= YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
#Download button
ytbutton = Button(root,width=10,bg="grey",fg="white",text="Download",command= Download)
ytbutton.grid()


root.mainloop()
