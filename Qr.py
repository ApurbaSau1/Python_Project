from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr:
    def __init__(self,root):
        self.root=root
     
        self.root.geometry("900x500+200+50")
        self.root.title("Qr Generator")
    #   for fixt the window
        self.root.resizable(False,False)
        
        title=Label(self.root,text="Welcome To QR Generator",font=("times new roman",40),bg='GREEN',fg="WHIte",anchor='w').place(x=0,y=0,relwidth=1)
       
        #=====Details Window=====
        self.code=StringVar()
        self.name=StringVar()
        self.add=StringVar()
        self.mobile=StringVar()
        self.BOD=StringVar()
        emp_Frame=Frame(self.root,bd=2,relief="raised",bg="white")
        emp_Frame.place(x=350,y=100,width=500,height=380)
        emp_title=Label(emp_Frame,text="Enter Your Details",font=("times new roman",20),bg='lightpink',fg="black").place(x=0,y=0,relwidth=1)
       
        code=Label(emp_Frame,text="Enter Id",font=("times new roman",18),bg='white',fg="black").place(x=30,y=50)
        name=Label(emp_Frame,text="Enter Your Name",font=("times new roman",18),bg='white',fg="black").place(x=30,y=80)
        add=Label(emp_Frame,text="Enter Your Address",font=("times new roman",18),bg='white',fg="black").place(x=30,y=112)
        mobile=Label(emp_Frame,text="Enter Mobile Number",font=("times new roman",18),bg='white',fg="black").place(x=30,y=145)
        BOD=Label(emp_Frame,text="Enter Date of Birth",font=("times new roman",18),bg='white',fg="black").place(x=30,y=180)
                
        code=Entry(emp_Frame,font=("times new roman",15),textvariable=self.code,bg='lightyellow',fg="black").place(x=280,y=50)
        name=Entry(emp_Frame,font=("times new roman",15),textvariable=self.name,bg='lightyellow',fg="black").place(x=280,y=80)
        add=Entry(emp_Frame,font=("times new roman",15),textvariable=self.add,bg='lightyellow',fg="black").place(x=280,y=115)
        mobile=Entry(emp_Frame,font=("times new roman",15),textvariable=self.mobile,bg='lightyellow',fg="black").place(x=280,y=150)
        BOD=Entry(emp_Frame,font=("times new roman",15),textvariable=self.BOD,bg='lightyellow',fg="black").place(x=280,y=185)
                
        btn_generate=Button(emp_Frame,text="Generat Qr",command=self.generate,font=("times new roman",15,"bold"),bg='lightpink',fg="black").place(x=100,y=250,width=120,height=50)
        btn_clear=Button(emp_Frame,text="clear",command=self.clear,font=("times new roman",15,"bold"),bg='lightgray',fg="black").place(x=250,y=249,width=120,height=50)
        
        self.msg=" "
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",15),bg='white',fg="blue")
        self.lbl_msg.place(x=100,y=320)
# generated qr code
        qrFrame=Frame(self.root,bd=2,relief="raised",bg="white")
        qrFrame.place(x=50,y=100,width=250,height=380)
        emp_title=Label(qrFrame,text="Generated Qr",font=("times new roman",20),bg='lightpink',fg="black").place(x=0,y=0,relwidth=1)
        self.qr_code=Label(qrFrame,text="no Qr\nAvailable",font=('times new roman',15),bg='blue',fg='white',bd=2,relief=RAISED)
        self.qr_code.place(x=30,y=100,width=180,height=200)
        
    def generate(self):
        if self.name.get()=='' or self.code.get()=='' or self.add.get()=='' or self.mobile.get()=='' or self.BOD.get()=='':
            self.msg="all field are requred!!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            data=(f"Id={self.code.get()}\nName={self.name.get()}\nAddress={self.add.get()}\nMobile Number={self.mobile.get()}\nDate of Birth={self.BOD.get()}")
            qr_code=qrcode.make(data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("qr_"+str(self.code.get() + self.name.get())+'.png')
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            self.msg="QR GENERATED SUCCESSFULLY"
            self.lbl_msg.config(text=self.msg,fg='green')
    def clear(self):
         self.code.set('')
         self.name.set('')
         self.add.set('')
         self.mobile.set('')
         self.BOD.set('')
         self.qr_code.config(image='') 
         self.msg=""
         self.lbl_msg.config(text=self.msg)  
            
root=Tk()
obj =Qr(root)
root.mainloop()    