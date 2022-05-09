from tkinter import *
from tkinter import messagebox
from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20', fg='blue').pack()
video_link = StringVar()
path=StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15').place(x= 160 , y = 60)
video_link_enter = Entry(root, width = 70,textvariable = video_link).place(x = 32, y = 90)
Label(root, text = 'Choose a path:', font = 'arial 15').place(x= 160 , y = 120)
path_enter = Entry(root, width = 70,textvariable = path).place(x = 32, y = 150)
def Downloader():     
    url =YouTube(str(video_link.get()))
    video = url.streams.first()
    video.download(str(path.get()))
    messagebox.showinfo('success','Video downloaded successfully')
Button(root,text = 'Click here to download', font = 'arial 15' ,bg = 'blue', padx = 2, command = Downloader).place(x=120 ,y = 220)
root.mainloop() 

