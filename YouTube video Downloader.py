from pytube import YouTube
from tkinter import *


root=Tk()
root.geometry("600x550")
root.title("Youtube_Downloader")
root.config(bg="#0d7ca8")
logo=PhotoImage(file="youtube_logo.png")
root.iconphoto(False,logo)


#heading
Label(root,text="YouTube Video Downloader",font="sansserif 22 bold",bg="black",fg="white").pack(padx=15,pady=35)

#Detail label
v_link=StringVar()
mp4_Path=StringVar()
Label(root,text="Enter Video Link Here",font="cursive 10 bold").place(x=25,y=125)
Label(root,text="Enter Mp4 Path Here",font="cursive 10 bold").place(x=25,y=150)

#entry
vlink_entry=Entry(root,width=45,font=20,textvariable=v_link).place(x=175,y=125)
mp4_entry=Entry(root,width=45,font=20,textvariable=mp4_Path).place(x=175,y=150)

#download function
def v_download():
    link=v_link.get()
    yt_link=YouTube(link)
    mp4=mp4_Path.get()
    my_video=yt_link.streams.get_highest_resolution()
    my_video.download(mp4)

    with open("file.txt","a")as f:
        f.write(yt_link.title+"\n")
        
Button(root,text="Download",font="cursive 20 bold",fg="white",bg="black",command=v_download).place(x=200,y=250)



root.mainloop()
