from tkinter import*
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import*
from PIL import Image , ImageTk
import imutils
import cv2
import face_recognition
from resizeimage import resizeimage
import numpy as np
import pyttsx3
import mysql.connector
import os
from tkcalendar import*
import webbrowser
import datetime

# from tkPDFViewer import tkPDFViewer as pdf

con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
mycursor=con.cursor()
face_cap=cv2.CascadeClassifier("C:/Users/apurb/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")


root=Tk()
root.geometry("1000x650+200+50")
root.title("Face Verification Management System")
root.resizable(False,False)
def Home():
    class Marquee(tk.Canvas):
        def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30,font=5):
            super().__init__(parent, borderwidth=borderwidth, relief=relief)

            self.fps = fps
            
            # start by drawing the text off screen, then asking the canvas
            # how much space we need. Use that to compute the initial size
            # of the canvas. 
            text = self.create_text(100, -1000, text=text, anchor="w", tags=("text",),font=font)
            (x0, y0, x1, y1) = self.bbox("text")
            width = (x1 - x0) + (2*margin) + (2*borderwidth)
            height = (y1 - y0) + (2*margin) + (2*borderwidth)
            self.configure(width=width, height=height)

            # start the animation
            self.animate()

        def animate(self):
            (x0, y0, x1, y1) = self.bbox("text")
            if x1 < 0 or y0 < 0:
                # everything is off the screen; reset the X
                # to be just past the right margin
                x0 = self.winfo_width()
                y0 = int(self.winfo_height()/2)
                self.coords("text", x0, y0)
            else:
                self.move("text", -2, 0)

            # do again in a few milliseconds
            self.after_id = self.after(int(1000/self.fps), self.animate) 
           
    # global notice
    try:
        con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
        mycursor=con.cursor()
        mycursor.execute("select Date,leaves_date from admin_notification where notices_id=7000")
        for notice_id in mycursor:
            start_date=notice_id[0]
            end_date=notice_id[1]

        if start_date!=None and end_date!=None:
            datelist=str(start_date)
            a=datelist[0]+datelist[1]+datelist[2]+datelist[3]
            b=datelist[5]+datelist[6]
            c=datelist[8]+datelist[9]
            startdate = datetime.date(int(a),int(b),int(c))

            datelist1=str(end_date)
            a1=datelist1[0]+datelist1[1]+datelist1[2]+datelist1[3]
            b1=datelist1[5]+datelist1[6]
            c1=datelist1[8]+datelist1[9]
            enddate = datetime.date(int(a1),int(b1),int(c1))

            current_date = datetime.date.today()

            if startdate <= current_date <= enddate:
                mycursor.execute("select notice from admin_notification where notices_id=7000")
                for notice_id in mycursor:
                    notice_details=notice_id[0]
                # print(notice_details)
                global n
                n=notice_details
                marquee = Marquee(root, text=n, borderwidth=5,font='15', relief="sunken")
                marquee.place(x=150,y=70,width=850,height=50)
        else:    
            marquee = Marquee(root, text='', borderwidth=5,font='15', relief="sunken")
            marquee.place(x=150,y=70,width=850,height=50)    
            
                
    except Exception as e:
        messagebox.showerror("Database error: ",f"{e}")  
                 
   
    
           
    NOTICETITLE=Label(root,text="Notice:-",font='Arial 25 bold') 
    NOTICETITLE.place(y=70)       
    
    
    
    # marquee.config(text='')
    Title=Label(root,text="Welcome To our Verification Management System",font='Arial 25 bold',bg='GREEN',fg="WHIte",pady=20,padx=200)
    Title.place(height=70,width=1000)
    user=Button(root,text="User",font='Calibri_Light 25 bold',padx=10,pady=10,activebackground="lightblue",cursor='hand2',command=lambda:UserPage())
    user.place(x=330,y=120)
    admin=Button(root,text="Admin",font='Calibri_Light 25 bold',padx=10,pady=10,activebackground="lightblue",cursor='hand2',command=lambda:AdminPage())
    admin.place(x=500,y=120)
    
    # User Part Start--------------------------------------------------------------------------------
    
    def UserPage():
        Title.destroy()
        admin.destroy()
        user.destroy()
        NOTICETITLE.destroy()
        marquee.destroy()
        
        known_face_encoding=[]
        known_faces_names=[]
        known_faces_id=[]
        first_count=0
        old_ids=0
        def video_stream(first_count,old_ids):
            # video=None
            # con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
            # umycursor=con.cursor()
            
            global video
            video= cv2.VideoCapture(0)
            # address="http://192.168.0.105:4747/video"
            # video.open(address)

            mycursor.execute("select * from user")
            for x in mycursor:
                rec_data=x[2]
                data_ids=x[0]
                name_id=x[1]
                with open('images.jpg','wb') as f:
                    f.write(rec_data)
                # f=open('images.jpg','wb')
                # f.write(rec_data)
                image=face_recognition.load_image_file("images.jpg")
                encoding=face_recognition.face_encodings(image)[0]
                known_face_encoding.append(encoding)
                known_faces_names.append(name_id)
                known_faces_id.append(data_ids)
            Turn_on(first_count,old_ids)

        
        def Turn_on(first_count,old_ids):
            # con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
            # umycursor=con.cursor()
            global video
            face_locations=[]
            face_encodings=[]
            ret,frame=video.read()
            
            
            if ret == True:
                
                live_video.place(x=45,y=65,width=450,height=350)
                
                
                frame = imutils.resize(frame,width=600)
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                faces = face_cap.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30,30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )

                for(x,y,w,h) in faces:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                        
                small_frame=cv2.resize(frame,(0,0),fx=0.25, fy=0.25)
                rgb_small_frame=small_frame[:,:,::-1]

                face_locations=face_recognition.face_locations(rgb_small_frame)
                face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
                for face_encoding in face_encodings:

                    matches=face_recognition.compare_faces(known_face_encoding, face_encoding)
                    name=" "
                    ids=" "
                    face_distance=face_recognition.face_distance(known_face_encoding, face_encoding)
                    best_match_index=np.argmin(face_distance)
                    if matches[best_match_index]:
                        name=known_faces_names[best_match_index]
                        ids=known_faces_id[best_match_index]
                        
                        if old_ids==ids:
                            first_count=first_count+1
                            if first_count==4:
                                first_count=0
                            # images retrive from data bases
                                # print(ids)
                                # print(name)
                                global ID
                                global NAME
                                ID=ids
                                NAME=name
                                mycursor.execute(f"select picture,department from user where user_id='{ids}'")
                                for z in mycursor:
                                    y=z[0]
                                    f=open('images.jpg','wb')
                                    f.write(y)
                                    user_dept=z[1]
                                    # present update
                                user_id_list=[]
                                mycursor.execute("select user_id from present where date=curdate()")
                                for users_id in mycursor:
                                    users_ids=users_id[0]
                                    user_id_list.append(users_ids)

                                if ids in user_id_list:
                                    mycursor.execute(f"select present_id from present where user_id={ids} and name='{name}' and Date=curdate()")
                                    for i in mycursor:
                                        presents_ids=i[0]
                                    mycursor.execute(f"update present set departure_time=curtime() where present_id='{presents_ids}'")
                                    con.commit()
                                else:
                                    mycursor.execute(f"insert into present(user_id,name,Date,arrival_time,department) values({ids},'{name}',curdate(),curtime(),'{user_dept}')")
                                    con.commit()
                                f=pyttsx3.init()
                                sound_name=name
                                f.say(f"Wellcome{sound_name}")
                                f.runAndWait()
                                
                                
                                img= Image.open("images.jpg")
                                img=img.resize((200,200)) 
                                img=ImageTk.PhotoImage(img) 
                                database_image.configure(image=img)
                                database_image.image=img
                                wellcomemsg.config(text=f"-:Wellcome{name}:-")
                                wellcomemsg.after(3000,lambda:wellcomemsg.config(text=''))
                                Name_msg.config(text=name,bg='lightyellow',fg="black")
                                Id_msg.config(text=ids)
                                if ids!='':
                                    gotouserview.config(state='normal')
                        else:
                            first_count=0
                        old_ids=ids
                    else:
                        first_count=0
                        f=pyttsx3.init()
                        f.say("you are unknown persion")
                        f.runAndWait()
                        Name_msg.config(text='',bg='gray')
                        Id_msg.config(text='No Id') 
                        msg.config(text='')     
                        database_image.config(image='')
                        gotouserview.config(state='disabled')
            
                        
            img = Image.fromarray(frame)
            image = ImageTk.PhotoImage(image=img)
            live_video.configure(image=image)
            live_video.image = image
            live_video.after(10, lambda:Turn_on(first_count,old_ids))
        def clear():
            Name_msg.config(text='',bg='gray')
            Id_msg.config(text='') 
            # msg.config(text='')     
            database_image.config(image='') 
            gotouserview.config(state='disabled') 


        #main frame============================================================== 
        title=Label(root,text="Welcome To Face Recognizer",font=("times new roman",40),bg='GREEN',fg="WHIte")
        title.place(x=0,y=0,relwidth=1)
        live_Frame=Frame(root,bd=2,relief="raised",bg="blue")
        live_Frame.place(x=50,y=130,width=550,height=450)
        live_titel=Label(live_Frame,text="Face Recognizer",font=("times new roman",20),bg='lightpink',fg="black")
        live_titel.place(x=0,y=0,relwidth=1)
        #live video============================================================
                    
        live_video=Label(live_Frame,bd=2,relief=RAISED)
        live_video.place(x=45,y=65,width=450,height=350)


        #show image================================
        Your_data=Frame(root,bd=2,relief="raised",bg="blue")
        Your_data.place(x=650,y=130,width=300,height=450)
        Your_data1=Label(Your_data,text="Face Recognizer",font=("times new roman",20),bg='lightpink',fg="black")
        Your_data1.place(x=0,y=0,relwidth=1)
        database_image=Label(Your_data,text="No Img",font=('times new roman',15),bg='gray',fg='black',bd=1,relief=RAISED)
        database_image.place(x=25,y=45,width=250,height=250)

        database_id=Label(Your_data,text="Your Id",font=('times new roman',15),bg='White',fg='black',bd=1,relief=RAISED)
        database_id.place(x=10,y=310,width=100,height=20)

        Id_msg=Label(Your_data,font=("times new roman",15),bg='lightyellow',fg="black")
        Id_msg.place(x=130,y=310,width=150,height=20)

        
        Name_msg=Label(Your_data,font=("times new roman",15),bg='gray')
        Name_msg.place(x=35,y=270,height=20)

        
        msg=Label(Your_data,text='Already Attend',font=("times new roman",20),bg='blue',fg="Lightgreen")
        msg.place(x=50,y=335)

        wellcomemsg=Label(root,font=("times new roman",28,"bold"),fg="green")
        wellcomemsg.place(x=255,y=590)
        #button================================================================
        data_clear=Button(Your_data,text="Clear All Data",font=("times new roman",18,"bold"),command=clear,bg='lightgray',fg="black",cursor='hand2')
        data_clear.place(x=70,y=385,width=160,height=50)               
        Backtomain=Button(root,text="back",font=("times new roman",18,"bold"),cursor='hand2',command=lambda:Back_to_Home_Page())
        Backtomain.place(x=20,y=590)
        gotouserview=Button(root,text="View",font=("times new roman",18,"bold"),state='disabled',cursor='hand2',command=lambda:User_View_page())
        gotouserview.place(x=900,y=590)
        video_stream(first_count,old_ids)
        
        
        # Back to Home Page
        def Back_to_Home_Page():
            global video
            live_video.config(image='')
            video.release()
            title.destroy()
            live_Frame.destroy()
            live_titel.destroy()
            live_video.destroy()
            Your_data.destroy()
            Your_data1.destroy()
            database_image.destroy

            database_id.destroy()
            Id_msg.destroy()

            Name_msg.destroy()
            msg.destroy()

            wellcomemsg.destroy()
            data_clear.destroy()               
            Backtomain.destroy()
            gotouserview.destroy()
            Home()
        # User_View_page----------------------------------------------------------------
        def User_View_page():
            global video
            live_video.config(image='')
            video.release()
            title.destroy()
            live_Frame.destroy()
            live_titel.destroy()
            live_video.destroy()
            Your_data.destroy()
            Your_data1.destroy()
            database_image.destroy

            database_id.destroy()
            Id_msg.destroy()

            Name_msg.destroy()
            msg.destroy()

            wellcomemsg.destroy()
            data_clear.destroy()               
            Backtomain.destroy()
            gotouserview.destroy()
            
            def USER_VIEW():
                con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                uvmycursor=con.cursor()
                
                ids=ID
                UserTitel=Label(root,text="Your All Data",font=("times new roman",50),bg='GREEN',fg="WHIte")
                UserTitel.pack(fill=X)
                UserdataViewe=Frame(root,bd=5,relief='raised',bg='lightblue')
                UserdataViewe.place(x=400,y=180,width=550,height=450)       
                UserimgViewe=Frame(root,bd=5,relief='raised',bg='lightblue')
                UserimgViewe.place(x=50,y=180,width=300,height=450) 
                user_id=int(ids)
                try:
                    uvmycursor.execute(f"select user.name,user.designation,user.department,leaves.total_leave,leaves.leave_taken,leaves.remaining_leave from user INNER JOIN leaves ON user.user_id=leaves.user_id where user.user_id={ids}")
                    for st_id in uvmycursor:
                        user_name=st_id[0]
                        user_designation=st_id[1]
                        user_department=st_id[2]
                        user_leave=st_id[3]
                        user_leave_taken=st_id[4]
                        user_remaining_leave=st_id[5]
                    # print(user_name)
                    # print(ids)
                    # print(user_designation)
                    # print(user_department)
                    # print(user_leave)
                    # print(user_leave_taken)
                    # print(user_remaining_leave)

                #Create Userdata Pannel start 

                    Database_UserName=Label(UserdataViewe,text="Your Name:-",font=("times new roman",25),bg='lightblue')
                    Database_UserName.place(x=15,y=15)
                    DATABASE_USERID=Label(UserdataViewe,text="Your Id:-",font=("times new roman",25),bg='lightblue')
                    DATABASE_USERID.place(x=15,y=60)
                    DATABASE_DESIGNATION=Label(UserdataViewe,text="Your Designation:-",font=("times new roman",25),bg='lightblue')
                    DATABASE_DESIGNATION.place(x=15,y=105)
                    DATABASE_DEPARTMENE=Label(UserdataViewe,text="Your Depertment:-",font=("times new roman",25),bg='lightblue')
                    DATABASE_DEPARTMENE.place(x=15,y=155)
                    TotalLeave1=Label(UserdataViewe,text="Total Leave:-",font=("times new roman",25),bg='lightblue')
                    TotalLeave1.place(x=15,y=205)
                    LeaveTaken1=Label(UserdataViewe,text="Leave Taken:-",font=("times new roman",25),bg='lightblue')
                    LeaveTaken1.place(x=15,y=255)
                    ApproveLeave1=Label(UserdataViewe,text="Approve Leave:-",font=("times new roman",25),bg='lightblue')
                    ApproveLeave1.place(x=15,y=305)
                    RemainingLeave1=Label(UserdataViewe,text="Remaining Leave:-",font=("times new roman",25),bg='lightblue')
                    RemainingLeave1.place(x=15,y=355)
                    #             # msg
                    # total="   "
                    global Name
                    Name =user_name
                    global UID
                    UID=ids
                    TDatabase_UserName=Label(UserdataViewe,text=user_name,bd=4,relief='groove',font=("times new roman",15))
                    TDatabase_UserName.place(x=275,y=15,width=250,height='40')
                    TDATABASE_USERID=Label(UserdataViewe,text=ids,bd=4,relief='groove',font=("times new roman",15))
                    TDATABASE_USERID.place(x=275,y=60,width=250,height='40')
                    TDATABASE_DESIGNATION=Label(UserdataViewe,text=user_designation,bd=4,relief='groove',font=("times new roman",15))
                    TDATABASE_DESIGNATION.place(x=275,y=105,width=250,height='40')
                    TDATABASE_DEPARTMENE=Label(UserdataViewe,text=user_department,bd=4,relief='groove',font=("times new roman",15))
                    TDATABASE_DEPARTMENE.place(x=275,y=155,width=250,height='40')
                    TTotalLeave1=Label(UserdataViewe,bd=4,text=user_leave,relief='groove',font=("times new roman",15))
                    TTotalLeave1.place(x=275,y=205,width=250,height='40')
                    if user_leave_taken ==None:
                        user_leave_taken = "0"
                    else:    
                        user_leave_taken = user_leave_taken
                    TLeaveTaken1=Label(UserdataViewe,bd=4,text=user_leave_taken,relief='groove',font=("times new roman",15))
                    TLeaveTaken1.place(x=275,y=255,width=250,height='40')
                    if user_remaining_leave ==None:
                        user_remaining_leave = "0"
                    else:    
                        user_remaining_leave = user_remaining_leave
                    TRemainingLeave1=Label(UserdataViewe,bd=4,text=user_remaining_leave,relief='groove',font=("times new roman",15))
                    TRemainingLeave1.place(x=275,y=355,width=250,height='40')
                except Exception as e:
                    messagebox.showwarning("Database Error",f"{e}")
                try:
                    con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                    mcursor=con.cursor()
                    mcursor.execute(f"select approved from user INNER JOIN approve ON user.user_id=approve.user_id where user.user_id={ids} AND approve.Date=curdate()")
                    for st_ids in mcursor:
                        user_approve_leave=st_ids[0]
                    TApproveLeave1=Label(UserdataViewe,text=user_approve_leave,bd=4,relief='groove',font=("times new roman",15))
                    TApproveLeave1.place(x=275,y=305,width=250,height='40')
                except Exception as e:
                    TApproveLeave1=Label(UserdataViewe,text='No Report',bd=4,relief='groove',font=("times new roman",15))
                    TApproveLeave1.place(x=275,y=305,width=250,height='40')
                

                # dataview complete

                # change Photo start
                def user_change_photo():
                    
                                UserTitel.destroy()
                                UserdataViewe.destroy()     
                                UserimgViewe.destroy()
                                Database_UserName.destroy()
                                DATABASE_USERID.destroy()
                                DATABASE_DESIGNATION.destroy()
                                DATABASE_DEPARTMENE.destroy()
                                TotalLeave1.destroy()
                                LeaveTaken1.destroy()
                                ApproveLeave1.destroy()
                                RemainingLeave1.destroy()
                                TDatabase_UserName.destroy()
                                TDATABASE_USERID.destroy()
                                TDATABASE_DESIGNATION.destroy()
                                TDATABASE_DEPARTMENE.destroy()
                                TTotalLeave1.destroy()
                                TLeaveTaken1.destroy()
                                TApproveLeave1.destroy()
                                TRemainingLeave1.destroy()
                                IDatabase_UserImg.destroy()
                                User_Image_change.destroy()
                                gotomain.destroy()
                                notice.destroy()
                                User_change_Title=Label(root,text="Chanage Photo",font=("times new roman",50),bg='GREEN',fg="WHIte")
                                User_change_Title.pack(fill=X)
                                                
                                changeFrame=Frame(root,bd=5,relief='raised',bg='lightblue')
                                changeFrame.place(x=80,y=175,width=850,height=430) 

                                # For Old Photo Fream
                                Old_Frame=Frame(changeFrame)
                                Old_Frame.place(x=50,y=50,width=300,height=350)

                                Old_title=Label(Old_Frame,font='30',text='Old Photo',bg='lightpink')
                                Old_title.pack(fill=X)
                                con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                chmycursor=con.cursor()
                                chmycursor.execute(f"select picture from user  where user_id='{user_id}'")
                                for details in chmycursor:
                                    user_pic=details[0]
                                    with open('images.jpg','wb') as f:
                                        f.write(user_pic)
                                        img=Image.open("images.jpg")
                                        img=img.resize((200,200))
                                        img=ImageTk.PhotoImage(img)
                                old_Photo=Label(Old_Frame,image=img,bg='lightgray')
                                old_Photo.image=img
                                old_Photo.place(x=25,y=50,width=250,height=250)

                                # For New Photo Fream
                                New_Frame=Frame(changeFrame)
                                New_Frame.place(x=500,y=50,width=300,height=350)

                                New_title=Label(New_Frame,font='30',text='New Photo',bg='lightpink')
                                New_title.pack(fill=X)

                                New_Photo=Label(New_Frame,text='No Photo',bg='lightgray')
                                New_Photo.place(x=25,y=50,width=250,height=250)

                                Path=Label(New_Frame)
                                Path.pack()
                                
                                
                                # Button 
                                Back_User_View=Button(root,text='Back',activebackground='lightblue',font='20',command=lambda: Back__TO_Userview())
                                Back_User_View.place(x=20,y=125,width=100,height=50)

                                choose_pic=Button(changeFrame,text='Choose Photo',activebackground='lightblue',font=20,command=lambda:selectPic())
                                choose_pic.place(x=355,y=100)

                                Submit_pic=Button(changeFrame,text='Submit Photo',activebackground='lightblue',font=20,command=lambda:Submit_picture())
                                Submit_pic.place(x=360,y=300)
                                
                                def selectPic():
                                    global img
                                    filename = filedialog.askopenfilename(initialdir="/folder",
                                                        filetypes=[("jpg images","*.jpg")])
                                    if filename.count("/") == 1:
                                        # print("your picture applicable")
                                        img = Image.open(filename)
                                        img = img.resize((200,200), Image.ANTIALIAS)
                                        img = ImageTk.PhotoImage(img)
                                        New_Photo['image'] = img
                                        # print(filename)
                                        Path.config(text=filename)    
                                        global path 
                                        path=filename
                                    else:
                                        messagebox.showerror("Error","your picture not applicable")
                                
                                
                                def Submit_picture():
                                    user_pic=path
                                    try:
                                        if 'jpg' in user_pic:
                                            mycursor.execute(f"update user set picture=load_file('{user_pic}') where user_id='{user_id}'")
                                            con.commit()
                                            Back__TO_Userview()
                                            UVl5=Label(root,text='-:Your Photo Successfully Uptodate:-',fg='green',font=("Calibri Light (Headings)",20))
                                            UVl5.place(x=300,y=130)
                                            UVl5.after(3000, lambda: UVl5.config(text=''))
                                        else:
                                            messagebox.showwarning("Database Error","file extension not valid")
                                            
                                    except Exception as e:
                                        messagebox.showwarning("Database Error",f"{e}")
                                
                                
                                def Back__TO_Userview():
                                    User_change_Title.destroy()                 
                                    changeFrame.destroy()
                                    Old_Frame.destroy()
                                    Old_title.destroy()
                                    old_Photo.destroy()
                                    New_Frame.destroy()
                                    New_title.destroy()
                                    New_Photo.destroy()
                                    Path.destroy()
                                    Back_User_View.destroy()
                                    choose_pic.destroy()
                                    Submit_pic.destroy()
                                    USER_VIEW()
                                    


                # change photo end


                # user photo view start 

                mycursor.execute(f"select picture from user  where user_id='{user_id}'")
                for details in mycursor:
                    user_pic=details[0]
                    with open('images.jpg','wb') as f:
                        f.write(user_pic)
                        img=Image.open("images.jpg")
                        img=img.resize((200,200))
                        img=ImageTk.PhotoImage(img)

                        IDatabase_UserImg=Label(UserimgViewe,image=img,bd=4,relief='groove')
                        IDatabase_UserImg.image=img
                        IDatabase_UserImg.place(x=25,y=30,width=250,height='250')
                        

                User_Image_change=Button(UserimgViewe,text='Change',font=(20),command=user_change_photo,cursor='hand2')
                User_Image_change.place(x=70,y=350,width=150,height=50)




                # user photo view compleate 
                def gotomain():
                                UserTitel.destroy()
                                UserdataViewe.destroy()     
                                UserimgViewe.destroy()
                                Database_UserName.destroy()
                                DATABASE_USERID.destroy()
                                DATABASE_DESIGNATION.destroy()
                                DATABASE_DEPARTMENE.destroy()
                                TotalLeave1.destroy()
                                LeaveTaken1.destroy()
                                ApproveLeave1.destroy()
                                RemainingLeave1.destroy()
                                TDatabase_UserName.destroy()
                                TDATABASE_USERID.destroy()
                                TDATABASE_DESIGNATION.destroy()
                                TDATABASE_DEPARTMENE.destroy()
                                TTotalLeave1.destroy()
                                TLeaveTaken1.destroy()
                                TApproveLeave1.destroy()
                                TRemainingLeave1.destroy()
                                IDatabase_UserImg.destroy()
                                User_Image_change.destroy()
                                
                                gotomain.destroy()
                                notice.destroy()
                                Home()



                gotomain=Button(root,text="LOG OUT",font=("times new roman",18,"bold"),activebackground="lightblue",bg='lightgray',fg="black",command=gotomain,cursor='hand2')
                gotomain.place(x=10,y=125,width=200,height=50)
                notice=Button(root,text="Notice",font=("Calibri_Light",15,"bold"),activebackground="lightblue",cursor='hand2',command=lambda:User_Sent_Notioce())
                notice.place(x=830,y=125,width=100,height=50)   
                
                #User Sent Notice Page----------------------------------------------------------------  
                def User_Sent_Notioce():
                    UserTitel.destroy()
                    UserdataViewe.destroy()     
                    UserimgViewe.destroy()
                    Database_UserName.destroy()
                    DATABASE_USERID.destroy()
                    DATABASE_DESIGNATION.destroy()
                    DATABASE_DEPARTMENE.destroy()
                    TotalLeave1.destroy()
                    LeaveTaken1.destroy()
                    ApproveLeave1.destroy()
                    RemainingLeave1.destroy()
                    TDatabase_UserName.destroy()
                    TDATABASE_USERID.destroy()
                    TDATABASE_DESIGNATION.destroy()
                    TDATABASE_DEPARTMENE.destroy()
                    TTotalLeave1.destroy()
                    TLeaveTaken1.destroy()
                    TApproveLeave1.destroy()
                    TRemainingLeave1.destroy()
                    IDatabase_UserImg.destroy()
                    User_Image_change.destroy()
                                
                    gotomain.destroy()
                    notice.destroy()
                    
                    noticetitle=Label(root,text="-:Notice:-",font=("times new roman",50),bg='GREEN',fg="WHIte")
                    noticetitle=Label(root,text="-:Notice:-",font=("times new roman",50),bg='GREEN',fg="WHIte")
                    noticetitle.pack(fill=X)
                    noticehead=Label(root,text="Dear Sir/Madam,",font=("times new roman",20))
                    noticehead.pack(anchor="w")

                    noticebody=Label(root,text="                     I Hope this letter finds You in good health and hight spirits. I am Writing to formally request a \n\nleave of absence from........................to......................as f need some time of to attend to ................... ",font=(18))    
                    noticebody.place(x=10,y=120)
                            
                    # Option Button Start 
                    List=['Medical Leave', 'Phisicl Leave', 'Personal Leave', 'Other']
                    option=StringVar()
                    option.set('Problem')
                    Lis=OptionMenu(root,option,*List)
                    Lis.place(x=830,y=155)


                    Entr=StringVar()
                    # pathname=StringVar()

                    yourType=Entry(textvariable=Entr,state='disabled')
                    yourType.place(x=820,y=180)
                    def my_show(*args):
                        if option.get()=='Other':
                            Entr.set('')
                            yourType.config(state='normal')
                            
                        else:
                            # print(option.get())
                            Entr.set(option.get())
                            yourType.config(state='disabled',text=Entr)
                            
                    option.trace('w',my_show) 

                    # Option Button End




                    # Date Entry Start Hear  
                    cal1=DateEntry(root,selectmode='day',date_pattern='yyyy-mm-dd')
                    cal1.place(x=220,y=170,width=120)
                    cal2=DateEntry(root,selectmode='day',date_pattern='yyyy-mm-dd')
                    cal2.place(x=385,y=170,width=120)
                    # Date Entry End Hear

                    your=Label(root,text="Your Sincerely",font=("times new roman",18))
                    your.place(x=800,y=220)
                    yourname=Label(root,text=Name,font=("Calibri_Light",15))
                    yourname.place(x=800,y=250)
                    yourId=Label(root,text=UID,font=("Calibri_Light",15))
                    yourId.place(x=850,y=280)
                    pathpdf=Label(root,state='disabled')
                    pathpdf.place(x=150,y=400,width=200)
                    Viewpdf=Button(root,text="Viewpdf",font=("Calibri_Light",15),activebackground="lightblue",state='disabled',cursor='hand2')
                    Viewpdf.place(x=350,y=400)
                    # Back to user view page
                    global file
                    file=StringVar()
                    def Attach():
                        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                                            title="choose Your Pdf File",
                                                            filetypes=(("PDF File",'.pdf'),("Pdf File",'.PDF')),
                                                            defaultextension='*.pdf')
                        file.set(filename)
                        pathpdf.config(text=filename,state='normal')
                        Viewpdf.config(text="Viewpdf",font=("Calibri_Light",15),activebackground="lightblue",command=lambda:ViewPDF(),state='normal')
                        
                        def ViewPDF():
                            webbrowser.open_new(filename)
                                
                                            
                    # Notie Button
                    snoticeButton=Button(root,text="Submit",font=("Calibri_Light",20),activebackground="lightblue",command=lambda:Submit(),cursor='hand2')
                    snoticeButton.place(x=850,y=500)
                                    
                    bnoticeButton=Button(root,text="Back",font=("Calibri_Light",20),activebackground="lightblue",command=lambda:BACK_TO_USERVIEW(),cursor='hand2')
                    bnoticeButton.place(x=10,y=500)

                    attachment=Button(root,text="Attachment",font=("Calibri_Light",15),activebackground="lightblue",command=Attach,cursor='hand2')
                    attachment.place(x=50,y=400)

                    def BACK_TO_USERVIEW():
                        snoticeButton.destroy()
                                    
                        bnoticeButton.destroy()

                        attachment.destroy()
                        
                        pathpdf.destroy()
                        Viewpdf.destroy()
                        cal1.destroy()
                        cal2.destroy()

                        your.destroy()
                        yourname.destroy()
                        yourId.destroy()
                        yourType.destroy()
                        Lis.destroy()
                        noticetitle.destroy()
                        noticehead.destroy()
                        noticebody.destroy()
                        USER_VIEW()
                        
                    def Submit():
                        if option.get()=='Other'and Entr.get()!=''and file.get()!='':
                            # print(Entr.get())
                            # print(cal1.get())
                            # print(cal2.get())  
                            # print(file.get())
                            
                            U_Id = UID
                            name = Name
                            notice = Entr.get()
                            # start_date = cal1.get()
                            # end_date = cal2.get()
                            leave =(cal2.get_date()-cal1.get_date()).days 
                            # = start_date+' to '+end_date
                            path = file.get()
                            mycursor.execute (f'insert into user_notification(user_id,name,date,notices,leave_date,picture) values({U_Id},"{name}",curdate(),"{notice}","{leave}",load_file("{path}"))')
                            con.commit()
                            NVl5=Label(root,text='-:Your Notice Send Successfully :-',fg='green',font=("Calibri Light (Headings)",20))
                            NVl5.place(x=300,y=130)
                            NVl5.after(3000, lambda: NVl5.config(text=''))
                            snoticeButton.destroy()
                                        
                            bnoticeButton.destroy()

                            attachment.destroy()
                            
                            pathpdf.destroy()
                            Viewpdf.destroy()
                            cal1.destroy()
                            cal2.destroy()

                            your.destroy()
                            yourname.destroy()
                            yourId.destroy()
                            yourType.destroy()
                            Lis.destroy()
                            noticetitle.destroy()
                            noticehead.destroy()
                            noticebody.destroy()
                            
                            USER_VIEW()
    
                            
                        elif option.get()!='Other'and option.get()!='Problem'and file.get()!='':
                            # print(file.get())
                            # print(option.get()) 
                            # print(cal1.get())
                            # print(cal2.get()) 
                            U_Id = UID
                            name = Name
                            notice = option.get()
                            # start_date = cal1.get()
                            # end_date = cal2.get()
                            leave =(cal2.get_date()-cal1.get_date()).days 
                            # = start_date+' to '+end_date
                            path = file.get()
                            mycursor.execute (f'insert into user_notification(user_id,name,date,notices,leave_date,picture) values({U_Id},"{name}",curdate(),"{notice}","{leave}",load_file("{path}"))')
                            con.commit()
                            NVl5=Label(root,text='-:Your Notice Send Successfully :-',fg='green',font=("Calibri Light (Headings)",20))
                            NVl5.place(x=300,y=130)
                            NVl5.after(3000, lambda: NVl5.config(text=''))
                            snoticeButton.destroy()
                                        
                            bnoticeButton.destroy()

                            attachment.destroy()
                            
                            pathpdf.destroy()
                            Viewpdf.destroy()
                            cal1.destroy()
                            cal2.destroy()

                            your.destroy()
                            yourname.destroy()
                            yourId.destroy()
                            yourType.destroy()
                            Lis.destroy()
                            noticetitle.destroy()
                            noticehead.destroy()
                            noticebody.destroy()
                            USER_VIEW()
                            
                            
                        else:
                            messagebox.showerror("Error","Please Fill all Items")    
                            pathpdf.config(text='')
                            option.set('Problem')
                            Entr.set('')
                            yourType.config(state='disabled',text=Entr)
   
                
            USER_VIEW()
            # User Page Compleated----------------------------------------------------------------
    # Admin Page Start----------------------------------------------------------------------------------------------------------------
    
    def AdminPage():
        NOTICETITLE.destroy()
        marquee.destroy()
        Title.destroy()
        admin.destroy()
        user.destroy()
        
        known_face_encoding=[]
        known_faces_names=[]
        known_faces_id=[]
        
        video=None
        first_count=0
        old_ids=0
        def video_stream(first_count,old_ids):
            con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
            Amycursor=con.cursor()
            global video
            video= cv2.VideoCapture(0)
            # address="http://192.168.0.105:4747/video"
            # video.open(address)

            Amycursor.execute("select admin.user_id,admin.name,user.picture from admin INNER JOIN user ON admin.user_id=user.user_id")
            for x in Amycursor:
                rec_data=x[2]
                data_ids=x[0]
                name_id=x[1]
                with open('images.jpg','wb') as f:
                    f.write(rec_data)
                # f=open('D:\\images.jpg','wb')
                # f.write(rec_data)
                image=face_recognition.load_image_file("images.jpg")
                encoding=face_recognition.face_encodings(image)[0]
                known_face_encoding.append(encoding)
                known_faces_names.append(name_id)
                known_faces_id.append(data_ids)
            Turn_on(first_count,old_ids)

        
        def Turn_on(first_count,old_ids):
            global video
            face_locations=[]
            face_encodings=[]
            ret,frame=video.read()
            
            
            if ret == True:
                
                live_video.place(x=45,y=65,width=450,height=350)
                
                
                frame = imutils.resize(frame,width=600)
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                faces = face_cap.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30,30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )

                for(x,y,w,h) in faces:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                        
                small_frame=cv2.resize(frame,(0,0),fx=0.25, fy=0.25)
                rgb_small_frame=small_frame[:,:,::-1]

                face_locations=face_recognition.face_locations(rgb_small_frame)
                face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
                for face_encoding in face_encodings:

                    matches=face_recognition.compare_faces(known_face_encoding, face_encoding)
                    name=" "
                    ids=" "
                    face_distance=face_recognition.face_distance(known_face_encoding, face_encoding)
                    best_match_index=np.argmin(face_distance)
                    if matches[best_match_index]:
                        name=known_faces_names[best_match_index]
                        ids=known_faces_id[best_match_index]
                        
                        if old_ids==ids:
                            first_count=first_count+1
                            if first_count==4:
                                first_count=0
                            # images retrive from data bases
                                # print(ids)
                                # print(name)
                                global Name
                                Name=name
                                global ID
                                ID=ids
                                mycursor.execute(f"select picture,department from user where user_id='{ids}'")
                                for z in mycursor:
                                    y=z[0]
                                    f=open('images.jpg','wb')
                                    f.write(y)
                                    user_dept=z[1]
                                    # present update
                                user_id_list=[]
                                mycursor.execute("select user_id from present where date=curdate()")
                                for users_id in mycursor:
                                    users_ids=users_id[0]
                                    user_id_list.append(users_ids)

                                if ids in user_id_list:
                                    mycursor.execute(f"select present_id from present where user_id={ids} and name='{name}' and Date=curdate()")
                                    for i in mycursor:
                                        presents_ids=i[0]
                                    mycursor.execute(f"update present set departure_time=curtime() where present_id='{presents_ids}'")
                                    con.commit()
                                else:
                                    mycursor.execute(f"insert into present(user_id,name,Date,arrival_time,department) values({ids},'{name}',curdate(),curtime(),'{user_dept}')")
                                    con.commit()
                                f=pyttsx3.init()
                                sound_name=name
                                f.say(f"hello{sound_name}")
                                f.runAndWait()
                                
                                
                                img= Image.open("images.jpg")
                                img=img.resize((200,200)) 
                                img=ImageTk.PhotoImage(img) 
                                database_image.configure(image=img)
                                database_image.image=img
                                wellcomemsg.config(text=f"-:Hello{name}:-")
                                wellcomemsg.after(3000,lambda:wellcomemsg.config(text=''))
                                Name_msg.config(text=name)
                                gotoAdminSubmit.config(state='normal')
                        else:
                            first_count=0
                        old_ids=ids
                    else:
                        first_count=0
                        f=pyttsx3.init()
                        f.say("you are unknown persion")
                        f.runAndWait()
                        Name_msg.config(text='')
                        msg.config(text='')     
                        database_image.config(image='')
                        gotoAdminSubmit.config(state='disabled')
            
                        
            img = Image.fromarray(frame)
            image = ImageTk.PhotoImage(image=img)
            live_video.configure(image=image)
            live_video.image = image
            live_video.after(10, lambda:Turn_on(first_count,old_ids))
        def clear():
                Name_msg.config(text='')
                
                    # msg.config(text='')     
                database_image.config(image='') 
                gotoAdminSubmit.config(state='disabled') 


        #main frame============================================================== 
        title=Label(root,text="Welcome To Face Recognizer",font=("times new roman",40),bg='GREEN',fg="WHIte")
        title.place(x=0,y=0,relwidth=1)
        live_Frame=Frame(root,bd=2,relief="raised",bg="blue")
        live_Frame.place(x=50,y=130,width=550,height=450)
        live_titel=Label(live_Frame,text="Face Recognizer",font=("times new roman",20),bg='lightpink',fg="black")
        live_titel.place(x=0,y=0,relwidth=1)
                #live video============================================================
                            
        live_video=Label(live_Frame,bd=2,relief=RAISED)
        live_video.place(x=45,y=65,width=450,height=350)


                #show image================================
        Your_data=Frame(root,bd=2,relief="raised",bg="blue")
        Your_data.place(x=650,y=130,width=300,height=450)
        Your_data1=Label(Your_data,text="Face Recognizer",font=("times new roman",20),bg='lightpink',fg="black")
        Your_data1.place(x=0,y=0,relwidth=1)
        database_image=Label(Your_data,text="No Img",font=('times new roman',15),bg='gray',fg='black',bd=1,relief=RAISED)
        database_image.place(x=25,y=45,width=250,height=250)

        

                
        Name_msg=Label(Your_data,font=("times new roman",15),bg='gray')
        Name_msg.place(x=35,y=270,height=20)

                
        msg=Label(Your_data,text='Already Attend',font=("times new roman",20),bg='blue',fg="Lightgreen")
        msg.place(x=50,y=335)

        wellcomemsg=Label(root,font=("times new roman",28,"bold"),fg="green")
        wellcomemsg.place(x=255,y=590)
                #button================================================================
        data_clear=Button(Your_data,text="Clear All Data",font=("times new roman",18,"bold"),command=clear,bg='lightgray',fg="black")
        data_clear.place(x=70,y=385,width=160,height=50)               
        Backtomain=Button(root,text="back",font=("times new roman",18,"bold"),command=lambda:BacktoMainPage())
        Backtomain.place(x=20,y=590)
        gotoAdminSubmit=Button(root,text="Submit",font=("times new roman",18,"bold"),state='disabled',command=lambda:Admin_second_varifiacation())
        gotoAdminSubmit.place(x=900,y=590)

        video_stream(first_count,old_ids)
        
        # BacktoAminPage--------------------------------------------------------------
        def BacktoMainPage():
            global video
            live_video.config(image='')
            # live_video.place_forget()
            video.release()
            title.destroy()
            live_Frame.destroy()
            live_titel.destroy()
            live_video.destroy()
            Your_data.destroy()
            Your_data1.destroy()
            database_image.destroy

            Name_msg.destroy()
            msg.destroy()

            wellcomemsg.destroy()
            data_clear.destroy()               
            Backtomain.destroy()
            gotoAdminSubmit.destroy()
            Home()
            
            #admin Second varifiacation page
        def Admin_second_varifiacation(): 
                
                ids=ID
                global video
                live_video.config(image='')
                # live_video.place_forget()
                video.release()
                title.destroy()
                live_Frame.destroy()
                live_titel.destroy()
                live_video.destroy()
                Your_data.destroy()
                Your_data1.destroy()
                database_image.destroy

                Name_msg.destroy()
                msg.destroy()

                wellcomemsg.destroy()
                data_clear.destroy()               
                Backtomain.destroy()
                gotoAdminSubmit.destroy()
                titel2=Label(root,text="ADMIN VERIFICATION",font=("times new roman",40),bg='GREEN',fg="WHIte")
                titel2.place(x=0,y=0,relwidth=1)
                AdminLogin=Frame(root,bd=10,bg='lightgreen',relief='raised')
                AdminLogin.place(x=150,y=120,width=700,height=300)

                AdminId=Label(AdminLogin,text="Admin ID",font=("Calibri Light (Headings)",25),bg='lightgreen')
                AdminId.place(x=50,y=20)
                AdminPassword=Label(AdminLogin,text="Admin Password",font=("Calibri Light (Headings)",25),bg='lightgreen')
                AdminPassword.place(x=50,y=80)       

                AID=StringVar()
                AP=StringVar()
                AId=Entry(AdminLogin,show="*",font=("Calibri Light (Headings)",22),bg="lightyellow",textvariable=AID)
                AId.place(x=300,y=20)   
                APass=Entry(AdminLogin,show="*",font=("Calibri Light (Headings)",22),bg="lightyellow",textvariable=AP)
                APass.place(x=300,y=80)

                # admin_id_list=[]
                # mycursor.execute("select user_id from admin")
                # for id_pass in mycursor:
                #     admin_id=id_pass[0]
                #     admin_id_list.append(admin_id)


                SubmitButton=Button(AdminLogin,text="SUBMIT",font=("Calibri Light (Headings)",20),command=lambda:adminzonesubmit(),activebackground="lightblue")
                SubmitButton.place(x=300,y=150)    
                forgetpass=Button(AdminLogin,text='Forget Password',font=('Times',10,'underline'),activebackground="lightgreen",command=lambda:forgetpas(),fg='blue',bg='lightgreen',cursor='hand2')
                forgetpass.place(x=450,y=170) 
                            
                def Cpass():
                    if  APass.cget('show')=='*':
                        APass.config(show='')
                    else:
                        APass.config(show='*')    
                cpass=Checkbutton(AdminLogin,command=Cpass,bg='lightgreen',activebackground='lightgreen')
                cpass.place(x=630,y=80)

                   # forget password start 
                def forgetpas():
                        con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                        mycursor=con.cursor()
                        AID.set('')
                        AP.set('')
                        fpass=Toplevel()
                        fpass.grab_set()
                        fpass.geometry("700x400+405+200")
                        fpass.title("Forget Password")
                        fpass.resizable(False,False)
                        fpass.overrideredirect(1)
                        noticetitle=Label(fpass,text="-:Forget Password:-",font=("times new roman",30),bg='GREEN',fg="WHIte")
                        noticetitle.pack(fill=X)
                        Newframe=Frame(fpass,bg='bisque1',relief='sunken',bd='5')
                        Newframe.place(x=50,y=100,width=600,height=250)
                        NewPassword=Label(Newframe,text='New Password:-',font='Calibri_Light 20 bold',bg='bisque1')
                        NewPassword.place(x=50,y=50)
                        ConformPassword=Label(Newframe,text='Conform Password:-',font='Calibri_Light 20 bold',bg='bisque1')
                        ConformPassword.place(x=20,y=100)
                        Npass=StringVar()
                        Cpass=StringVar()
                        NewPassdata=Entry(Newframe,font='Calibri_Light 20 bold',bg='lightyellow',bd=2,relief='sunken',textvariable=Npass)
                        NewPassdata.place(x=300,y=50,width=250)
                        ConformPassdata=Entry(Newframe,font='Calibri_Light 20 bold',bg='lightyellow',relief='sunken',textvariable=Cpass)
                        ConformPassdata.place(x=300,y=100,width=250)
                        NnoBack=Button(Newframe,text='Back',font=('Calibri_Light' 'bold'),command=fpass.destroy)
                        NnoBack.place(x=50,y=150)
                        NyesSubmit=Button(Newframe,text='Sumbit',font=('Calibri_Light'  'bold'),command=lambda:PasswordChange())
                        NyesSubmit.place(x=500,y=150)
                            # Admin Home Page
                        def PasswordChange():
                                if Npass.get() != Cpass.get():
                                    messagebox.showwarning('warning',"password and confirm password are not same")
                                    Npass.set('')
                                    Cpass.set('')
                                else:
                                    con_pass=Npass.get()
                                    # print(Cpass.get()) 
                                    length=len(con_pass)
                                    if length <=50:
                                        mycursor.execute(f"update admin set password='{con_pass}' where user_id='{ids}'")
                                        con.commit()
                                        fpass.destroy()  
                                        sm=Label(root,text="-:Your Password Successfully Changed:-",fg='green',font=('Arial',30))
                                        sm.place(x=130,y=500)
                                        sm.after(3000,lambda:sm.config(text=''))
                                    else:
                                        print("ok")
                                        messagebox.showwarning('warning','plase enter fifty digit password')
                def adminzonesubmit():
                    con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                    Asmycursor=con.cursor()
                    if AID.get()==''or AP.get()=='':
                                messagebox.showwarning('warning',"Please Fill All The Items")
                                AID.set('')
                                AP.set('')
                    else:
                        try:
                            ide =int(AID.get())
                            passw=AP.get()
                            if ide == ids:
                                
                                Asmycursor.execute(f"select password from admin where user_id='{ide}'")
                                for pass_check in Asmycursor:
                                    admin_pass=pass_check[0]
                                # print("id detected")
                                if passw==admin_pass:
                                        titel2.destroy()
                                        AdminId.destroy()
                                        AdminPassword.destroy()
                                        AId.destroy()
                                        APass.destroy()
                                        AdminLogin.destroy()
                                        SubmitButton.destroy()
                                        titel2.destroy()
                                        
                                        def  Adminhome():
                                            titel3=Label(root,text="ADMIN HOME PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                            titel3.place(x=0,y=0,relwidth=1)
                                            adminhomeframe=Frame(root,bg='lightyellow',relief='groove',bd='10',padx='50')
                                            adminhomeframe.place(x=150,y=100,width=700,height=300)
                                            # adminname="ADMIN NAME"
                                            AName=Label(root,text=f"-:Welcome {Name} :-",font=("times new roman",30))
                                            AName.place(x=250,y=70)   
                                            
                                            # Admin Page Buttons
                                            
                                            insert=Button(adminhomeframe,text="INSERT ",font=("Calibri Light (Headings)",20),command=lambda:MainInsert())
                                            insert.place(x=20,y=30,width=150,height=50)
                                            
                                            Update=Button(adminhomeframe,text="UPDATE ",font=("Calibri Light (Headings)",20),command=lambda:MainUpdate())
                                            Update.place(x=200,y=30,width=150,height=50)
                                            
                                            Delete=Button(adminhomeframe,text="DELETE",font=("Calibri Light (Headings)",20),command=lambda:MainDelete())
                                            Delete.place(x=380,y=30,width=150,height=50)
                                            
                                            Logout=Button(adminhomeframe,text="Logout",font=("Calibri Light (Headings)",20),command=lambda:adminhome())
                                            Logout.place(x=20,y=130,width=150,height=50)
                                            
                                            VIEW=Button(adminhomeframe,text="View",font=("Calibri Light (Headings)",20),command=lambda:MainViewPage())
                                            VIEW.place(x=200,y=130,width=150,height=50)
                                            
                                            NoticeButton=Button(adminhomeframe,text="Notice",font=("Calibri Light (Headings)",20),command=lambda:mnotice())
                                            NoticeButton.place(x=380,y=130,width=150,height=50)                            
                                            # Goto Home Page
                                            
                                            def adminhome():
                                                titel3.destroy()
                                                insert.destroy()
                                                Update.destroy()
                                                Delete.destroy()
                                                Logout.destroy()
                                                VIEW.destroy()
                                                AName.destroy()
                                                
                                                NoticeButton.destroy()
                                                adminhomeframe.destroy()
                                                Home()
                                                
                                            #MainInsert  page
                                            def MainInsert():
                                                titel3.destroy()
                                                insert.destroy()
                                                Update.destroy()
                                                Delete.destroy()
                                                Logout.destroy()
                                                VIEW.destroy()
                                                AName.destroy()
                                                
                                                NoticeButton.destroy()
                                                adminhomeframe.destroy()
                                                
                                                
                                                titel4=Label(root,text="INSERT PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                titel4.place(x=0,y=0,relwidth=1)
                                                                        
                                                InsertFrame=Frame(root,bg='peach puff',relief='ridge',bd='15')
                                                InsertFrame.place(x=300,y=100,height=200,width=400)


                                                # Back to admin Home Page
                                                def BacktoAdminHome():
                                                    titel4.destroy()
                                                    userInsert.destroy()
                                                    adminInsert.destroy()
                                                    Backtoadminhome.destroy()
                                                    InsertFrame.destroy()
                                                    Adminhome()
                                                    
                                                    # User Admin Position start
                                                def AdminInsert():
                                                   
                                                    
                                                    titel4.destroy()
                                                    userInsert.destroy()
                                                    adminInsert.destroy()
                                                    Backtoadminhome.destroy()
                                                    InsertFrame.destroy()
                                                    titel6=Label(root,text="Welcome To Admin Insert Page",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                    titel6.place(x=0,y=0,relwidth=1)
                                                    AdminInsertFrame=Frame(root,bg='lightgreen')
                                                    AdminInsertFrame.place(x=200,y=100,width=600,height=280)

                                                    NameAdmininsert=Label(AdminInsertFrame,text="Name Of Admin",font=("times new roman",20),bg='lightgreen')
                                                    NameAdmininsert.place(x=40,y=40)
                                                    IdAdmininsert=Label(AdminInsertFrame,text="Id Of Admin",font=("times new roman",20),bg='lightgreen')
                                                    IdAdmininsert.place(x=60,y=90)
                                                    PassAdmininsert=Label(AdminInsertFrame,text="Password Of Admin",font=("times new roman",20),bg='lightgreen')
                                                    PassAdmininsert.place(x=20,y=140)
                                                                                
                                                    # Entry
                                                    AName=StringVar()
                                                    AId=StringVar()
                                                    APass=StringVar()
                                                                                
                                                                                
                                                    NameAdmininsertEntry=Entry(AdminInsertFrame,font=("times new roman",20),textvariable=AName)
                                                    NameAdmininsertEntry.place(x=250,y=40)
                                                    IdAdmininsertEntry=Entry(AdminInsertFrame,font=("times new roman",20),textvariable=AId)
                                                    IdAdmininsertEntry.place(x=250,y=90)
                                                    PassAdmininsertEntry=Entry(AdminInsertFrame,font=("times new roman",20),textvariable=APass)
                                                    PassAdmininsertEntry.place(x=250,y=140)
                                                                                                
                                                                                
                                                    #Submit Button
                                                    def ASubmit():
                                                        if AName.get()==''or AId.get()=='' or APass.get()=='':
                                                            messagebox.showwarning('warning',"Please Fill All The Items")     
                                                        else:
                                                            con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                            AImycursor=con.cursor()
                                                            user_id_lists=[]
                                                            AImycursor.execute("select user_id from user")
                                                            for id_pass in AImycursor:
                                                                user_ids=id_pass[0]
                                                                user_id_lists.append(user_ids)
                                                            count=0
                                                            count1=0
                                                            try:
                                                                admin_user_id=[]
                                                                AImycursor.execute("select user_id from admin")
                                                                for admin_i in AImycursor:
                                                                    admin_i2=admin_i[0]
                                                                    admin_user_id.append(admin_i2)
                                                                admin_name=AName.get()
                                                                admin_id=int(AId.get())
                                                                admin_password=APass.get()

                                                                admin_name=admin_name.upper()
                                                                if admin_id in user_id_lists:
                                                                    AImycursor.execute(f"select name from user where user_id={admin_id}")
                                                                    for ad_name in AImycursor:
                                                                        user_name=ad_name[0]
                                                                    count=1
                                                                if user_name==admin_name:
                                                                    count1=1
                                                            except Exception as e:
                                                                messagebox.showwarning('warning',f"{e}") 
                                                                AName.set('')
                                                                AId.set('')
                                                                APass.set('')

                                                        try:
                                                            if count==1 and count1==1:
                                                                if admin_id in admin_user_id:
                                                                    messagebox.showerror('error',"all ready insert")
                                                                else:
                                                                    AImycursor.execute(f"insert into admin(name,user_id,password)values('{admin_name}','{admin_id}','{admin_password}')")
                                                                    con.commit()
                                                                    AName.set('')
                                                                    AId.set('')
                                                                    APass.set('')
                                                                    l2=Label(root,text=f"-:{admin_name} You Are Now As an Admin:-",fg='green',font=("Calibri Light (Headings)",30))
                                                                    l2.place(x=120,y=500)
                                                                    l2.after(3000, lambda: l2.config(text=''))
                                                            else:
                                                                messagebox.showwarning('warning',"Please Check Your Id And Name") 
                                                                AName.set('')
                                                                AId.set('')
                                                                APass.set('')
                                                                
                                                        except Exception as e:
                                                            messagebox.showwarning('warning',f"{e}") 
                                                            AName.set('')
                                                            AId.set('')
                                                            APass.set('')
                                                        
                                                        
                                                        
                                                    #Back to Insert Page
                                                                                
                                                                                
                                                    def BacktoInsertPage():
                                                        titel6.destroy() 
                                                        NameAdmininsert.destroy()
                                                        IdAdmininsert.destroy()
                                                        PassAdmininsert.destroy()
                                                        PassAdmininsertEntry.destroy()
                                                        IdAdmininsertEntry.destroy()
                                                        NameAdmininsertEntry.destroy()
                                                        ABacktoInsertPage.destroy()
                                                        ASubmitButton.destroy()
                                                        AdminInsertFrame.destroy()
                                                        MainInsert()
                                                                                    
                                                    #insert Admin Buttons
                                                    ABacktoInsertPage=Button(AdminInsertFrame,text="Back",font=("times new roman",20),activebackground="lightblue",command=BacktoInsertPage)
                                                    ABacktoInsertPage.place(x=150,y=200)
                                                    ASubmitButton=Button(AdminInsertFrame,text="Submit",font=("times new roman",20),activebackground="lightblue",command=ASubmit)
                                                    ASubmitButton.place(x=250,y=200)
                                                    AClearButton=Button(AdminInsertFrame,text="Clear",font=("times new roman",20),activebackground='lightblue',command=lambda:AIClear())
                                                    AClearButton.place(x=380,y=200)                        
                                                    # Insert Admin Page end
                                                    def AIClear():
                                                        AName.set('')
                                                        AId.set('')
                                                        APass.set('')
                                                                                                    

                                                                        
                                                    # Admin Insert Page End   
                                                    
                                                # User Insert Page Start
                                                
                                                def UserInsert():
                                                        
                                                    titel4.destroy()
                                                    userInsert.destroy()
                                                    adminInsert.destroy()
                                                    Backtoadminhome.destroy()
                                                    InsertFrame.destroy()
                                                    titel5=Label(root,text="Welcome To User Insert Page",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                    titel5.place(x=0,y=0,relwidth=1)

                                                    UserInsertFrame=Frame(root,bg='lightgreen',bd=4,relief='ridge')
                                                    UserInsertFrame.place(x=200,y=100,width=600,height=350)       

                                                                        
                                                    UName=Label(UserInsertFrame,text="Enter Name",font=("Calibri Light (Headings)",20),bg='lightgreen')
                                                    UName.place(x=55,y=10)
                                                    Iagepath=Label(UserInsertFrame,text="Enter Image Path",font=("Calibri Light (Headings)",20),bg='lightgreen')
                                                    Iagepath.place(x=20,y=55)
                                                    Designation=Label(UserInsertFrame,text="Enter Designation",font=("Calibri Light (Headings)",20),bg='lightgreen')
                                                    Designation.place(x=20,y=100)
                                                    Department=Label(UserInsertFrame,text="Enter Department",font=("Calibri Light (Headings)",20),bg='lightgreen')
                                                    Department.place(x=20,y=145)

                                                    SLeav=Label(UserInsertFrame,text="Enter Leave",font=("Calibri Light (Headings)",20),bg='lightgreen')
                                                    SLeav.place(x=50,y=195)
                                                                            
                                                    UNameEntry=StringVar()
                                                    ULeavEntry=StringVar()
                                                    UIagepathEntry=StringVar()
                                                    UDesignationEntry=StringVar()
                                                    UDepartmentEntry=StringVar()
                                                                            
                                                    UnameEntry=Entry(UserInsertFrame,font=("Calibri Light (Headings)",20),textvariable=UNameEntry)
                                                    UnameEntry.place(x=250,y=10)

                                                    IagepathEntry=Entry(UserInsertFrame,font=("Calibri Light (Headings)",20),textvariable=UIagepathEntry)
                                                    IagepathEntry.place(x=250,y=55)      
                                                    DesignationEntry=Entry(UserInsertFrame,font=("Calibri Light (Headings)",20),textvariable=UDesignationEntry)
                                                    DesignationEntry.place(x=250,y=100)
                                                    DepartmentEntry=Entry(UserInsertFrame,font=("Calibri Light (Headings)",20),textvariable=UDepartmentEntry)
                                                    DepartmentEntry.place(x=250,y=145)

                                                    SLeaveEntry=Entry(UserInsertFrame,font=("Calibri Light (Headings)",20),textvariable=ULeavEntry)
                                                    SLeaveEntry.place(x=250,y=195)


                                                    lbl_show_pic = Label(root)
                                                    lbl_show_pic.place(x=800,y=150)
                                                        
                                                                                    
                                                    # User Insert Buttons

                                                                                                
                                                    MainBack=Button(UserInsertFrame,text="Back",font=("Calibri Light (Headings)",20),command=lambda:userinsert_to_maininsertpage())    
                                                    MainBack.place(x=100,y=250)
                                                    InsertSubmit=Button(UserInsertFrame,text="Submit",font=("Calibri Light(Headings)",20),command=lambda:USubmit())
                                                    InsertSubmit.place(x=240,y=250)
                                                    InsertClear=Button(UserInsertFrame,text="Clear",font=("Calibri Light(Headings)",20),command=lambda:clearInsert())
                                                    InsertClear.place(x=400,y=250)   
                                                    UImg=Button(UserInsertFrame,text="Browes",font=("Calibri Light(Headings)",15),command=lambda:selectPic())
                                                    UImg.place(x=505,y=55)


                                                    # Brows Images
                                                    def selectPic():
                                                        global img
                                                        UserInsertfilename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                                                        filetypes=[("jpg images","*.jpg")])
                                                        if UserInsertfilename.count("/") == 1:
                                                            img = Image.open(UserInsertfilename )
                                                            img = img.resize((200,200), Image.ANTIALIAS)
                                                            img = ImageTk.PhotoImage(img)
                                                            lbl_show_pic['image'] = img
                                                            IagepathEntry.insert(0, UserInsertfilename )
                                                        else:
                                                            messagebox.showerror("error","your picture not applicable")
                                                            IagepathEntry.delete(0,'end')
                                                            lbl_show_pic.config(image='')
                                                    
                                                        
                                                    #Clear All Data
                                                    def clearInsert():
                                                        UNameEntry.set('')
                                                        ULeavEntry.set('')
                                                        UIagepathEntry.set('')
                                                        UDesignationEntry.set('')
                                                        UDepartmentEntry.set('')
                                                        lbl_show_pic.config(image='')
                                                        

                                                    # User Submit 
                                                    def USubmit():
                                                        con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                        UImycursor=con.cursor()
                                                        if UNameEntry.get()==''or ULeavEntry.get()=='' or UIagepathEntry.get()=='' or UDesignationEntry.get()==''or UDepartmentEntry.get()=='':
                                                            messagebox.showwarning('warning',"Please Fill All The Items")  
                                                        else:
                                                                 
                                                                
                                                            # print((UNameEntry.get()).upper())    
                                                            # print(ULeavEntry.get())    
                                                            # print(UIagepathEntry.get())    
                                                            # print((UDesignationEntry.get()).upper())    
                                                            # print((UDepartmentEntry.get()).upper())    
                                                            
                                                            
                                                                    # user id
                                                            user_id_lists=[]
                                                            UImycursor.execute("select user_id from user")
                                                            for id_pass in UImycursor:
                                                                user_ids=id_pass[0]
                                                                user_id_lists.append(user_ids)
                                                            user_id=int(user_id_lists[-1])+1
                                                            count=0
                                                            try:
                                                                user_name=UNameEntry.get()
                                                                user_img_path=UIagepathEntry.get()
                                                                user_deisg=UDesignationEntry.get()
                                                                user_dept=UDepartmentEntry.get()
                                                                user_total_leave=int(ULeavEntry.get())
                                                                user_name=user_name.upper()
                                                                user_deisg=user_deisg.upper()
                                                                user_dept=user_dept.upper()
                                                            
                                                                
                                                            except Exception as e:
                                                                count=1
                                                                UNameEntry.set('')
                                                                ULeavEntry.set('')
                                                                UIagepathEntry.set('')
                                                                UDesignationEntry.set('')
                                                                UDepartmentEntry.set('')
                                                                lbl_show_pic.config(image='') 
                                                                messagebox.showwarning('warning',f"{e}")
                                                            try:
                                                                b=10
                                                                if type(user_total_leave)==type(b):
                                                                    if 'jpg'in user_img_path and count==0:
                                                                        UImycursor.execute(f"insert into user (name,picture,designation,department) values('{user_name}',load_file('{user_img_path}'),'{user_deisg}','{user_dept}')")
                                                                        # UImycursor.execute(f"insert into leaves(user_id,name,total_leave) values('{user_id}','{user_name}','{user_total_leave}')")
                                                                        con.commit()
                                                                        user_id_lists=[]
                                                                        UImycursor.execute("select user_id from user")
                                                                        for id_pass in UImycursor:
                                                                            user_ids=id_pass[0]
                                                                            user_id_lists.append(user_ids)
                                                                        user_id=int(user_id_lists[-1])
                                                                        UImycursor.execute(f"insert into leaves(user_id,name,total_leave) values('{user_id}','{user_name}','{user_total_leave}')")
                                                                        con.commit()
                                                                        UNameEntry.set('')
                                                                        ULeavEntry.set('')
                                                                        UIagepathEntry.set('')
                                                                        UDesignationEntry.set('')
                                                                        UDepartmentEntry.set('')
                                                                        lbl_show_pic.config(image='')    
                                                                        l1=Label(root,text='-:Successfully Inserted:-',fg='green',font=("Calibri Light (Headings)",30))
                                                                        l1.place(x=300,y=500)
                                                                    
                                                                        
                                                                    else:
                                                                        UNameEntry.set('')
                                                                        ULeavEntry.set('')
                                                                        UIagepathEntry.set('')
                                                                        UDesignationEntry.set('')
                                                                        UDepartmentEntry.set('')
                                                                        lbl_show_pic.config(image='') 
                                                                        messagebox.showwarning('warning',"file extension not valid")
                                                                else:
                                                                    UNameEntry.set('')
                                                                    ULeavEntry.set('')
                                                                    UIagepathEntry.set('')
                                                                    UDesignationEntry.set('')
                                                                    UDepartmentEntry.set('')
                                                                    lbl_show_pic.config(image='') 
                                                                    messagebox.showwarning('warning',"you can not insert alphabet")

                                                            except Exception as e:
                                                                print("wrong input")
                                                                UNameEntry.set('')
                                                                ULeavEntry.set('')
                                                                UIagepathEntry.set('')
                                                                UDesignationEntry.set('')
                                                                UDepartmentEntry.set('')
                                                                lbl_show_pic.config(image='') 
                                                                messagebox.showwarning('warning',f"{e}")
                                                            l1.after(3000, lambda: l1.config(text=''))
                                                                                
                                                                                    
                                                    # user to Maininset page
                                                    def userinsert_to_maininsertpage():
                                                        titel5.destroy()
                                                        UName.destroy()
                                                        SLeav.destroy()
                                                        Iagepath.destroy()
                                                        Designation.destroy()
                                                        Department.destroy()
                                                        MainBack.destroy()
                                                        InsertSubmit.destroy()
                                                        InsertClear.destroy()
                                                        UnameEntry.destroy()
                                                        SLeaveEntry.destroy()
                                                        IagepathEntry.destroy()
                                                        DesignationEntry.destroy()
                                                        DepartmentEntry.destroy()
                                                        UImg.destroy()
                                                        lbl_show_pic.destroy()
                                                        UserInsertFrame.destroy()
                                                        MainInsert()                                  

                                                
                                                                            
                                                                            
                                                # User Insert Page End
                                                    #   Insert Page Button
                                                userInsert=Button(InsertFrame,text="User",font='Calibri_Light 15 bold',padx=5,pady=5,activebackground="lightblue",command=UserInsert)
                                                userInsert.place(x=100,y=10)
                                                adminInsert=Button(InsertFrame,text="Admin",font='Calibri_Light 15 bold',padx=5,pady=5,activebackground="lightblue",command=AdminInsert)
                                                adminInsert.place(x=200,y=10)
                                                Backtoadminhome=Button(InsertFrame,text="Back to admin",font='Calibri_Light 15 bold',padx=5,pady=5,activebackground="lightblue",command=BacktoAdminHome)
                                                Backtoadminhome.place(x=115,y=80)
                                            # Insert page Done-------------------------------------------------------------------------
                                            
                                            # Update Page Start-------------------------------------------------------------------------
                                        
                                            def MainUpdate():
                                                titel3.destroy()
                                                insert.destroy()
                                                Update.destroy()
                                                Delete.destroy()
                                                Logout.destroy()
                                                VIEW.destroy()
                                                AName.destroy()
                                                
                                                NoticeButton.destroy()
                                                adminhomeframe.destroy()
                                                 
                                                UpdateLabel=Label(root,text="UPDATE PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                UpdateLabel.place(x=0,y=0,relwidth=1)                      
                                                UUI=StringVar()
                                                UpdateFrame=Frame(root,bg='yellow3',relief='ridge',bd='15')
                                                UpdateFrame.place(x=300,y=100,height=200,width=400)
                                                UpdateId=Label(UpdateFrame,text="Enter Id",font=("times new roman",20))
                                                UpdateId.place(x=30,y=20)
                                                UpdateIdEntry=Entry(UpdateFrame,font='Calibri_Light 20',textvariable=UUI)
                                                UpdateIdEntry.place(x=140,y=20,width=200)
                                                                        
                                                                        
                                                                        # goto next Update Page
                                                UpdateSubmit=Button(UpdateFrame,text='Submit',font='bold 25',command=lambda:UpdateHomePage())
                                                UpdateSubmit.place(x=200,y=100,height=50,width=120)   
                                                                    
                                                UpdateBack=Button(UpdateFrame,text='Back',font='bold 25',command=lambda:updatetohome())
                                                UpdateBack.place(x=65,y=100,height=50,width=100)   
                                                
                                                # back to Admin Home Page----------------------------------------------------------------
                                                def updatetohome():
                                                    UpdateFrame.destroy()
                                                    UpdateBack.destroy()
                                                    UpdateSubmit.destroy()
                                                    Adminhome()
                                                    UpdateId.destroy()
                                                    UpdateIdEntry.destroy()
                                                    UpdateLabel.destroy()
                                                                     
                                                def UpdateHomePage():
                                                    con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                    UUmycursor=con.cursor()
                                                    if UUI.get()=='':
                                                        messagebox.showwarning('warning',"Please Fill The Item")     
                                                    else:
                                                    
                                                        user_id_lists=[]
                                                        UUmycursor.execute("select user_id from user")
                                                        for id_pass in UUmycursor:
                                                            user_ids=id_pass[0]
                                                            user_id_lists.append(user_ids)
                                                        # count=0
                                                        try:
                                                            user_id=int(UUI.get())
                                                            if user_id in user_id_lists :
                                                                                            # old Data
                                                                UpdateFrame.destroy()
                                                                # UpdateBack.destroy()
                                                                UpdateSubmit.destroy()
                                                                UpdateId.destroy()
                                                                UpdateIdEntry.destroy()
                                                                # utitel.destroy()    
                                                                # forName
                                                                # user id                            
                                                                LeftFrame=Frame(root,bg='lightgreen',bd='5',relief='groove')
                                                                LeftFrame.place(x=40,y=80,width=460,height=470)

                                                                RightFrame=Frame(root,bg='lightgreen',bd='5',relief='groove')
                                                                RightFrame.place(x=520,y=80,width=450,height=470)


                                                                oldphoto=Label(LeftFrame,text='Old photo',bd=2,relief='groove')
                                                                oldphoto.place(x=130,y=55,width=200,height=200)
                                                                olddata=Label(LeftFrame,text="OLD DATA",bg='lightgreen',font=('Bernard MT Condensed',30,'bold'))
                                                                olddata.pack()
                                                                OUName=Label(LeftFrame,text="Old Name",font=("Vrinda (Headings CS)",20),bg='lightgreen')
                                                                OUName.place(x=10,y=260)
                                                                OSLeave=Label(LeftFrame,text="Old Leave",font=("Vrinda (Headings CS)",20),bg='lightgreen')
                                                                OSLeave.place(x=10,y=310)
                                                                ODesignation=Label(LeftFrame,text="Old Designation",font=("Vrinda (Headings CS)",20),bg='lightgreen')
                                                                ODesignation.place(x=10,y=360)
                                                                ODepartment=Label(LeftFrame,text="Old Department",font=("Vrinda (Headings CS)",20),bg='lightgreen')
                                                                ODepartment.place(x=10,y=410)

                                                                try:    
                                                                    if UUI.get()!='':
                                                                        UUmycursor.execute(f"select user.name,user.picture,user.department,user.designation,leaves.total_leave from user  INNER JOIN leaves ON user.user_id=leaves.user_id where user.user_id='{user_id}'")
                                                                        for details in UUmycursor:
                                                                            user_name=details[0]
                                                                            user_pic=details[1]
                                                                            with open('images.jpg','wb') as f:
                                                                                f.write(user_pic)
                                                                            img=Image.open("images.jpg")
                                                                            img=img.resize((200,200))
                                                                            img=ImageTk.PhotoImage(img)
                                                                            oldphoto.config(image=img)
                                                                            oldphoto.image=img 
                                                                                
                                                                            user_desig=details[2]
                                                                            user_dept=details[3]
                                                                            user_leave=details[4]

                                                                

                                                                        OUNameData=Label(LeftFrame,text=user_name,font=("Vrinda (Headings CS)",13),bg='lightYellow',bd='5',relief='ridge',fg='black')
                                                                        OUNameData.place(x=210,y=270,width='200')
                                                                        OSLeaveData=Label(LeftFrame,text=user_leave,font=("Vrinda (Headings CS)",13),bg='lightYellow',bd='5',relief='ridge')
                                                                        OSLeaveData.place(x=210,y=310,width='200')
                                                                        ODesignationData=Label(LeftFrame,text=user_desig,font=("Vrinda (Headings CS)",13),bg='lightYellow',bd='5',relief='ridge')
                                                                        ODesignationData.place(x=210,y=410,width='200')
                                                                        ODepartmentData=Label(LeftFrame,text=user_dept,font=("Vrinda (Headings CS)",13),bg='lightYellow',bd='5',relief='ridge')
                                                                        ODepartmentData.place(x=210,y=360,width='200')

                                                                except Exception as e:
                                                                    messagebox.showwarning('DataBase Error',f"{e}")                       # only for checkbox

                                                                c1_v1=StringVar()
                                                                c1_v1.set(' ')
                                                                c2_v1=StringVar()
                                                                c2_v1.set(' ')
                                                                c3_v1=StringVar()
                                                                c3_v1.set(' ')
                                                                c4_v1=StringVar()
                                                                c4_v1.set(' ')
                                                                c5_v1=StringVar()
                                                                c5_v1.set(' ')



                                                                                        # New Data
                                                                checkphoto=Checkbutton(LeftFrame,bg='lightgreen',onvalue='Yes',offvalue=' ',variable=c5_v1,command=lambda:NPhoto(),activebackground='lightgreen')
                                                                checkphoto.place(x=350,y=140)
                                                                checkName=Checkbutton(LeftFrame,bg='lightgreen',onvalue='Yes',offvalue=' ',variable=c1_v1,command=lambda:NcheckName(),activebackground='lightgreen')
                                                                checkName.place(x='415',y=270)
                                                                checkpic=Checkbutton(LeftFrame,bg='lightgreen',onvalue='Yes',offvalue=' ',variable=c2_v1,command=lambda:NcheckLeave(),activebackground='lightgreen')
                                                                checkpic.place(x='415',y=320)
                                                                checkDesignation=Checkbutton(LeftFrame,bg='lightgreen',onvalue='Yes',offvalue=' ',variable=c3_v1,command=lambda:NcheckDesignation(),activebackground='lightgreen')
                                                                checkDesignation.place(x='415',y=370)
                                                                checkDepartment=Checkbutton(LeftFrame,bg='lightgreen',onvalue='Yes',offvalue=' ',variable=c4_v1,command=lambda:NcheckDepartment(),activebackground='lightgreen')
                                                                checkDepartment.place(x='415',y=420)
                                                                Newdata=Label(RightFrame,text="NEW DATA",bg='lightgreen',font=('Bernard MT Condensed',30,'bold'))
                                                                Newdata.pack()
                                                                Newphoto=Label(RightFrame,text='New photo\n like:-D:/picture Name.jpg',bd=2,relief='groove')
                                                                Newphoto.place(x=130,y=55,width=200,height=200)
                                                                NUName=Label(RightFrame,text="New Name",font=("Vrinda (Headings CS)",20),bg='lightgreen')
                                                                NUName.place(x=10,y=260)
                                                                NSLeave=Label(RightFrame,text="New Leave",font=("Vrinda (Headings CS)",20),bg='lightgreen')
                                                                NSLeave.place(x=10,y=310)
                                                                NDesignation=Label(RightFrame,text="New Designation",font=("Vrinda (Headings CS)",20),bg='lightgreen')
                                                                NDesignation.place(x=10,y=360)
                                                                NDepartment=Label(RightFrame,text="New Department",font=("Vrinda (Headings CS)",20),bg='lightgreen')
                                                                NDepartment.place(x=10,y=410)

                                                                                        # only for UserUpdate Input
                                                                NewName = StringVar()
                                                                NewLeave = StringVar()
                                                                NewDesignation=StringVar()
                                                                NewDepartment=StringVar()
                                                                Newimgupdate=StringVar()

                                                                NewName.set('')
                                                                NewLeave.set('')
                                                                NewDesignation.set('')
                                                                NewDepartment.set('')
                                                                Newimgupdate.set('')


                                                                NewBrowser=Button(RightFrame,text='Browser',state='disabled',font=('Vrinda (Body CS)',10,"bold"),command=lambda:selectPic())
                                                                NewBrowser.place(x=350,y=140)
                                                                UPDATEIMAGEpath=Entry(RightFrame,textvariable=Newimgupdate,state='disabled')
                                                                UPDATEIMAGEpath.place(x=335,y=170,width=100)
                                                                NNameData=Entry(RightFrame,font=("Vrinda (Headings CS)",20),textvariable=NewName,bg='lightYellow',bd='5',relief='ridge',state='disabled')
                                                                NNameData.place(x=220,y=260,width='200')
                                                                NSLeaveData=Entry(RightFrame,font=("Vrinda (Headings CS)",20),textvariable=NewLeave,bg='lightYellow',bd='5',relief='ridge',state='disabled')
                                                                NSLeaveData.place(x=220,y=310,width='200')
                                                                NDesignationData=Entry(RightFrame,font=("Vrinda (Headings CS)",20),textvariable=NewDesignation,bg='lightYellow',bd='5',relief='ridge',state='disabled')
                                                                NDesignationData.place(x=220,y=360,width='200')
                                                                NDepartmentData=Entry(RightFrame,font=("Vrinda (Headings CS)",20),textvariable=NewDepartment,bg='lightYellow',bd='5',relief='ridge',state='disabled')
                                                                NDepartmentData.place(x=220,y=410,width='200')

                                                                                        # Brows Images
                                                                def selectPic():
                                                                    global img
                                                                    Updatefilename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                                                                    filetypes=[("jpg images","*.jpg")])
                                                                    if Updatefilename.count("/") == 1:
                                                                        # print("your picture applicable")
                                                                        img = Image.open(Updatefilename)
                                                                        img = img.resize((200,200))
                                                                        img = ImageTk.PhotoImage(img)
                                                                        Newphoto['image'] = img
                                                                        UPDATEIMAGEpath.insert(0,Updatefilename)
                                                                    else:
                                                                        messagebox.showerror("Error","your picture not applicable")
                                                                

                                                                                            

                                                                                            

                                                                UpBack=Button(root,text='Back',font=('Vrinda (Body CS)',20,"bold"),command=lambda:Update_to_MainUpdate())
                                                                UpBack.place(x=20,y=550)


                                                                UpSubmit=Button(root,text='Submit',font=('Vrinda (Body CS)',20,"bold"),command=lambda:UPDATE_SUBMIT())
                                                                UpSubmit.place(x=850,y=550)




                                                                def Update_to_MainUpdate():
                                                                        UpdateLabel.destroy()
                                                                        LeftFrame.destroy()
                                                                        RightFrame.destroy()
                                                                        olddata.destroy()
                                                                        OUName.destroy()
                                                                        OSLeave.destroy()
                                                                        ODesignation.destroy()
                                                                        ODepartment.destroy()
                                                                        OUNameData.destroy()
                                                                        OSLeaveData.destroy()
                                                                        ODesignationData.destroy()
                                                                        ODepartmentData.destroy()
                                                                        checkName.destroy()
                                                                        checkpic.destroy()
                                                                        checkDesignation.destroy()
                                                                        checkDepartment.destroy()
                                                                        Newdata.destroy()
                                                                        NUName.destroy()
                                                                        NSLeave.destroy()
                                                                        NDesignation.destroy()
                                                                        NDepartment.destroy()
                                                                        NSLeaveData.destroy()
                                                                        NDesignationData.destroy()
                                                                        NDepartmentData.destroy()
                                                                        UpBack.destroy()
                                                                        UpSubmit.destroy()
                                                                        # update()
                                                                        # Ul1.destroy()
                                                                        MainUpdate()


                                                                                        # forName
                                                                def NcheckName():
                                                                            if(c1_v1.get()=='Yes'):
                                                                                NNameData.config(state='normal')
                                                                                                
                                                                            else:
                                                                                NNameData.config(state='disabled')  
                                                                                NewName.set('')
                                                                                                

                                                                                        #for Id 
                                                                def NcheckLeave():
                                                                            if(c2_v1.get()=='Yes'):
                                                                                NSLeaveData.config(state='normal')
                                                                                                
                                                                            else:
                                                                                NSLeaveData.config(state='disabled')   
                                                                                NewLeave.set('')
                                                                                            

                                                                                        # For Designation 
                                                                def NcheckDesignation():
                                                                                if(c3_v1.get()=='Yes'):
                                                                                    NDesignationData.config(state='normal')
                                                                                                
                                                                                else:
                                                                                    NDesignationData.config(state='disabled')    
                                                                                    NewDesignation.set('')
                                                                                                
                                                                                        
                                                                                        # For Department 
                                                                def NcheckDepartment():
                                                                                if(c4_v1.get()=='Yes'):
                                                                                    NDepartmentData.config(state='normal')
                                                                                            
                                                                                else:
                                                                                    NDepartmentData.config(state='disabled')    
                                                                                    NewDepartment.set('')   
                                                                                                

                                                                def NPhoto():
                                                                                if(c5_v1.get()=='Yes'):
                                                                                    NewBrowser.config(state='normal')
                                                                                            
                                                                                    UPDATEIMAGEpath.config(state='normal')
                                                                                else:
                                                                                    NewBrowser.config(state='disabled') 
                                                                                    Newphoto.config(image='') 
                                                                                                
                                                                                    UPDATEIMAGEpath.delete(0,'end')
                                                                                    UPDATEIMAGEpath.config(state='disabled')
                                                                                        


                                                                def UPDATE_SUBMIT():        
                                                                                if NewName.get()!='':
                                                                                    # print(NewName.get())
                                                                                    try:
                                                                                        user_name=NewName.get()
                                                                                        user_name=user_name.upper()
                                                                                        try:
                                                                                            UUmycursor.execute(f"update user set name='{user_name}' where user_id='{user_id}'")
                                                                                            UUmycursor.execute(f"update present set name='{user_name}' where user_id='{user_id}'")
                                                                                            UUmycursor.execute(f"update user_notification set name='{user_name}' where user_id='{user_id}'")
                                                                                            
                                                                                            UUmycursor.execute(f"update leaves set name='{user_name}' where user_id='{user_id}'")
                                                                                            UUmycursor.execute(f"update approve set name='{user_name}' where user_id='{user_id}'")
                                                                                            UUmycursor.execute(f"update admin set name='{user_name}' where user_id='{user_id}'")
                                                                                            con.commit()
                                                                                            c=1
                                                                                            
                                                                                            # Update_to_MainUpdate()
                                                                                            
                                                                                        except Exception as e:
                                                                                                messagebox.showwarning('DataBase Error',f"{e}")
                                                                                    except Exception as e:
                                                                                        messagebox.showwarning('warning',f"{e}")
                                            
                                                                                if NewLeave.get()!='':  
                                                                                    # print(NewLeave.get())
                                                                                    try:
                                                                                        user_leaves=int(NewLeave.get())
                                                                                        try:
                                                                                        
                                                                                            UUmycursor.execute(f"update leaves set total_leave={user_leaves} where user_id={user_id}")
                                                                                            con.commit()
                                                                                            c=2
                                                                                        
                                                                                            
                                                                                        except Exception as e:
                                                                                                messagebox.showwarning('DataBase Error',f"{e}")
                                                                                                NewLeave.set('')
                                                                                    except Exception as e:
                                                                                        messagebox.showwarning('warning',f"{e}")
                                                                                        NewLeave.set('')
                                                                                                    
                                                                                if NewDesignation.get()!='':
                                                                                    try:
                                                                                        user_desig=NewDesignation.get()
                                                                                        user_desig=user_desig.upper()
                                                                                        try:
                                                                                            UUmycursor.execute(f"update user set designation='{user_desig}' where user_id='{user_id}'")
                                                                                            con.commit()
                                                                                            c=3                                              
                                                                                        
                                                                                            
                                                                                        except Exception as e:
                                                                                                messagebox.showwarning('DataBase Error',f"{e}")
                                                                                    except Exception as e:
                                                                                        messagebox.showwarning('warning',f"{e}")
                                                                                    # print(NewDesignation.get())
                                                                                            
                                                                                                    
                                                                                if NewDepartment.get()!='':
                                                                                    # print(NewDepartment.get())
                                                                                    try:
                                                                                        # user_pic=Newimgupdate.get()
                                                                                        user_dept=(NewDepartment.get()).upper()

                                                                                        try:
                                                                                            UUmycursor.execute(f"update user set department='{user_dept}' where user_id='{user_id}'")
                                                                                            UUmycursor.execute(f"update present set department='{user_dept}' where user_id='{user_id}'")
                                                                                            con.commit()
                                                                                            c=4
                                                                                                                            
                                                                                        except Exception as e:
                                                                                                messagebox.showwarning('DataBase Error',f"{e}")
                                                                                    except Exception as e:
                                                                                        messagebox.showwarning('warning',f"{e}")
                                                                                    
                                                                                                
                                                                                                    
                                                                                if Newimgupdate.get()!='':
                                                                                    # print(Newimgupdate.get())
                                                                                    try:
                                                                                        user_pic=Newimgupdate.get()
                                                                                        try:
                                                                                            if 'jpg' in user_pic:
                                                                                                UUmycursor.execute(f"update user set picture=load_file('{user_pic}') where user_id='{user_id}'")
                                                                                                con.commit()
                                                                                                c=5
                                                                                            
                                                                                            else:
                                                                                                print("file extension not valid")
                                                                                    
                                                                                        except Exception as e:
                                                                                                messagebox.showwarning('DataBase Error',f"{e}")
                                                                                    except Exception as e:
                                                                                        messagebox.showwarning('warning',f"{e}")
                                                                                if c==1 or c==2 or c==3 or c==4 or c==5 :
                                                                                    Update_to_MainUpdate()
                                                                                    Ul5=Label(root,text='-:Successfully Uptodate:-',fg='green',font=("Calibri Light (Headings)",30))
                                                                                    Ul5.place(x=300,y=500)
                                                                                    Ul5.after(3000, lambda: Ul5.config(text=''))
                                                            else:
                                                                messagebox.showwarning('warning',"Your Id is not Granted")  
                                                                UUI.set('')
                                                        except Exception as e:
                                                            messagebox.showwarning('warning',f"{e}")  
                                                            UUI.set('') 

            
                                
                                            # Update Page End-------------------------------------------------------------------------
                                            
                                             # Delete Page Start--------------------------------------------------------------------------
                                            def MainDelete():
                                                
                                                titel3.destroy()
                                                insert.destroy()
                                                Update.destroy()
                                                Delete.destroy()
                                                Logout.destroy()
                                                VIEW.destroy()
                                                adminhomeframe.destroy()
                                                AName.destroy()
                                                NoticeButton.destroy()
                                                
                                                dtitel=Label(root,text="DELETE PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                dtitel.place(x=0,y=0,relwidth=1)
                                                
                                                DeleteFrame=Frame(root,bg='peach puff',relief='ridge',bd='15')
                                                DeleteFrame.place(x=300,y=100,height=200,width=400)
                                                UserDelete=Button(DeleteFrame,text="User",font='Calibri_Light 15 bold',padx=5,pady=5,activebackground="lightblue",command=lambda:userDelete())
                                                UserDelete.place(x=100,y=10)
                                                adminDelete=Button(DeleteFrame,text="Admin",font='Calibri_Light 15 bold',padx=5,pady=5,activebackground="lightblue",command=lambda:AdminDelete())
                                                adminDelete.place(x=200,y=10)
                                                Backtoadminhome=Button(DeleteFrame,text="Back to admin",font='Calibri_Light 15 bold',padx=5,pady=5,activebackground="lightblue",command=lambda:BacktoAdminHome())
                                                Backtoadminhome.place(x=115,y=80)   
                                                
                                                # Back to admin Home Page
                                                def BacktoAdminHome():
                                                    dtitel.destroy()
                                                    UserDelete.destroy()
                                                    adminDelete.destroy()
                                                    Backtoadminhome.destroy()
                                                    Adminhome()
                                                    DeleteFrame.destroy()
                                                  # User Deletepage start----------------------------------------------------------------- 
                                                def userDelete():
                                                    dtitel.destroy()
                                                    UserDelete.destroy()
                                                    adminDelete.destroy()
                                                    Backtoadminhome.destroy()
                                                    DeleteFrame.destroy()
                                                    DUI=StringVar()
                                                    DUsertitle=Label(root,text="DELETE PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                    DUsertitle.place(x=0,y=0,relwidth=1)
                                                    Duserframe=Frame(root,bg='bisque1',relief='sunken',bd='5')
                                                    Duserframe.place(x=300,y=100,width=400,height=250)
                                                    DUserLabel=Label(Duserframe,text='Enter Id',font='Calibri_Light 15 bold',bg='bisque1')
                                                    DUserLabel.place(x=40,y=50)
                                                    DUserEntry=Entry(Duserframe,font='Calibri_Light 15 bold',textvariable=DUI)
                                                    DUserEntry.place(x=120,y=50)

                                                    def DUBack():
                                                        DUsertitle.destroy()
                                                        Duserframe.destroy()
                                                        DUserLabel.destroy()
                                                        DUserEntry.destroy()
                                                        DUserSubmit.destroy()
                                                        DUserBack.destroy()
                                                        MainDelete()
                                                                                    
                                                                                    
                                                    def USure():
                                                        con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                        mycursor=con.cursor()
                                                        if DUI.get()=='':
                                                            messagebox.showwarning('warning',"Please Fill The Item")
                                                        else:    
                                                            user_id_lists=[]
                                                            mycursor.execute("select user_id from user")
                                                            for id_pass in mycursor:
                                                                user_ids=id_pass[0]
                                                                user_id_lists.append(user_ids)
                                                            try:
                                                                user_id=int(DUI.get())
                                                                if user_id in user_id_lists:
                                                                    # print("id is granted")
                                                                    DUI.set('') 
                                                                    udser=Toplevel()
                                                                    udser.configure(bg="lightgreen")
                                                                    udser.grab_set()
                                                                    udser.overrideredirect(1)
                                                                    udser.geometry("650x400+450+170")
                                                                    udser.title("Notice")
                                                                    udser.resizable(False,False)
                                                                    try:
                                                                        mycursor.execute(f"select name from user where user_id='{user_id}'")
                                                                        for admin_name in mycursor:
                                                                            admin_name=admin_name[0]
                                                                        # print(user_id)
                                                                        # print(admin_name)

                                                                        DUsertitle=Label(udser,text="CONFORM DELETE PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                                        DUsertitle.place(x=0,y=0,relwidth=1)
                                                                        Duserframe=Frame(udser,bg='bisque1',relief='sunken',bd='5')
                                                                        Duserframe.place(x=30,y=100,width=600,height=250)
                                                                        DUserId=Label(Duserframe,text='Id:-',font='Calibri_Light 20 bold',bg='bisque1')
                                                                        DUserId.place(x=40,y=50)
                                                                        DUserName=Label(Duserframe,text='Name:-',font='Calibri_Light 20 bold',bg='bisque1')
                                                                        DUserName.place(x=40,y=100)
                                                                                                    
                                                                        DUserIddata=Label(Duserframe,text=user_id,font='Calibri_Light 20 bold',bg='lightyellow',bd=2,relief='sunken')
                                                                        DUserIddata.place(x=140,y=50,width=430)
                                                                        DUserNamedata=Label(Duserframe,text=admin_name,font='Calibri_Light 20 bold',bg='lightyellow',relief='sunken')
                                                                        DUserNamedata.place(x=140,y=100,width=430)
                                                                                                    
                                                                        def UCdelete():
                                                                            
                                                                            mycursor.execute(f"delete from user where user_id='{user_id}'")
                                                                            mycursor.execute(f"delete from present where user_id='{user_id}'")
                                                                            mycursor.execute(f"delete from user_notification where user_id='{user_id}'")

                                                                            mycursor.execute(f"delete from leaves where user_id='{user_id}'")
                                                                            mycursor.execute(f"delete from approve where user_id='{user_id}'")
                                                                            mycursor.execute(f"delete from admin where user_id='{user_id}'")
                                                                            con.commit()
                                                                            udser.destroy()
                                                                            UDl1=Label(root,text='-:Successfully Deleted:-',fg='green',font=("Calibri Light (Headings)",30))
                                                                            UDl1.place(x=300,y=500)
                                                                            UDl1.after(3000, lambda: UDl1.config(text=''))
                                                                        yesSubmit=Button(Duserframe,text='YES',font=('Calibri_Light'  'bold'),command=lambda:UCdelete())
                                                                        yesSubmit.place(x=460,y=150)
                                                                        noBack=Button(Duserframe,text='NO',font=('Calibri_Light' 'bold'),command=udser.destroy)
                                                                        noBack.place(x=70,y=150)

                                                                    except Exception as e:
                                                                        messagebox.showwarning("Database Error",f"{e}")
                                                                else:
                                                                    messagebox.showwarning("warning","id is not granted")
                                                                    DUI.set('')
                                                            except Exception as e:
                                                                messagebox.showwarning("warning",f"{e}")
                                                                DUI.set('')  
                                                                                    
                                                    DUserSubmit=Button(Duserframe,text='Submit',font=('Calibri_Light'  'bold'),command=USure)
                                                    DUserSubmit.place(x=260,y=100)
                                                    DUserBack=Button(Duserframe,text='Back',font=('Calibri_Light' 'bold'),command=DUBack)
                                                    DUserBack.place(x=70,y=100)
                                                    
                                                    #User Delete PAge End----------------------------------------------------------------
                                                
                                                
                                                # Admin Delete Page Start----------------------------------------------------------------
                                                
                                                def AdminDelete():
                                                        con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                        mycursor=con.cursor()
                                                        dtitel.destroy()
                                                        UserDelete.destroy()
                                                        adminDelete.destroy()
                                                        Backtoadminhome.destroy()
                                                        DeleteFrame.destroy()
                                                        DAI=StringVar()
                                                        DAdmintitle=Label(root,text="DELETE PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                        DAdmintitle.place(x=0,y=0,relwidth=1)
                                                        DAdminframe=Frame(root,bg='bisque1',relief='sunken',bd='5')
                                                        DAdminframe.place(x=300,y=100,width=400,height=250)

                                                        DAdminLabel=Label(DAdminframe,text='Enter Id',font='Calibri_Light 15 bold',bg='bisque1')
                                                        DAdminLabel.place(x=40,y=50)
                                                        DAdminEntry=Entry(DAdminframe,font='Calibri_Light 15 bold',textvariable=DAI)
                                                        DAdminEntry.place(x=120,y=50)

                                                        def DABack():  # Back to Main Delete Page
                                                            DAdmintitle.destroy()
                                                            DAdminframe.destroy()
                                                            DAdminLabel.destroy()
                                                            DAdminEntry.destroy()
                                                            DAdminSubmit.destroy()
                                                            DAdminBack.destroy()
                                                            MainDelete()
                                                                                        
                                                        def ASure():  #View last admin view
                                                            con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                            mycursor=con.cursor()
                                                            if DAI.get()=='':                         
                                                                messagebox.showwarning('warning',"Please Fill The Item")
                                                            else: 
                                                                
                                                                user_id_list=[]
                                                                mycursor.execute("select user_id from admin")
                                                                for id_pass in mycursor:
                                                                    user_ids=id_pass[0]
                                                                    user_id_list.append(user_ids)
                                                                try:
                                                                    user_id=int(DAI.get())
                                                                    if user_id in user_id_list:
                                                                        # print("id is granted")
                                                                        DAI.set('')
                                                                        admin=Toplevel()
                                                                        admin.grab_set()
                                                                        admin.overrideredirect(1)
                                                                        admin.configure(bg="lightgreen")

                                                                        admin.geometry("650x400+450+170")
                                                                        admin.title("Notice")
                                                                        admin.resizable(False,False)
                                                                        DAdmintitle=Label(admin,text="CONFORM DELETE PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                                        DAdmintitle.place(x=0,y=0,relwidth=1)
                                                                        DAdminFrame=Frame(admin,bg='bisque1',relief='sunken',bd='5')
                                                                        DAdminFrame.place(x=25,y=100,width=600,height=250)
                                                                        try:
                                                                            mycursor.execute(f"select name from admin where user_id='{user_id}'")
                                                                            for admin_name in mycursor:
                                                                                admin_name=admin_name[0]
                                                                            # print(user_id)
                                                                            # print(admin_name)
                                                                                        
                                                                            DAdminId=Label(DAdminFrame,text='Id:-',font='Calibri_Light 20 bold',bg='bisque1')
                                                                            DAdminId.place(x=40,y=50)
                                                                            DAdminName=Label(DAdminFrame,text='Name:-',font='Calibri_Light 20 bold',bg='bisque1')
                                                                            DAdminName.place(x=40,y=100)
                                                                            
                                                                            DAdminIddata=Label(DAdminFrame,text=user_id,font='Calibri_Light 20 bold',bg='lightyellow',bd=2,relief='sunken')
                                                                            DAdminIddata.place(x=140,y=50,width=430)
                                                                            DAdminNamedata=Label(DAdminFrame,text=admin_name,font='Calibri_Light 17 bold',bg='lightyellow',relief='sunken')
                                                                            DAdminNamedata.place(x=140,y=100,width=430)
                                                                            
                                                                            yesSubmit=Button(DAdminFrame,text='YES',font=('Calibri_Light'  'bold'),command=lambda:ACdelete())
                                                                            yesSubmit.place(x=460,y=150)
                                                                            noBack=Button(DAdminFrame,text='NO',font=('Calibri_Light' 'bold'),command=admin.destroy)
                                                                            noBack.place(x=70,y=150)
                                                                            def ACdelete():
                                                                                con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                                                mycursor=con.cursor()
                                                                                mycursor.execute(f"delete from admin where user_id='{user_id}'")
                                                                                con.commit()
                                                                                admin.destroy()
                                                                                ADl1=Label(root,text=f"-:{admin_name} You are Not now as a Admin:-",fg='green',font=("Calibri Light (Headings)",30))
                                                                                ADl1.place(x=120,y=500)
                                                                                ADl1.after(3000, lambda: ADl1.config(text=''))

                                                                        except Exception as e:
                                                                            messagebox.showwarning("Database Error",f"{e}")
                                                                            admin.destroy()
                                                                    else:
                                                                        messagebox.showwarning("warning","id is not granted")
                                                                        DAI.set('')
                                                                except Exception as e:
                                                                    messagebox.showwarning("warning",f"{e}")
                                                                    DAI.set('')
                                                                                                                    
                                                                                        
                                                                                        
                                                        #Delete Page Buttons 
                                                        DAdminSubmit=Button(DAdminframe,text='Submit',font=('Calibri_Light'  'bold'),command=lambda:ASure())
                                                        DAdminSubmit.place(x=260,y=100)
                                                        DAdminBack=Button(DAdminframe,text='Back',font=('Calibri_Light' 'bold'),command=DABack)
                                                        DAdminBack.place(x=70,y=100)
                                                # Admin Delete Page End----------------------------------------------------------------
                                        
                                            # Delete Page End---------
                                            # View Page Start----------------------------------------------------------------
                                            def MainViewPage():
                                                titel3.destroy()
                                                insert.destroy()
                                                Update.destroy()
                                                Delete.destroy()
                                                Logout.destroy()
                                                VIEW.destroy()
                                                adminhomeframe.destroy()
                                                AName.destroy()
                                                NoticeButton.destroy()
                                                
                                                viewpage=Label(root,text="-:Main View Page:-",font=("times new roman",50),bg='GREEN',fg="WHIte")
                                                viewpage.pack(fill=X)
                                                viewmanu=Frame(root,bg='lightyellow',bd=5,relief='ridge')
                                                viewmanu.place(x=280,y=150,height=250,width=500) 
                                                
                                                Admin_View_User=Button(viewmanu,text=" User\n   View  ",font=("times new roman",20),command=lambda:admin_View_User())
                                                Admin_View_User.place(x=20,y=20)

                                                Admin_View_Attedndence=Button(viewmanu,text="Attenence \nView",font=("times new roman",20),command=lambda:admin_View_UserAttendence())
                                                Admin_View_Attedndence.place(x=160,y=20)
                                                
                                                Admin_View_totaluser=Button(viewmanu,text="View Total \nUser",font=("times new roman",20),command=lambda:Total_User())
                                                Admin_View_totaluser.place(x=320,y=20)

                                                back_to_mainadminpage=Button(viewmanu,text='Back to main \nadmin page',font=("times new Roman",20),command=lambda:back_to_main_adminpage())
                                                back_to_mainadminpage.place(x=155,y=120)
                                                
                                                # Back to Main Admin page----------------------------------------------------------------
                                                def back_to_main_adminpage():
                                                    viewpage.destroy()
                                                    viewmanu.destroy() 
                                                    Admin_View_User.destroy()
                                                    Admin_View_Attedndence.destroy()
                                                    Admin_View_totaluser.destroy()
                                                    back_to_mainadminpage.destroy()
                                                    Adminhome()  
                                                                      
                                                # Total_User Started----------------------------------------------------------------
                                                def Total_User():  
                                                    viewpage.destroy()
                                                    viewmanu.destroy() 
                                                    Admin_View_User.destroy()
                                                    Admin_View_Attedndence.destroy()
                                                    Admin_View_totaluser.destroy()
                                                    back_to_mainadminpage.destroy() 
                                                    con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                    mycur=con.cursor()
                                                    mycur.execute("select user_id from user")
                                                    user_id_lists=[]
                                                    for id_pass in mycur:
                                                        user_ids=id_pass[0]
                                                        user_id_lists.append(user_ids)

                                                    total_user=len(user_id_lists)


                                                    title=Label(root,text="-:Total User:-",font=("times new roman",50),bg='GREEN',fg="WHIte")
                                                    title.pack(fill=X)
                                                    totaluser=Label(root,text="Total User:-",font=("times new roman",40))
                                                    totaluser.place(x=300,y=100)
                                                    totaluservalue=Label(root,text=total_user,font=("times new roman",40))
                                                    totaluservalue.place(x=600,y=100)
                                                    TotalFrame=Frame(root,bg='lightblue',bd=5,relief='groove')
                                                    TotalFrame.place(x=50,y=200,width=900,height=400)

                                                    scroll=Scrollbar(TotalFrame)
                                                    scroll.pack(side=RIGHT,fill=Y)


                                                    TotalName=Label(TotalFrame,text="Name\n",font=("times new roman",20),bg='lightblue')
                                                    TotalName.place(x=70,y=5)
                                                    TotalID=Label(TotalFrame,text="ID",font=("times new roman",20),bg='lightblue')
                                                    TotalID.place(x=400,y=5)
                                                    TotalDEGINATION=Label(TotalFrame,text="Designation",font=("times new roman",20),bg='lightblue')
                                                    TotalDEGINATION.place(x=540,y=5)
                                                    TotalDepertment=Label(TotalFrame,text="Depertment",font=("times new roman",20),bg='lightblue')
                                                    TotalDepertment.place(x=730,y=5)
                                                    # total_name_data=Label(TotalFrame,font=("times new roman",20))
                                                    # total_name_data.place(x=20,y=50)

                                                    BButton=Button(root,text='Close',font=("times new roman",15),command=lambda:clear())
                                                    BButton.place(x=70,y=150)
                                                    SeeButton=Button(root,text='View',font=("times new roman",15),command=lambda:See())
                                                    SeeButton.place(x=900,y=150)
                                                    SButton=Button(root,text='Save',font=("times new roman",15),command=lambda:Save(),state='disabled')
                                                    SButton.place(x=480,y=600)
                                                    
                                                    try:
                                                        def See():
                                                            cone=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                            # print("hii")
                                                            mycu=cone.cursor()
                                                            mycu.execute("select user_id,name,department,designation from user") 
                                                            SButton.config(state='normal')
                                                            Total_Name=Listbox(TotalFrame,font=(10),yscrollcommand=scroll.set)
                                                            Total_Name.place(x=20,y=40,width=300,height=330)
                                                            scroll.config(command=Total_Name.yview)
                                                            
                                                            Total_ID=Listbox(TotalFrame,font=(10),yscrollcommand=scroll.set)
                                                            Total_ID.place(x=400,y=40,width=50,height=330)
                                                            scroll.config(command=Total_ID.yview)
                                                            
                                                            Total_Designation=Listbox(TotalFrame,font=(10),yscrollcommand=scroll.set)
                                                            Total_Designation.place(x=530,y=40,width=150,height=330)
                                                            scroll.config(command=Total_Designation.yview)
                                                            
                                                            Total_Department=Listbox(TotalFrame,font=(10),yscrollcommand=scroll.set)
                                                            Total_Department.place(x=750,y=40,width=100,height=330)
                                                            
                                                            scroll.config(command=Total_Department.yview)
                                                            
                                                            for out_data in mycu:
                                                                out_user_id=out_data[0]
                                                                out_user_name=out_data[1]
                                                                out_department=out_data[2]
                                                                out_designation=out_data[3]   
                                                                
                                                                Total_Name.insert(END,f"{out_user_name}")
                                                                Total_ID.insert(END,f"{out_user_id}")
                                                                Total_Designation.insert(END,f"{out_designation}")
                                                                Total_Department.insert(END,f"{out_department}")
                                                        def Save():
                                                            cone=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                            # print("hii")
                                                            mycu=cone.cursor()
                                                            file=filedialog.asksaveasfile(filetypes=[('exel files','*.csv')],defaultextension='.csv',
                                                                                        title='Save File',mode='w')   
                                                            # mycu.execute("select user_id from user")
                                                            mycu.execute("select user_id,name,department,designation from user")
                                                            for data in mycu:
                                                                # print(data)
                                                                out_user_id=data[0]
                                                                out_user_name=data[1]
                                                                out_department=data[2]
                                                                out_designation=data[3]   
                                                                # print(out_user_id, out_user_name, out_department, out_designation)
                                                                file.write(f"{out_user_id},{out_user_name},{out_department},{out_designation} \n")   
                                                                # file.close()
                                                    except Exception as e:
                                                        messagebox.showerror("Database error: ",f"{e}")
                                                        
                                                        
                                                    def clear():
                                                                TotalFrame.destroy()
                                                                title.destroy()
                                                                totaluser.destroy()
                                                                totaluservalue.destroy()
                                                                BButton.destroy()
                                                                SeeButton.destroy()
                                                                SButton.destroy()
                                                                MainViewPage()
                                                       
                                                # Admin see Total User End----------------------------------------------------------------
                                                # Admin see User Details---------------------------------------------------------------- 
                                                def admin_View_User():
                                                    
                                                    viewpage.destroy()
                                                    viewmanu.destroy() 
                                                    Admin_View_User.destroy()
                                                    Admin_View_Attedndence.destroy()
                                                    Admin_View_totaluser.destroy()
                                                    back_to_mainadminpage.destroy()
                                                    ASUI=StringVar()
                                                    Adminseetitle=Label(root,text="ADMIN SEE THE USER DETAIL PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")
                                                    Adminseetitle.place(x=0,y=0,relwidth=1)
                                                    Adminseeframe=Frame(root,bg='bisque1',relief='sunken',bd='5')
                                                    Adminseeframe.place(x=300,y=100,width=400,height=250)
                                                    AdminseeLabel=Label(Adminseeframe,text='Enter Id',font='Calibri_Light 15 bold',bg='bisque1')
                                                    AdminseeLabel.place(x=40,y=50)
                                                    AdminseeEntry=Entry(Adminseeframe,font='Calibri_Light 15 bold',textvariable=ASUI)
                                                    AdminseeEntry.place(x=120,y=50)
                                                    
                                                    AdminseeSubmit=Button(Adminseeframe,text='Submit',font=('Calibri_Light'  'bold'),command=lambda:admin_see_user_details())
                                                    AdminseeSubmit.place(x=260,y=100)
                                                    AdminseeBack=Button(Adminseeframe,text='Back',font=('Calibri_Light' 'bold'),command=lambda:Adminseepage_to_optionsview())
                                                    AdminseeBack.place(x=70,y=100)
                                                    
                                                    
                                                    def admin_see_user_details():
                                                        if ASUI.get()=='':
                                                            messagebox.showwarning("warning","please fill the blank")
                                                        else: 
                                                            cone=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                                # print("hii")
                                                            avmycu=cone.cursor()
                                                            avmycu.execute("select user_id from user")
                                                            user_id_lists=[]
                                                            for id_pass in avmycu:
                                                                user_ids=id_pass[0]
                                                                user_id_lists.append(user_ids)
                                                            
                                                            try:
                                                                # cone=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                                # # print("hii")
                                                                # avmycu=cone.cursor()
                                                                user_id=int(ASUI.get())
                                                                if user_id in user_id_lists:
                                                                    Adminseetitle.destroy()
                                                                    Adminseeframe.destroy()
                                                                    AdminseeLabel.destroy()
                                                                    AdminseeEntry.destroy()
                                                                    AdminseeSubmit.destroy()
                                                                    AdminseeBack.destroy()
                                                                    avmycu.execute(f"select user.name,user.picture,user.department,user.designation,leaves.total_leave, leaves.leave_taken, leaves.remaining_leave from user  INNER JOIN leaves ON user.user_id=leaves.user_id where user.user_id='{user_id}'")
                                                                    for details in avmycu:
                                                                        user_name=details[0]
                                                                        user_pic=details[1]
                                                                    
                                                                        user_desig=details[2]
                                                                        user_dept=details[3]
                                                                        user_total_leave=details[4]
                                                                        user_leave_taken=details[5]
                                                                        user_remaining_leave=details[6]                  
                                                                    
                                                                    if user_leave_taken ==None:
                                                                        user_leave_taken=0
                                                                    else:
                                                                        user_leave_taken=user_leave_taken
                                                                        
                                                                        
                                                                    if user_remaining_leave == None:
                                                                        user_remaining_leave=0
                                                                    else:
                                                                        user_remaining_leave=user_remaining_leave

                                                                    ASUserTitel=Label(root,text="Your All Data",font=("times new roman",50),bg='GREEN',fg="WHIte")
                                                                    ASUserTitel.pack(fill=X)

                                                                    ASUserdataViewe=Frame(root,bd=5,relief='raised',bg='lightblue')
                                                                    ASUserdataViewe.place(x=400,y=180,width=550,height=390)       
                                                                    ASUserimgViewe=Frame(root,bd=5,relief='raised',bg='lightblue')
                                                                    ASUserimgViewe.place(x=50,y=180,width=300,height=390) 
                                                                    
                                                                    
                                                                    ASDatabase_UserName=Label(ASUserdataViewe,text="Your Name:-",font=("times new roman",25),bg='lightblue')
                                                                    ASDatabase_UserName.place(x=15,y=15)
                                                                    ASDATABASE_USERID=Label(ASUserdataViewe,text="Your Id:-",font=("times new roman",25),bg='lightblue')
                                                                    ASDATABASE_USERID.place(x=15,y=60)
                                                                    ASDATABASE_DESIGNATION=Label(ASUserdataViewe,text="Your Designation:-",font=("times new roman",25),bg='lightblue')
                                                                    ASDATABASE_DESIGNATION.place(x=15,y=105)
                                                                    ASDATABASE_DEPARTMENE=Label(ASUserdataViewe,text="Your Depertment:-",font=("times new roman",25),bg='lightblue')
                                                                    ASDATABASE_DEPARTMENE.place(x=15,y=155)
                                                                    ASTotalLeave1=Label(ASUserdataViewe,text="Total Leave:-",font=("times new roman",25),bg='lightblue')
                                                                    ASTotalLeave1.place(x=15,y=205)
                                                                    ASLeaveTaken1=Label(ASUserdataViewe,text="Leave Taken:-",font=("times new roman",25),bg='lightblue')
                                                                    ASLeaveTaken1.place(x=15,y=255)
                                                                
                                                                    ASRemainingLeave1=Label(ASUserdataViewe,text="Remaining Leave:-",font=("times new roman",25),bg='lightblue')
                                                                    ASRemainingLeave1.place(x=15,y=305)
                                                                        #             # msg
                                                                        # total="                                "
                                                                    ASTDatabase_UserName=Label(ASUserdataViewe,text=user_name,bd=4,relief='groove',font=("times new roman",15))
                                                                    ASTDatabase_UserName.place(x=275,y=15,width=250,height='40')
                                                                    
                                                                    ASTDATABASE_USERID=Label(ASUserdataViewe,text=user_id,bd=4,relief='groove',font=("times new roman",15))
                                                                    ASTDATABASE_USERID.place(x=275,y=60,width=250,height='40')
                                                                    
                                                                    ASTDATABASE_DESIGNATION=Label(ASUserdataViewe,text=user_desig,bd=4,relief='groove',font=("times new roman",15))
                                                                    ASTDATABASE_DESIGNATION.place(x=275,y=105,width=250,height='40')
                                                                    
                                                                    ASTDATABASE_DEPARTMENE=Label(ASUserdataViewe,text=user_dept,bd=4,relief='groove',font=("times new roman",15))
                                                                    ASTDATABASE_DEPARTMENE.place(x=275,y=155,width=250,height='40')
                                                                    
                                                                    ASTTotalLeave1=Label(ASUserdataViewe,text=user_total_leave,bd=4,relief='groove',font=("times new roman",15))
                                                                    ASTTotalLeave1.place(x=275,y=205,width=250,height='40')                  
                                                                    
                                                                    ASTLeaveTaken1=Label(ASUserdataViewe,text=user_leave_taken,bd=4,relief='groove',font=("times new roman",15))
                                                                    ASTLeaveTaken1.place(x=275,y=255,width=250,height='40')
                                                                    
                                                                    ASTRemainingLeave1=Label(ASUserdataViewe,text=user_remaining_leave,bd=4,relief='groove',font=("times new roman",15))
                                                                    ASTRemainingLeave1.place(x=275,y=305,width=250,height='40')
                                                                    
                                                                    ASBack_User_View=Button(root,text='Back',activebackground='lightblue',font='20',command=lambda: Back_TO_Adminsee_user())
                                                                    ASBack_User_View.place(x=20,y=100,width=100,height=50)
                                                                    
                                                                    with open('images.jpg','wb') as f:
                                                                            f.write(user_pic)
                                                                            img=Image.open("images.jpg")
                                                                            img=img.resize((200,200))
                                                                            img=ImageTk.PhotoImage(img)
                                                                            
                                                                            ASIDatabase_UserImg=Label(ASUserimgViewe,image=img,bd=4,relief='groove')
                                                                            ASIDatabase_UserImg.image=img
                                                                            ASIDatabase_UserImg.place(x=20,y=70,width=250,height='250')
                                                                    
                                                                    def Back_TO_Adminsee_user():
                                                                        ASUserTitel.destroy()
                                                                        ASUserdataViewe.destroy() 
                                                                        ASUserimgViewe.destroy()
                                                                        ASDatabase_UserName.destroy()
                                                                        ASDATABASE_USERID.destroy()
                                                                        ASDATABASE_DESIGNATION.destroy()
                                                                        ASDATABASE_DEPARTMENE.destroy()
                                                                        ASTotalLeave1.destroy()
                                                                        ASLeaveTaken1.destroy()
                                                                        ASRemainingLeave1.destroy()
                                                                        ASTDatabase_UserName.destroy()
                                                                        ASTDATABASE_USERID.destroy()
                                                                        ASTDATABASE_DESIGNATION.destroy()
                                                                        ASTDATABASE_DEPARTMENE.destroy()
                                                                        ASTTotalLeave1.destroy()
                                                                        ASTRemainingLeave1.destroy()
                                                                        ASTLeaveTaken1.destroy()
                                                                        ASBack_User_View.destroy()
                                                                        ASIDatabase_UserImg.destroy()
                                                                        admin_View_User()
                                                                else:
                                                                    messagebox.showwarning("warning","Your Id not found")
                                                                    ASUI.set('')    
                                                            except Exception as e:
                                                                messagebox.showwarning("Database Error",f"{e}")   
                                                                
                                                                ASUI.set('')
                                                    
                                                    def Adminseepage_to_optionsview():
                                                        Adminseetitle.destroy()
                                                        Adminseeframe.destroy()
                                                        AdminseeLabel.destroy()
                                                        AdminseeEntry.destroy()
                                                        AdminseeSubmit.destroy()
                                                        AdminseeBack.destroy()
                                                        MainViewPage()
                                                
                                                
                                                
                                                    # Admin See User Details end----------------------------------------------------------------
                                                
                                                
                                                    # Admin see Attendnce Details start---------------------------------------------------------------- 
                                                def admin_View_UserAttendence():
                                                    
                                                        viewpage.destroy()
                                                        viewmanu.destroy() 
                                                        Admin_View_User.destroy()
                                                        Admin_View_Attedndence.destroy()
                                                        Admin_View_totaluser.destroy()
                                                        back_to_mainadminpage.destroy()
                                                    
                                                        AttendenceViewtitle=Label(root,text="ATTENDENCE VIEW PAGE",font=("times new roman",40),bg='GREEN',fg="WHIte")

                                                        AttendenceViewtitle.place(x=0,y=0,relwidth=1)

                                                        AttendenceViewFream=Frame(root,bg='lightGREEN',bd=5,relief='groove')

                                                        AttendenceViewFream.place(x=200,y=125,height=300,width=550)
                                                        # text=StringVar()

                                                        Attendenceexcelcreate=Label(root,font=("times new roman",30),fg='green')
                                                        Attendenceexcelcreate.place(x=255,y=70)

                                                        # Date Entry Start Hear  
                                                        cal1=DateEntry(AttendenceViewFream,selectmode='day',date_pattern='yyyy-mm-dd',font=('times new roman',20))
                                                        cal1.place(x=50,y=10)
                                                        cal2=DateEntry(AttendenceViewFream,selectmode='day',date_pattern='yyyy-mm-dd',font=('times new roman',20))
                                                        cal2.place(x=260,y=10)
                                                        # Date Entry End Hear


                                                        # for single Id
                                                        OneId=Button(AttendenceViewFream,text="Single User",font=("times new roman",20),command=lambda:EnterID())
                                                        OneId.place(x=280,y=50)
                                                        ID=StringVar()
                                                        enterID=Label(AttendenceViewFream,text="Please enter User ID:-",font=("times new roman",20),bg='lightgreen')
                                                        enterID.place(x=30,y=115)
                                                        EnterId=Entry(AttendenceViewFream,font=("times new roman",20),state='disabled',textvariable=ID)
                                                        EnterId.place(x=280,y=115,width=230)


                                                        showdetails=Label(AttendenceViewFream,font=("times new roman",20))
                                                        showdetails.place(x=20,y=165,width=500)
                                                        SendButton=Button(AttendenceViewFream,text="Send",font=("times new roman",15),command=lambda:SEND(),state="disabled")
                                                        SendButton.place(x=455,y=115)

                                                        ViewSave=Button(AttendenceViewFream,text="Save",font=("times new roman",20),command=lambda:Savefile(),state='disabled')
                                                        ViewSave.place(x=130,y=230)
                                                        Viewclear=Button(AttendenceViewFream,text="Clear",font=("times new roman",20),command=lambda:clearalldata())
                                                        Viewclear.place(x=300,y=230)
                                                        Back_to_mainview=Button(root,text="back",font=("times new roman",20),command=lambda:Back_to_main_viewpage())
                                                        Back_to_mainview.place(x=30,y=80)
                                                        
                                                        
                                                        
                                                        
                                                        def EnterID():
                                                            EnterId.config(state='normal')
                                                            showdetails.config(text='')
                                                            SendButton.config(state='normal')
                                                                
                                                            
                                                            
                                                            
                                                        def SEND():
                                                            con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                            SUmycursor=con.cursor()
                                                            if ID.get()=='':
                                                                    messagebox.showwarning("warning","Please Enter Your Id")
                                                                    SendButton.config(state='disabled')
                                                                    EnterId.config(state='disabled')
                                                                    showdetails.config(text='')
                                                            else:
                                                                try:
                                                                    user_id=int(ID.get())
                                                                    user_id_lists=[]
                                                                    SUmycursor.execute("select user_id from user")
                                                                    for id_pass in SUmycursor:
                                                                        user_ids=id_pass[0]
                                                                        user_id_lists.append(user_ids)

                                                                    if user_id in user_id_lists:
                                                                        # print("id is granted")
                                                                        SUmycursor.execute(f"select name from user where user_id={user_id}")
                                                                        for user_name in SUmycursor:
                                                                            user_name=user_name[0]
                                                                            # print(user_name)

                                                                    
                                                                        showdetails.config(text=f"Name:- {user_name}")
                                                                        ViewSave.config(state='normal')
                                                                        global c
                                                                        c=1
                                                                    else:
                                                                        messagebox.showerror("error",f"{ID.get()} not Exists")
                                                                        SendButton.config(state='disabled')
                                                                        EnterId.delete(0,'end')
                                                                        EnterId.config(state='disabled')
                                                                        showdetails.config(text='')
                                                                        
                                                                        
                                                                except Exception as e:
                                                                    messagebox.showerror("Database Error",f"{e}")     
                                                                    EnterId.delete(0,'end')
                                                                    SendButton.config(state='disabled')
                                                                    EnterId.config(state='disabled')
                                                                    
                                                            



                                                        # clear alldata

                                                        def clearalldata():
                                                            Attendenceexcelcreate.config(text="-:All data Cleared:-")
                                                            Attendenceexcelcreate.place(x=360)
                                                            Attendenceexcelcreate.after(3000,lambda:Attendenceexcelcreate.config(text=''))
                                                            ID.set('')
                                                            EnterId.config(state='disabled')
                                                            showdetails.config(text='')
                                                            ViewSave.config(state='disabled')
                                                            SendButton.config(state='disabled')
                                                            



                                                        # back to main view----------------------------------------------------------------
                                                        def Back_to_main_viewpage():
                                                            Back_to_mainview.destroy()
                                                            Viewclear.destroy()
                                                            ViewSave.destroy()

                                                            AttendenceViewtitle.destroy()

                                                            AttendenceViewFream.destroy()
                                                            Attendenceexcelcreate.destroy()
                                                            cal1.destroy()
                                                            cal2.destroy()
                                                            AllId.destroy()
                                                            OneId.destroy()
                                                            enterID.destroy()
                                                            EnterId.destroy()
                                                            showdetails.destroy()
                                                            SendButton.destroy()
                                                            MainViewPage()
                                                            
                                                        def AllID():
                                                                con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                                mycurs=con.cursor()
                                                            
                                                                EnterId.config(state='disabled')
                                                                ViewSave.config(state='normal')
                                                                global c
                                                                c=0
                                                                ID.set('')  
                                                                try:
                                                                    user_id_lists=[]
                                                                    mycurs.execute("select user_id from user")
                                                                    for id_pass in mycurs:
                                                                        user_ids=id_pass[0]
                                                                        user_id_lists.append(user_ids)

                                                                    total_user=len(user_id_lists)
                                                                    # print(total_user)
                                                                except Exception as e:
                                                                    messagebox.showerror("Database Error",f"{e}")

                                                                showdetails.config(text=f"Totla User:-{total_user}")


                                                        # convert to excel format and save
                                                        def Savefile():
                                                            if c==1:
                                                                try:
                                                                    # print("hii")
                                                                    con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                                    SUmycursor=con.cursor()
                                                                    start_date=cal1.get()
                                                                    end_date=cal2.get()
                                                                    SUmycursor.execute(f"select present.user_id,present.name,present.department,present.Date,present.arrival_time,present.departure_time,leaves.total_leave,leaves.leave_taken,leaves.remaining_leave from leaves INNER JOIN present ON leaves.user_id=present.user_id where leaves.user_id={ID.get()} AND Date BETWEEN '{start_date}' AND '{end_date}'") 
                                                                    file=filedialog.asksaveasfile(filetypes=[('exel files','*.csv')],defaultextension='.csv',title='Save File',mode='w')  
                                                                    
                                                                    for out_data in SUmycursor:
                                                                            out_user_id=out_data[0]
                                                                            out_user_name=out_data[1]
                                                                            out_department=out_data[2]
                                                                            out_date=out_data[3]
                                                                            out_arrival_time=out_data[4]
                                                                            out_departure_time=out_data[5]
                                                                            out_total_leave=out_data[6]
                                                                            out_leave_taken=out_data[7]
                                                                            out_remaining_leave=out_data[8]
                                                                        
                                                                        # print(out_user_id, out_user_name, out_department, out_date, out_arrival_time, out_departure_time, out_total_leave, out_leave_taken, out_remaining_leave)
                                                                            file.write(f"{out_user_id}, {out_user_name}, {out_department}, {out_date}, {out_arrival_time}, {out_departure_time},{ out_total_leave}, {out_leave_taken},{ out_remaining_leave} \n")   
                                                                    
                                                                
                                                                except Exception as e:
                                                                    messagebox.showerror("Database Error",f"{e}")
                                                                showdetails.config(text='')
                                                                ViewSave.after(300,lambda:ViewSave.config(state='disabled'))
                                                                SendButton.config(state='disabled')
                                                                EnterId.delete(0,'end')
                                                                EnterId.config(state='disabled')
                                                            else:    
                                                                try:
                                                                    con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                                    mycurs=con.cursor()
                                                                    start_date=cal1.get()
                                                                    end_date=cal2.get()

                                                                    mycurs.execute(f"select present.user_id,present.name,present.department,present.Date,present.arrival_time,present.departure_time,leaves.total_leave,leaves.leave_taken,leaves.remaining_leave from leaves INNER JOIN present ON leaves.user_id=present.user_id where Date BETWEEN '{start_date}' AND '{end_date}'") 
                                                                    
                                                                    file=filedialog.asksaveasfile(filetypes=[('exel files','*.csv')],defaultextension='.csv',  title='Save File',mode='w') 
                                                                    for out_data in mycurs:
                                                                                out_user_id=out_data[0]
                                                                                out_user_name=out_data[1]
                                                                                out_department=out_data[2]
                                                                                out_date=out_data[3]
                                                                                out_arrival_time=out_data[4]
                                                                                out_departure_time=out_data[5]
                                                                                out_total_leave=out_data[6]
                                                                                out_leave_taken=out_data[7]
                                                                                out_remaining_leave=out_data[8]
                                                                                # print(out_user_id, out_user_name, out_department, out_date, out_arrival_time, out_departure_time, out_total_leave, out_leave_taken, out_remaining_leave)
                                                                                
                                                                                file.write(f"{out_user_id}, {out_user_name}, {out_department}, {out_date}, {out_arrival_time}, {out_departure_time},{ out_total_leave}, {out_leave_taken},{ out_remaining_leave} \n")   
                                                                                # file.close()
                                                                                    
                                                                        
                                                                except Exception as e:
                                                                    messagebox.showerror("Database Error",f"{e}")
                                                                showdetails.config(text='')
                                                                ViewSave.after(300,lambda:ViewSave.config(state='disabled'))
                                                                SendButton.config(state='disabled')
        
                                                        AllId=Button(AttendenceViewFream,text="All User",font=("times new roman",20),command=lambda:AllID())
                                                        AllId.place(x=100,y=50)
                                                            



                                                        
                                                    
                                                    # Admin see Attendnce Details End---------------------------------------------------------------- 

                                                
                                                
                                                # View Page End----------------------------------------------------------------
                                             
                                            # Notice Part Start----------------------------------------------------------------
                                            def mnotice():
                                                titel3.destroy()
                                                insert.destroy()
                                                Update.destroy()
                                                Delete.destroy()
                                                Logout.destroy()
                                                VIEW.destroy()
                                                adminhomeframe.destroy()
                                                AName.destroy()
                                                NoticeButton.destroy()
                                                
                                                
                                                noticetitle=Label(root,text="-:Admin Send & View Notice:-",font=("times new roman",50),bg='GREEN',fg="WHIte")
                                                noticetitle.pack(fill=X)
                                                noticeFrame=Frame(root,bd=4,relief='raised',bg='lightgreen')
                                                noticeFrame.place(x=250,y=150,height=250,width=500)
                                                back_to_Mainadminpage=Button(noticeFrame,text='Back to main \nadmin page',font=("times new Roman",20),command=lambda:Back_To_Main_Adminpage())
                                                back_to_Mainadminpage.place(x=155,y=120) 
                                                adminsendbutton=Button(noticeFrame,text='Admin Send \n notice',font=("times new Roman",20),command=lambda:goto_send())
                                                adminsendbutton.place(x=65,y=25)
                                                con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                mycursor=con.cursor()
                                            

                                                number=1
                                                adminseenbutton=Button(noticeFrame,text=f'Admin Seen \n notice  {number}',font=("times new Roman",20))
                                                adminseenbutton.place(x=265,y=25)

                                                def Back_To_Main_Adminpage():
                                                    noticeFrame.destroy()
                                                    noticetitle.destroy()
                                                    Adminhome()
                                                    
                                                # admin send Notice Start------------------------------------------
                                                
                                                def goto_send():
                                                    noticeFrame.destroy()
                                                    noticetitle.destroy()
                                                    con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                    Asycursor=con.cursor()
                                                    try:
                                                        Asycursor.execute("select notice from admin_notification where notices_id=7000")
                                                        for notice_details in Asycursor:
                                                            notices=notice_details[0]



                                                        anoticesendtitle=Label(root,text="-:Admin Send Notice:-",font=("times new roman",50),bg='GREEN',fg="WHIte")
                                                        anoticesendtitle.pack(fill=X)
                                                        anoticesendFrame=Frame(root,bd=4,relief='raised',bg='lightgreen')
                                                        anoticesendFrame.place(x=250,y=120,height=450,width=500)
                                                        text=Text(anoticesendFrame,font=("times new roman",15))
                                                        text.place(x=45,y=50,height=300,width=400)
                                                        back_to_mainNotice=Button(anoticesendFrame,text='Back',font=("times new roman",20),command=lambda:amain_back())
                                                        back_to_mainNotice.place(x=100,y=370)
                                                        ASubmitNotice=Button(anoticesendFrame,text='Submit',font=("times new roman",20),command=lambda:amain_submit())
                                                        ASubmitNotice.place(x=200,y=370)
                                                        ADeleteNotice=Button(anoticesendFrame,text='Delete',font=("times new roman",20),command=lambda:amain_Delete())
                                                        ADeleteNotice.place(x=320,y=370)
                                                        todaydate=Label(anoticesendFrame,text='Today',font=("times new roman",18),bg='lightgreen')
                                                        todaydate.place(x=30,y=10)
                                                        cal1=DateEntry(anoticesendFrame,selectmode='day',date_pattern='yyyy-mm-dd',font=(15))
                                                        cal1.place(x=100,y=13,width=150)
                                                        Nextdate=Label(anoticesendFrame,text='Next',font=("times new roman",18),bg='lightgreen')
                                                        Nextdate.place(x=265,y=10)
                                                        cal2=DateEntry(anoticesendFrame,selectmode='day',date_pattern='yyyy-mm-dd',font=(15))
                                                        cal2.place(x=320,y=13,width=150)
                                                    


                                                        def amain_submit():
                                                            con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                            mycursor=con.cursor()
                                                            str=text.get('1.0',END)
                                                            if notices == None or notices =='':
                                                                
                                                                notice=str
                                                                today_date=cal1.get()
                                                                next_date=cal2.get()
                                                                mycursor.execute(f"update admin_notification set notice='{notice}' where notices_id=7000")
                                                                mycursor.execute(f"update admin_notification set Date='{today_date}' where notices_id=7000")
                                                                mycursor.execute(f"update admin_notification set leaves_date='{next_date}' where notices_id=7000")
                                                                con.commit()
                                                                dnl5=Label(root,text='-:Your Notice Successfully Send:-',fg='green',font=("Calibri Light (Headings)",20))
                                                                dnl5.place(x=270,y=580)
                                                                dnl5.after(3000, lambda: dnl5.config(text=''))
                                                                anoticesendtitle.destroy()
                                                                anoticesendFrame.destroy()
                                                                mnotice()
                                                            else:
                                                                messagebox.showerror("Error: ","please delete old msg")
                                                            # print(str)
                                                                text.delete('1.0',END)    
                                                        def amain_back():
                                                            anoticesendtitle.destroy()
                                                            anoticesendFrame.destroy()
                                                            mnotice()
                                                            
                                                        def amain_Delete():
                                                            con=mysql.connector.connect(host="localhost", user="root", password="", database="project")
                                                            dmycursor=con.cursor()
                                                            try:
                                                                dmycursor.execute("select notice from admin_notification where notices_id=7000")
                                                                for notice_details1 in dmycursor:
                                                                    notices1=notice_details1[0]

                                                                if notices1!=None and notices1 !='':
                                                                    dmycursor.execute("update admin_notification set notice='' where notices_id=7000")
                                                                    dmycursor.execute("update admin_notification set Date='' where notices_id=7000")
                                                                    dmycursor.execute("update admin_notification set leaves_date='' where notices_id=7000")
                                                                    con.commit()
                                                                    dnl5=Label(root,text='-:Old Notice Successfully Deleted:-',fg='green',font=("Calibri Light (Headings)",20))
                                                                    dnl5.place(x=270,y=580)
                                                                    dnl5.after(3000, lambda: dnl5.config(text=''))
                                                                    anoticesendtitle.destroy()
                                                                    anoticesendFrame.destroy()
                                                                    mnotice()
                                                                else:
                                                                    messagebox.showerror("error: ","msg already deleted") 
                                                                    # print("msg already deleted")
                                                            except Exception as e:
                                                                messagebox.showerror("Database error: ",f"{e}")  
                                                    except Exception as e:
                                                        messagebox.showerror("Database error: ",f"{e}")
                                                # admin send Notice end ------------------------------------------    
                                        
                                        
                                            # Notice Part End----------------------------------------------------------------
                                        
                                        
                                        Adminhome()        
                                else:
                                    messagebox.showwarning('warning',"wrong password")
                                    AID.set('')
                                    AP.set('')
                            else:
                                    messagebox.showwarning('warning',"wrong Id")
                                    AID.set('')
                                    AP.set('')
                            
                        except Exception as e:
                                messagebox.showwarning('warning',f"{e}")
                                AID.set('')
                                AP.set('')
                # Admin Second Varification Compleated       
        
Home()
root.mainloop()    