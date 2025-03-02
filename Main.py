from tkinter import*
import os
from tkinter import filedialog,messagebox
from pytubefix import YouTube
from resizeimage import resizeimage
from PIL import Image,ImageTk
from datetime import datetime
import requests
import time
# import AudioSeg
def time():
    now = datetime.now()
    now= now.strftime("%H%M%S")
    # print(now)
    return now
# print(formatted)
def selectlocation():
    filename = filedialog.askdirectory() 
    Broweslocation.config(text=filename)
    
    
    
root = Tk()
root.geometry("820x350+400+70")

root.title("Apurba Audio Downloader")
root.resizable(False,False)
Viewtitle=Label(root,text="Welcome to Apu Audio Downloder",font=("times new roman",40),bg='GREEN',fg="WHIte")
Viewtitle.place(x=0,y=0,relwidth=1)

ViewFream=Frame(root,bg='lightGREEN',bd=10,relief='ridge')
ViewFream.place(x=30,y=80,height=250,width=500)

Youtubeview=Frame(root,bg='lightGREEN',bd=10,relief='ridge')
Youtubeview.place(x=540,y=80,height=250,width=250)

def removePlaceholder(text):
    link=text
    # print(link)
    try:
        if len(text)>0:
            LPaste.config(text='')
            LPaste.place_configure(x=500)
            # print(link.get())
            y=YouTube(link)
            Title=y.title
            YouTubeTitle.config(text=Title,fg='green',font='bold')
            ImgUrl=y.thumbnail_url
            Img=requests.get(ImgUrl)
            
            f=open('Thumbnails.png','wb')
            f.write(Img.content)
            img= Image.open("Thumbnails.png")
            img=img.resize((150,150))
            image= ImageTk.PhotoImage(img)
            # new.save("Thumbnails"+'.png') 
            # image=PhotoImage(file="D:/program language/python/project/youtube video downloder/Thumbnails.png") 
            YouTubeimage.configure(image=image)
            YouTubeimage.image=image
            
        else:
            LPaste.config(text='Please Paste Your Link')
            LPaste.place_configure(x=100)   
    except:
        messagebox.showwarning('warning',"This Is Not a Link") 
        clearall() 
def clearall():
    # link.delete(0,'end')
    EPaste.delete(0,'end')
    os.remove("Thumbnails.png")
    Broweslocation.configure(text='')
    LPaste.configure(text='Please Paste Your Link')
    LPaste.place_configure(x=100) 
    YouTubeimage.config(image='')
    YouTubeTitle.config(text='No Title',fg='black',font='10')
    # print(filename)
link=StringVar()
EPaste=Entry(ViewFream,font=("times new roman",25),textvariable=link)
EPaste.place(x=30,y=10,width=420)
# youtube_1=YouTube(link.get())
EPaste.bind('<KeyRelease>',lambda e:removePlaceholder(EPaste.get()))

LPaste=Label(ViewFream,text='Please Paste Your Link',font=("times new roman",20),bg='white')
LPaste.place(x=100,y=12)
Paste=Button(ViewFream,text="Paste",font=("times new roman",18),command=lambda:Link())
Paste.place(x=400,y=10)
EPaste.bind('<Button-2>',lambda e:EPaste.focus())
def Link():
    EPaste.event_generate("<<Paste>>")
    link=root.clipboard_get()
    removePlaceholder(link)
   
#    print(link)   
   

Broweslocation=Label(ViewFream,font=("times new roman",20))
Broweslocation.place(x=50,y=100,width=300)
Location=Label(ViewFream,text='Please select your Position',font=("times new roman",20),background='lightgreen')
Location.place(x=50,y=55,width=300)

YouTubeimage=Label(Youtubeview,text='No Image')
YouTubeimage.place(x=15,y=10,width=200,height=160)

# title=YouTube(link.get())
# print(title.title)
YouTubeTitle=Label(Youtubeview,text='No Title',font="10")
YouTubeTitle.place(x=15,y=180,width=200,height=40)
filestore=Button(ViewFream,text="Browse",font=("times new roman",20),command=selectlocation)
filestore.place(x=370,y=90)
Audio=Button(ViewFream,text="Download Audio",font=("times new roman",18),command=lambda:audiodownload())
Audio.place(x=100,y=150)

Clear=Button(ViewFream,text="Clear",font=("times new roman",18),command=clearall)
Clear.place(x=320,y=150)
def audiodownload():
     now=time()
    #  print("hhh"+now)
    #  print(link.get())
     if link.get()=='':
        messagebox.showwarning('warning',"Please Fill All The Items")
     else:    
        # print(Broweslocation.cget("text"))
        location=Broweslocation.cget("text")

        if location=='':
            messagebox.showwarning('warning',"Please Select Your Position")

        else:
            try:
                # title=YouTube(link.get())
                # path =location+"/"+title.title+'.mp4'
                # # print(path)
                # file = os.path.isfile(path) 
                # # print(file)
                # if(file==False):
                #     print("hii")
                title=YouTube(link.get())
                stream=title.streams.get_by_itag(140)

                t=title.title[0:20]
            # print(t)
                stream.download(location+"/",t+now+".mp4")
                messagebox.showinfo("Download", "Download finished", parent=root)
                clearall()
                # else:
                #     messagebox.showwarning("Error", "This File Already exist")
            except:
                messagebox.showwarning("Error", "Somthing Internal Problem")



root.mainloop()
