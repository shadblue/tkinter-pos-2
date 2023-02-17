from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Style,Progressbar,Combobox,Treeview
import sqlite3
import sys
from win32api import GetSystemMetrics
from tkinter.messagebox import showinfo
from tkinter import messagebox
import time
import sqlite3
import mysql
from mysql import connector
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# mpl.use('GTKAgg') # to use GTK UI
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd

width=int(GetSystemMetrics(0))
height=int(GetSystemMetrics(1))

myfont0=('Arial',10,'bold')
myfont=('Arial',15)
myfontb=('Arial',15,'bold')
myfont1=('Arial',20)
myfont2=('Arial',25)
myfont3=('Arial',35)

expression = ""



class MAINAPPLICATION():
    def __init__(self) -> None:
        main_window=Tk()
        s=Style()
        s.theme_use('clam')
        
        # employee variable
        useEntVar=StringVar()
        lastEntVar=StringVar()
        roleEntVar=StringVar()
        passEntVar=StringVar()
        idEntVar=StringVar()
        
        # PRODUCT VARIABVLES
        prodNameEntVar=StringVar()
        prodCompanyEntVar=StringVar()
        prodQtyEntVar=StringVar()
        prodPriceEntVar=StringVar()
        prodUseEntVar=StringVar()
        
        # log in variable
        logUseEntVar=StringVar()
        logPassEntVar=StringVar()
        
        # search
        searchProd_entV=StringVar()
        
        main_window.geometry(f"{int(width)}x{int(height)}+0+0")
        main_window.resizable(width=0,height=0)
        
        # creating a blank icon for the main window
        icon=PhotoImage(master=main_window,height=16,width=16)
        icon.blank()
        icon.transparency_set(0,0,0)
        main_window.iconphoto(False,icon)
        main_window.title('POS System')
        # main_window.attributes("-topmost",True)
        main_window.wm_overrideredirect(1)
        
        # to center the main window
        try:
            screen_width=main_window.winfo_screenwidth()
            screen_height=main_window.winfo_screenheight()
            app_height=main_window.winfo_height()
            app_width=main_window.winfo_width()

            x_loc=int(screen_width/2)-int(app_width/2)
            y_loc=int(screen_height/2)-int(app_height/2)
            
        except Exception as msg:
            print(msg)
            pass
        
        main_canvas=Canvas(main_window,highlightthickness=0,background='beige')
        main_canvas.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        closeCan=Canvas(main_canvas,highlightthickness=0,bg='#1f1f3a')
        closeCan.place(relx=0,rely=0,relwidth=1,relheight=0.04)
        
        dest_lbl=Label(closeCan,text='X',bg='#1f1f3a',fg='#ffffff',font=('Arial',15))
        dest_lbl.pack(side=RIGHT,padx=10)
        dest_lbl.bind("<ButtonPress>",lambda event:sys.exit())
        
        reset_lbl=Label(closeCan,text='2',font=('Marlett',12),fg='#ffffff',bg='#1f1f3a')
        reset_lbl.pack(side=RIGHT,padx=7)
        
        minimize_lbl=Label(closeCan,text='-',font=('Arial',35),fg='#ffffff',bg='#1f1f3a')
        minimize_lbl.pack(side=RIGHT,padx=7)
        
        # myfont0=('Arial',10)
        # myfont=('Arial',15)
        # myfont1=('Arial',20)
        # myfont2=('Arial',25)
        # myfont3=('Arial',35)
        
        info_can=Canvas(main_canvas,highlightthickness=0,bg='#ffffff')
        info_can.place(relx=0,rely=0.04,relwidth=1,relheight=0.06)
        
        Label(info_can,text='Developed by: Slim Shady',bg='#ffffff',fg='black',font=myfont).pack(side=RIGHT,pady=8)
        
        # line
        Frame(info_can,bg='black').place(relx=0,rely=0.99,relwidth=1)
        
        
        content_can=Canvas(main_canvas,highlightthickness=0,bg='lightgreen')
        content_can.place(relx=0,rely=0.1,relwidth=1,relheight=0.84)
        
        # canvases in contcan
        log_can=Canvas(content_can,highlightthickness=0,bg='lightgreen')
        # log_can.place(relx=0,rely=0,relwidth=1,relheight=1)
        sign_can=Canvas(content_can,highlightthickness=0,bg='green')
        # sign_can.place(relx=0,rely=0,relwidth=1,relheight=1)
        body_can=Canvas(content_can,highlightthickness=0,bg='yellow')
        # body_can.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.admin_can=Canvas(content_can,highlightthickness=0,bg='lime')
        emp_can=Canvas(content_can,highlightthickness=0,bg='yellow')
        prod_can=Canvas(content_can,highlightthickness=0,bg='yellow')
        customer_can=Canvas(content_can,highlightthickness=0,bg='yellow')
        order_can=Canvas(content_can,highlightthickness=0,bg='yellow')
        
        menu_can=Canvas(content_can,highlightthickness=0,bg='yellow')
        location_can=Canvas(content_can,highlightthickness=0,bg='yellow')
        
        content_list=[log_can,sign_can,body_can,self.admin_can,emp_can,prod_can,customer_can,order_can,menu_can,location_can]
        
        # contents of bottom can
        bottom_can=Canvas(main_canvas,highlightthickness=0,bg='#ffffff')
        bottom_can.place(relx=0,rely=0.94,relwidth=1,relheight=0.06)
        
        # line
        Frame(bottom_can,bg='black').place(relx=0,rely=0,relwidth=1)
        
        Label(bottom_can,text='Operator: Slim Shady',bg='#ffffff',fg='black',font=myfont).pack(side=RIGHT,pady=8)
        
        
        # ====================Content of logcan===================
        logContCan=Canvas(log_can,highlightthickness=0,bg='blue')
        logContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        
        logBodyCan=Canvas(logContCan,highlightthickness=0,bg='#ffffff')
        logBodyCan.place(relx=0.4,rely=0.1,relheight=0.8,relwidth=0.3)
        
        # creating profile image
        profileImg=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/user.jpg")
        profileImg=profileImg.resize((150,100),Image.ANTIALIAS)
        profileImg=ImageTk.PhotoImage(profileImg,master=main_window)
        Label(logBodyCan,text='Username',bg='beige',fg='black',image=profileImg,font=myfont,bd=0).place(relx=0.36,rely=0.21)
        
        Label(logBodyCan,text='Username',bg='#ffffff',fg='black',font=myfont).place(relx=0.17,rely=0.4)
        Label(logBodyCan,text='Password',bg='#ffffff',fg='black',font=myfont).place(relx=0.17,rely=0.5)
        
        logUseEnt=Entry(logBodyCan,font=myfont,textvariable=logUseEntVar,bg='#ffffff',fg='#2A2D2E',bd=0)
        logUseEnt.place(relx=0.17,rely=0.45,relwidth=0.65)
        logPassEnt=Entry(logBodyCan,font=myfont,bg='#ffffff',textvariable=logPassEntVar,fg='#2A2D2E',bd=0)
        logPassEnt.place(relx=0.17,rely=0.55,relwidth=0.62)
        
        # creating q image
        quizImg=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/qa.jpg")
        quizImg=quizImg.resize((30,30),Image.ANTIALIAS)
        quizImg=ImageTk.PhotoImage(quizImg,master=main_window)
        Label(logBodyCan,text='Username',bg='beige',fg='black',image=quizImg,font=myfont,bd=0).place(relx=0.78,rely=0.545)
        
        
        logLbl=Label(logBodyCan,text='Login',bg='#ffffff',fg='black',font=myfont1,bd=2,relief=RIDGE)
        logLbl.place(relx=0.43,rely=0.6,relwidth=0.16)
        admLogLbl=Label(logBodyCan,text='Admin Login',bg='#ffffff',fg='black',font=myfont,bd=2,relief=RIDGE)
        admLogLbl.place(relx=0.41,rely=0.7,relwidth=0.21)
        
        
        # lines
        Frame(logBodyCan,bg='black').place(relx=0.17,rely=0.39,relwidth=0.65)
        Frame(logBodyCan,bg='black').place(relx=0.17,rely=0.49,relwidth=0.65)
        # Frame(logContCan,bg='black').place(relx=0.43,rely=0.59,relwidth=0.16)
        
        Label(logContCan,text='Not a member?',fg='#ffffff',bg='blue',font=myfont).place(relx=0.85,rely=0.03)
        toSignLbl=Label(logContCan,text='Sign Up',fg='#ffffff',bg='blue',font=myfont2,bd=2,relief=RIDGE)
        toSignLbl.place(relx=0.93,rely=0.02)
        
        # ====================Content of sigin can===================
        signContCan=Canvas(sign_can,highlightthickness=0,bg='#ffffff')
        signContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        # creating profile image
        signProfileImg=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/user.jpg")
        signProfileImg=signProfileImg.resize((150,100),Image.ANTIALIAS)
        signProfileImg=ImageTk.PhotoImage(signProfileImg,master=main_window)
        Label(signContCan,text='Username',bg='beige',fg='black',image=signProfileImg,font=myfont,bd=0).place(relx=0.44,rely=0.02)
        
        Label(signContCan,text='Username',bg='#ffffff',fg='black',font=myfont).place(relx=0.4,rely=0.2)
        Label(signContCan,text='Last Name',bg='#ffffff',fg='black',font=myfont).place(relx=0.4,rely=0.3)
        Label(signContCan,text='Role',bg='#ffffff',fg='black',font=myfont).place(relx=0.4,rely=0.4)
        Label(signContCan,text='National id',bg='#ffffff',fg='black',font=myfont).place(relx=0.4,rely=0.5)
        Label(signContCan,text='Password',bg='#ffffff',fg='black',font=myfont).place(relx=0.4,rely=0.6)
        Label(signContCan,text='Confirm Password',bg='#ffffff',fg='black',font=myfont).place(relx=0.4,rely=0.7)
        
        useEnt=Entry(signContCan,font=myfont,textvariable=useEntVar,bg='#ffffff',bd=0,fg='black')
        useEnt.place(relx=0.4,rely=0.24,relwidth=0.16)
        lastEnt=Entry(signContCan,font=myfont,bg='#ffffff',textvariable=lastEntVar,bd=0,fg='black')
        lastEnt.place(relx=0.4,rely=0.34,relwidth=0.16)
        roleEnt=Entry(signContCan,font=myfont,bg='#ffffff',textvariable=roleEntVar,bd=0,fg='black')
        roleEnt.place(relx=0.4,rely=0.44,relwidth=0.16)
        passEnt=Entry(signContCan,font=myfont,textvariable=passEntVar,bg='#ffffff',bd=0,fg='black')
        passEnt.place(relx=0.4,rely=0.54,relwidth=0.16)
        idEnt=Entry(signContCan,font=myfont,bg='#ffffff',textvariable=idEntVar,bd=0,fg='black')
        idEnt.place(relx=0.4,rely=0.64,relwidth=0.16)
        cPassEnt=Entry(signContCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        cPassEnt.place(relx=0.4,rely=0.74,relwidth=0.15)
        
        # useEnt=Entry(signContCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        # useEnt.place(relx=0.4,rely=0.24,relwidth=0.16)
        # passEnt=Entry(signContCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        # passEnt.place(relx=0.4,rely=0.34,relwidth=0.16)
        # useEnt=Entry(signContCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        # useEnt.place(relx=0.4,rely=0.44,relwidth=0.16)
        # passEnt=Entry(signContCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        # passEnt.place(relx=0.4,rely=0.54,relwidth=0.16)
        # useEnt=Entry(signContCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        # useEnt.place(relx=0.4,rely=0.64,relwidth=0.16)
        # passEnt=Entry(signContCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        # passEnt.place(relx=0.4,rely=0.74,relwidth=0.15)
        
        # creating q image
        squizImg=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/qa.jpg")
        squizImg=squizImg.resize((30,30),Image.ANTIALIAS)
        squizImg=ImageTk.PhotoImage(squizImg,master=main_window)
        Label(signContCan,text='Username',bg='beige',fg='black',image=squizImg,font=myfont,bd=0).place(relx=0.55,rely=0.74)
        
        # lines
        Frame(signContCan,bg='black').place(relx=0.4,rely=0.28,relwidth=0.16)
        Frame(signContCan,bg='black').place(relx=0.4,rely=0.38,relwidth=0.16)
        Frame(signContCan,bg='black').place(relx=0.4,rely=0.48,relwidth=0.16)
        Frame(signContCan,bg='black').place(relx=0.4,rely=0.58,relwidth=0.16)
        Frame(signContCan,bg='black').place(relx=0.4,rely=0.68,relwidth=0.16)
        Frame(signContCan,bg='black').place(relx=0.4,rely=0.18,relwidth=0.16)
        
        Label(signContCan,text='Already signed up?',bg='#ffffff',fg='black',font=myfont).place(relx=0,rely=0.03) 
        backLbl=Label(signContCan,text='Login',bg='#ffffff',fg='black',font=myfont1,bd=2,relief=RIDGE)
        backLbl.place(relx=0.09,rely=0.03,relwidth=0.07)
        signLbl=Label(signContCan,text='Signup',bg='#ffffff',fg='black',font=myfont1,bd=2,relief=RIDGE)
        signLbl.place(relx=0.4,rely=0.8,relwidth=0.16)
        
        #  ====================Content of admin can==================
        # function to resize image
        def resizeAdmnImage(image):
            img=Image.open(image)
            img=img.resize((30,40),Image.ANTIALIAS)
            img=ImageTk.PhotoImage(img,master=main_window)
            return img
        
        # Images
        cus_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/customer.jpg")
        logout_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/out.png")
        emplo_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/emp.png")
        order_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/order.png")
        men_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/menu.jpg")
        location_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/loc.png")
        
        def resizeAddImage(image):
            img=Image.open(image)
            img=img.resize((50,40),Image.ANTIALIAS)
            img=ImageTk.PhotoImage(img,master=main_window)
            return img
        addCus_img=resizeAddImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/addcus.png")
        
        
        
        dashContCan=Canvas(self.admin_can,highlightthickness=0,bg='#ffffff')
        dashContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        
        #xxxxxxxxxxxxxxxxx==== Side Canvas ===xxxxxxxxxxxxxxxxxxxxxx
        sideCan=Canvas(dashContCan,highlightthickness=0,bg='#ffffff')
        sideCan.place(relx=0,rely=0,relheight=1,relwidth=0.08)
        
        dashLbl=Label(sideCan,text="Dashboard",bg='#ffffff',font=myfont,fg='black',image=logout_img,compound=TOP,bd=2,relief=GROOVE)
        dashLbl.place(relx=0,rely=0,relwidth=1,relheight=0.1)
        prodImg6=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/prod.png")
        prodImg6=prodImg6.resize((50,40),Image.ANTIALIAS)
        prodImg6=ImageTk.PhotoImage(prodImg6,master=main_window)
        employee_openLbl=Label(sideCan,text="Employee",bg='#ffffff',font=myfont,fg='black',image=emplo_img,compound=TOP,bd=2,relief=GROOVE)
        employee_openLbl.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)
        
        prodOpenLbl=Label(sideCan,text="Product",bg='#ffffff',font=myfont,fg='black',image=prodImg6,compound=TOP,bd=2,relief=GROOVE)
        prodOpenLbl.place(relx=0,rely=0.2,relwidth=1,relheight=0.1)
        CustOpenLbl=Label(sideCan,text="Customers",bg='#ffffff',font=myfont,fg='black',image=cus_img,compound=TOP,bd=2,relief=GROOVE)
        CustOpenLbl.place(relx=0,rely=0.3,relwidth=1,relheight=0.1)
        OrdOpenLbl=Label(sideCan,text="Orders",bg='#ffffff',font=myfont,fg='black',image=order_img,compound=TOP,bd=2,relief=GROOVE)
        OrdOpenLbl.place(relx=0,rely=0.4,relwidth=1,relheight=0.1)
        MenuOpenLbl=Label(sideCan,text="Menu",bg='#ffffff',font=myfont,fg='black',image=men_img,compound=TOP,bd=2,relief=GROOVE)
        MenuOpenLbl.place(relx=0,rely=0.5,relwidth=1,relheight=0.1)
        locOpenLbl=Label(sideCan,text="Location",bg='#ffffff',font=myfont,fg='black',image=location_img,compound=TOP,bd=2,relief=GROOVE)
        locOpenLbl.place(relx=0,rely=0.6,relwidth=1,relheight=0.1)
        adminOutLbl=Label(sideCan,text="Logout",bg='#ffffff',font=myfont,fg='black',image=logout_img,compound=TOP,bd=2,relief=GROOVE)
        adminOutLbl.place(relx=0,rely=0.7,relwidth=1,relheight=0.1)
        
        
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        separatorCan=Canvas(dashContCan,highlightthickness=0,bg='silver')
        separatorCan.place(relx=0.08,rely=0,relheight=1,relwidth=0.001)\
            
        drop_img=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/drop.jpg")
        drop_img=drop_img.resize((20,30),Image.ANTIALIAS)
        drop_img=ImageTk.PhotoImage(drop_img,master=main_window)
        
        
        
        # ==========daily========================
        dailyFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        dailyFrame.place(relx=0.1,rely=0.02,relheight=0.15,relwidth=0.24)
        
        # image
        up_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/up.jpg")
        
        Label(dailyFrame,text="Daily Sale",bg='#ffffff',font=myfont,fg='black').place(relx=0.1,rely=0.1)
        Label(dailyFrame,text="",bg='#ffffff',font=myfont,image=up_img,bd=0,fg='black').place(relx=0.1,rely=0.4)
        Label(dailyFrame,text="Ksh 249",bg='#ffffff',font=myfont,bd=0,fg='black').place(relx=0.2,rely=0.4)
        Label(dailyFrame,text="67%",bg='#ffffff',font=myfont,bd=0,fg='black').place(relx=0.8,rely=0.4)
        
        # Progress bar widget
        p = Progressbar(dailyFrame, orient="horizontal", length=400, mode="determinate",
                    takefocus=True, maximum=100)
        p['value'] = 0
        p.pack(side=BOTTOM,padx=(0,10),pady=(0,10))

        def start():
            if p['value'] < 100:
                p['value'] += 10

                main_window.after(1000, start)

        main_window.after(1000, start)
        
        # ========================monthly sales==============
        monthlyFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        monthlyFrame.place(relx=0.35,rely=0.02,relheight=0.15,relwidth=0.32)
        
        # image
        up_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/up.jpg")
        
        Label(monthlyFrame,text="Daily Sale",bg='#ffffff',font=myfont,fg='black').place(relx=0.1,rely=0.1)
        Label(monthlyFrame,text="",bg='#ffffff',font=myfont,image=up_img,bd=0,fg='black').place(relx=0.1,rely=0.4)
        Label(monthlyFrame,text="Ksh 249",bg='#ffffff',font=myfont,bd=0,fg='black').place(relx=0.2,rely=0.4)
        Label(monthlyFrame,text="67%",bg='#ffffff',font=myfont,bd=0,fg='black').place(relx=0.8,rely=0.4)
        
        # Progress bar widget
        m = Progressbar(monthlyFrame, orient="horizontal", length=400, mode="determinate",
                    takefocus=True, maximum=100)
        m['value'] = 0
        m.pack(side=BOTTOM,padx=(0,10),pady=(0,10))

        def start():
            if m['value'] < 100:
                m['value'] += 20

                main_window.after(1000, start)

        main_window.after(1000, start)
        
        
        # =====================Yearly frame======
        
        yearlyFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        yearlyFrame.place(relx=0.68,rely=0.02,relheight=0.15,relwidth=0.3)
        
        # image
        up_img=resizeAdmnImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/up.jpg")
        
        Label(yearlyFrame,text="Daily Sale",bg='#ffffff',font=myfont,fg='black').place(relx=0.1,rely=0.1)
        Label(yearlyFrame,text="",bg='#ffffff',font=myfont,image=up_img,bd=0,fg='black').place(relx=0.1,rely=0.4)
        Label(yearlyFrame,text="Ksh 249",bg='#ffffff',font=myfont,bd=0,fg='black').place(relx=0.2,rely=0.4)
        Label(yearlyFrame,text="67%",bg='#ffffff',font=myfont,bd=0,fg='black').place(relx=0.8,rely=0.4)
        
        # Progress bar widget
        y = Progressbar(yearlyFrame, orient="horizontal", length=400, mode="determinate",
                    takefocus=True, maximum=100)
        y['value'] = 0
        y.pack(side=BOTTOM,padx=(0,10),pady=(0,10))

        def start():
            if y['value'] < 100:
                y['value'] += 30

                main_window.after(1000, start)

        main_window.after(1000, start)
        
        # ==============Recent users===========================
        recentUserFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        recentUserFrame.place(relx=0.1,rely=0.2,relheight=0.3,relwidth=0.24)
        
        Label(recentUserFrame,text="Last Months Sales",bg='#ffffff',font=myfont,fg='black').place(relx=0.02,rely=0.06)
        
      
        
        Label(recentUserFrame,text="This Month",bg='#ffffff',font=myfont,fg='black',image=drop_img,compound=RIGHT,bd=2,relief=GROOVE).place(relx=0.7,rely=0.02)
        
        Frame(recentUserFrame,bg='silver').place(relx=0,rely=0.17,relheight=0.001,relwidth=1)
        
        recentbodyFrame=Frame(recentUserFrame,bg='#ffffff',bd=0)
        recentbodyFrame.place(relx=0,rely=0.2,relheight=0.8,relwidth=1)
        
        #------------------ line graph-----------------
        fig, ax = plt.subplots()
 
        t = np.arange(0, 3, .01)
        line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, recentbodyFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        
        toolbar = NavigationToolbar2Tk(canvas, recentbodyFrame, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=BOTTOM, fill=X)
        
        # ==============Recent users===========================
        barFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        barFrame.place(relx=0.1,rely=0.51,relheight=0.3,relwidth=0.24)
        
        Label(barFrame,text="Top Collections By Revenue",bg='#ffffff',font=myfont,fg='black').place(relx=0.02,rely=0.06)
      
        
        Label(barFrame,text="This Month",bg='#ffffff',font=myfont,fg='black',image=drop_img,compound=RIGHT,bd=2,relief=GROOVE).place(relx=0.7,rely=0.02)
        
        Frame(barFrame,bg='silver').place(relx=0,rely=0.17,relheight=0.001,relwidth=1)
        
        barbodyFrame=Frame(barFrame,bg='#ffffff',bd=0)
        barbodyFrame.place(relx=0,rely=0.2,relheight=0.8,relwidth=1)
        
        # ------------bar graaph------------------------
        # prepare data
        data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, barbodyFrame)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, barbodyFrame)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # ==============Recent users===========================
        pieUserFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        pieUserFrame.place(relx=0.35,rely=0.2,relheight=0.3,relwidth=0.32)
        
        Label(pieUserFrame,text="Average Price and Unit per Transaction",bg='#ffffff',font=myfont,fg='black').place(relx=0.02,rely=0.06)
  
        Label(pieUserFrame,text="This Month",bg='#ffffff',font=myfont,fg='black',image=drop_img,compound=RIGHT,bd=2,relief=GROOVE).place(relx=0.78,rely=0.02)
        
        Frame(pieUserFrame,bg='silver').place(relx=0,rely=0.17,relheight=0.001,relwidth=1)
        
        piebodyFrame=Frame(pieUserFrame,bg='#ffffff',bd=0)
        piebodyFrame.place(relx=0,rely=0.2,relheight=0.8,relwidth=1)
        
        # --------------pie-chart-----------
        stockListExp = ['AMZN' , 'AAPL', 'JETS', 'CCL', 'NCLH']
        stockSplitExp = [15,25,40,10,10]

        fig = Figure() # create a figure object
        ax = fig.add_subplot(111) # add an Axes to the figure

        ax.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True,)

        chart1 = FigureCanvasTkAgg(fig,piebodyFrame)
        chart1.get_tk_widget().pack()
        # ,,,,,,,,,,,,,,,,,,,,,<<<<<<< Bar Chart 2 .........................>>>>>>>>>>>>>>>>>>>>>>>
        bar2UserFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        bar2UserFrame.place(relx=0.35,rely=0.51,relheight=0.3,relwidth=0.32)
        
        Label(bar2UserFrame,text="Total Customers and Visitors",bg='#ffffff',font=myfont,fg='black').place(relx=0.02,rely=0.06)
        
        
        
        Label(bar2UserFrame,text="This Month",bg='#ffffff',font=myfont,fg='black',image=drop_img,compound=RIGHT,bd=2,relief=GROOVE).place(relx=0.78,rely=0.02)
        
        Frame(bar2UserFrame,bg='silver').place(relx=0,rely=0.17,relheight=0.001,relwidth=1)
        
        c_width = 500
        c_height = 200
        c = Canvas(bar2UserFrame, highlightthickness=0,bg='#ffffff')
        c.place(relx=0,rely=0.2,relheight=0.8,relwidth=1)

        c.create_rectangle(20, 140, 120, 180, fill="red")
        c.create_text(70, 130, text="Projects--20%")
        c.create_rectangle(140, 160, 240, 180, fill="blue")
        c.create_text(190, 150, text="Quizzes--10%")
        c.create_rectangle(260, 120, 360, 180, fill="green")
        c.create_text(310, 110, text="Midterm--30%")
        c.create_rectangle(380, 100, 480, 180, fill="orange")
        c.create_text(430, 90, text="Final--40%")
        c.create_line(0, 180, 500, 180)
        
        # <<<<<<<<<<<<<<<<<<<<<<<<<Upcoming Events >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        upEventsFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        upEventsFrame.place(relx=0.68,rely=0.2,relheight=0.35,relwidth=0.3)
        
        Label(upEventsFrame,text="Top Items Sold",bg='#ffffff',font=myfont,fg='black').place(relx=0.02,rely=0.06)
        Label(upEventsFrame,text="This Month",bg='#ffffff',font=myfont,fg='black',image=drop_img,compound=RIGHT,bd=2,relief=GROOVE).place(relx=0.78,rely=0.02)
        
        Frame(upEventsFrame,bg='silver').place(relx=0,rely=0.16,relheight=0.001,relwidth=1)
        
        hbar_Img=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/2BarPlot.png")
        hbar_Img=hbar_Img.resize((670,300),Image.ANTIALIAS)
        hbar_Img=ImageTk.PhotoImage(hbar_Img,master=main_window)
        
        Label(upEventsFrame,text="This Month",bg='#ffffff',font=myfont,fg='black',image=hbar_Img,bd=0).place(relx=0,rely=0.17,relwidth=1,relheight=0.74)
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<events>>>>>>>>>>>>>>>>>>>>>>>>>
        totIdeasFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        # totIdeasFrame.place(relx=0.68,rely=0.43,relheight=0.13,relwidth=0.3)
        
        totLocFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        totLocFrame.place(relx=0.68,rely=0.565,relheight=0.13,relwidth=0.3)
        
        data1 = {'country': ['A', 'B', 'C', 'D', 'E'],
         'gdp_per_capita': [45000, 42000, 52000, 49000, 47000]
         }
        df1 = pd.DataFrame(data1)
        
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, totLocFrame)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df1 = df1[['country', 'gdp_per_capita']].groupby('country').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Country Vs. GDP Per Capita')
        
        btnFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        btnFrame.place(relx=0.68,rely=0.7,relheight=0.29,relwidth=0.3)
        
        stockListExp = ['USA', 'Brazil', 'Russia', 'Spain', 'UK']
        stockSplitExp = [2026493, 710887, 476658, 288797, 287399]

        fig = Figure() # create a figure object
        ax = fig.add_subplot(111) # add an Axes to the figure

        ax.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True,)

        chart1 = FigureCanvasTkAgg(fig,btnFrame)
        chart1.get_tk_widget().pack()
        # ================ Last Frame ==================================
        lastfFrame=Frame(dashContCan,bg='#ffffff',bd=1,relief=RIDGE)
        lastfFrame.place(relx=0.1,rely=0.82,relheight=0.17,relwidth=0.57)
        
        # line graph
        data2 = {'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
         }  
        df2 = pd.DataFrame(data2)
        
        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, lastfFrame)
        line2.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df2 = df2[['year', 'unemployment_rate']].groupby('year').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        ax2.set_title('Year Vs. Unemployment Rate')
        
        # doted graph
        data3 = {'interest_rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'index_price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
         }
        df3 = pd.DataFrame(data3)
        
        figure3 = plt.Figure(figsize=(5, 4), dpi=100)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(df3['interest_rate'], df3['index_price'], color='g')
        scatter3 = FigureCanvasTkAgg(figure3, lastfFrame)
        scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)
        ax3.legend(['index_price'])
        ax3.set_xlabel('Interest Rate')
        ax3.set_title('Interest Rate Vs. Index Price')
        
        
        
        
        
        # =====================End of Content of Admin===================
        
        # ============contents of employee can=============================
        
        EmployeeContCan=Canvas(emp_can,highlightthickness=0,bg='#ffffff')
        EmployeeContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        # add employee image
        addEmpImg=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/addemp.png")
        addEmpImg=addEmpImg.resize((50,40),Image.ANTIALIAS)
        addEmpImg=ImageTk.PhotoImage(addEmpImg,master=main_window)
        insertEmpLbl=Label(EmployeeContCan,text="Add Employees",bg='#ffffff',font=myfont,fg='black',bd=2,relief=GROOVE,image=addEmpImg,compound=RIGHT)
        insertEmpLbl.place(relx=0.738,rely=0.08,relwidth=0.1)
        
        csvLbl=Label(EmployeeContCan,text="Import CSV",bg='#ffffff',font=myfont,fg='black',bd=2,relief=GROOVE,compound=RIGHT)
        csvLbl.place(relx=0.84,rely=0.08,relheight=0.05)
        
        sachLbl=Label(EmployeeContCan,text="Search",bg='lightgreen',font=myfont,fg='black',bd=2,relief=GROOVE,compound=RIGHT)
        sachLbl.place(relx=0.738,rely=0.14,relheight=0.05)
        serch_ent=Entry(EmployeeContCan,bg='#ffffff',font=myfont,fg='black',bd=0)
        serch_ent.place(relx=0.78,rely=0.155)
        Frame(EmployeeContCan,bg='brown').place(relx=0.78,rely=0.188,relwidth=0.12,relheight=0.001)
        # add back image
        empBackImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/back2.png")
        empBackImg5=empBackImg5.resize((50,40),Image.ANTIALIAS)
        empBackImg5=ImageTk.PhotoImage(empBackImg5,master=main_window)
        EmpDashLbl=Label(EmployeeContCan,text="Back to Dashboard",bg='#ffffff',font=myfont,fg='black',image=empBackImg5,compound=LEFT)
        EmpDashLbl.place(relx=0.1,rely=0.08,relwidth=0.12)
        
        empTreeCan=Canvas(EmployeeContCan,highlightthickness=2,bg='green',bd=2,relief=GROOVE)
        empTreeCan.place(relx=0.1,rely=0.2,relheight=0.6,relwidth=0.8)
        # Creating a tree
        # style treeview
        style=Style()
        style.theme_use('clam')
        style.configure("Treeview",font=myfont,foreground='#2b2b2b',cellpadding=19)
        style.configure("Treeview.Heading",font=myfont,foreground='#444',background='PowderBlue',cellpadding=19)
        style.map('Treeview', background=[('selected','darkgreen')],foreground=[('selected','orange')])
        
        # style=Style()
        # style.theme_use('clam')
        # style.configure("Treeview", background="beige", fieldbackground="beige", foreground="black",rowheight=25)
        # style.configure('Treeview.Heading', background="PowderBlue")
        empTree=Treeview(empTreeCan,columns=("column1","column2","column3","column4","column5"),show='headings',selectmode='browse')
        
        empTree.column("column1",anchor=CENTER,width=80)
        empTree.column("column2",anchor=CENTER,width=80)
        empTree.column("column3",anchor=CENTER,width=80)
        empTree.column("column4",anchor=CENTER,width=80)
        empTree.column("column5",anchor=CENTER,width=80)
        
        empTree.heading("#1",text="User Name",anchor=CENTER)
        empTree.heading("#2",text="Last Name",anchor=CENTER)
        empTree.heading("#3",text="Role",anchor=CENTER)
        empTree.heading("#4",text="Salary",anchor=CENTER)
        empTree.heading("#5",text="Password",anchor=CENTER)
        
        empTree.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        # alternating colors
        empTree.tag_configure("odd",background="#eee")
        empTree.tag_configure("even",background="#ddd")
        # attaching scroll bars
        sb_vertical=Scrollbar(empTreeCan,orient='vertical',command=empTree.yview)
        sb_horizontal=Scrollbar(empTreeCan,orient='horizontal',command=empTree.xview)
        empTree.configure(yscrollcommand=sb_vertical.set,xscrollcommand=sb_horizontal.set)
        sb_vertical.grid(row=0,column=1,sticky='ns')
        sb_horizontal.grid(row=1,column=0,sticky='ew')
        
        # configure position of grid for treeview
        empTreeCan.grid_rowconfigure(0,weight=1)
        empTreeCan.grid_columnconfigure(0,weight=1)
        
        # \\\\\\\\\\\\\\\\\insert employee\\\\\\\\\\\\\\\\\
        insertCan=Canvas(EmployeeContCan,highlightthickness=0,bg='#ffffff',bd=2,relief=RIDGE)
        # insertCan.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.48)
        
        closeInsertLbl=Label(insertCan,text='x',bg='#ffffff',fg='black',font=myfont3)
        closeInsertLbl.place(relx=0.96,rely=0.02)
        
        # creating profile image
        signProfileImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/user.jpg")
        signProfileImg5=signProfileImg5.resize((150,100),Image.ANTIALIAS)
        signProfileImg5=ImageTk.PhotoImage(signProfileImg5,master=main_window)
        Label(insertCan,text='',bg='#ffffff',fg='black',image=signProfileImg5,font=myfont,bd=0).place(relx=0.44,rely=0.02)
        
        Label(insertCan,text='Username',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.2)
        Label(insertCan,text='Last Name',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.3)
        Label(insertCan,text='role',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.4)
        Label(insertCan,text='Password',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.5)
        Label(insertCan,text='National ID',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.6)
        Label(insertCan,text='Confirm Password',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.7)
        
        useEnt=Entry(insertCan,font=myfont,textvariable=useEntVar,bg='#ffffff',bd=0,fg='black')
        useEnt.place(relx=0.3,rely=0.24,relwidth=0.46)
        lastEnt=Entry(insertCan,font=myfont,bg='#ffffff',textvariable=lastEntVar,bd=0,fg='black')
        lastEnt.place(relx=0.3,rely=0.34,relwidth=0.46)
        roleEnt=Entry(insertCan,font=myfont,bg='#ffffff',textvariable=roleEntVar,bd=0,fg='black')
        roleEnt.place(relx=0.3,rely=0.44,relwidth=0.46)
        passEnt=Entry(insertCan,font=myfont,textvariable=passEntVar,bg='#ffffff',bd=0,fg='black')
        passEnt.place(relx=0.3,rely=0.54,relwidth=0.46)
        idEnt=Entry(insertCan,font=myfont,bg='#ffffff',textvariable=idEntVar,bd=0,fg='black')
        idEnt.place(relx=0.3,rely=0.64,relwidth=0.46)
        cPassEnt=Entry(insertCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        cPassEnt.place(relx=0.3,rely=0.74,relwidth=0.45)
        
        # creating q image
        squizImg3=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/qa.jpg")
        squizImg3=squizImg3.resize((30,30),Image.ANTIALIAS)
        squizImg3=ImageTk.PhotoImage(squizImg3,master=main_window)
        Label(insertCan,text='Username',bg='beige',fg='black',image=squizImg3,font=myfont,bd=0).place(relx=0.75,rely=0.735)
        
        # lines
        Frame(insertCan,bg='black').place(relx=0.3,rely=0.28,relwidth=0.46)
        Frame(insertCan,bg='black').place(relx=0.3,rely=0.38,relwidth=0.46)
        Frame(insertCan,bg='black').place(relx=0.3,rely=0.48,relwidth=0.46)
        Frame(insertCan,bg='black').place(relx=0.3,rely=0.58,relwidth=0.46)
        Frame(insertCan,bg='black').place(relx=0.3,rely=0.68,relwidth=0.46)
        Frame(insertCan,bg='black').place(relx=0.3,rely=0.18,relwidth=0.46)
        
        # Label(root1,text='Already signed up?',bg='#ffffff',fg='black',font=myfont).place(relx=0,rely=0.03) 
        # backLbl=Label(root1,text='Login',bg='#ffffff',fg='black',font=myfont1,bd=2,relief=RIDGE)
        # backLbl.place(relx=0.09,rely=0.03,relwidth=0.07)
        signEmpLbl=Label(insertCan,text='SUBMIT',bg='beige',fg='black',font=myfont1,bd=2,relief=RIDGE)
        signEmpLbl.place(relx=0.3,rely=0.8,relwidth=0.46)
        
        # =============end of employee can================================
        
        # ============Contents of product can============================
        prodContCan=Canvas(prod_can,highlightthickness=0,bg='#ffffff')
        prodContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        
        
        # add back image
        prodBackImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/back2.png")
        prodBackImg5=prodBackImg5.resize((50,40),Image.ANTIALIAS)
        prodBackImg5=ImageTk.PhotoImage(prodBackImg5,master=main_window)
        # EmpDashLbl=Label(EmployeeContCan,text="Back to Dashboard",bg='#ffffff',font=myfont,fg='black',image=empBackImg5,compound=LEFT)
        # EmpDashLbl.place(relx=0,rely=0,relwidth=0.12)
    
        prodDashLbl=Label(prodContCan,text="Back to Dashboard",bg='#ffffff',font=myfont,fg='black',image=prodBackImg5,compound=LEFT)
        prodDashLbl.place(relx=0.1,rely=0.08,relwidth=0.12)
        
        prodSelectLbl=Label(prodContCan,text="Select",bg='#ffffff',font=myfont,fg='black',bd=2,relief=GROOVE)
        prodSelectLbl.place(relx=0.1,rely=0.15,relwidth=0.12)
        
        # add product image
        addProdImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/addprod.png")
        addProdImg5=addProdImg5.resize((50,40),Image.ANTIALIAS)
        addProdImg5=ImageTk.PhotoImage(addProdImg5,master=main_window)
        # addEmpLbl=Label(EmployeeContCan,text="Add Employees",bg='#ffffff',font=myfont,fg='black',image=addProdImg5,compound=RIGHT)
        # addEmpLbl.place(relx=0.2,rely=0.01,relwidth=0.1)
        insertProdLbl=Label(prodContCan,text="Add Products",bg='#ffffff',font=myfont,fg='black',bd=2,relief=GROOVE,image=addProdImg5,compound=RIGHT)
        insertProdLbl.place(relx=0.738,rely=0.08,relwidth=0.1)
        
        
        
        csvLbl=Label(prodContCan,text="Import CSV",bg='#ffffff',font=myfont,fg='black',bd=2,relief=GROOVE,compound=RIGHT)
        csvLbl.place(relx=0.84,rely=0.08,relheight=0.05)
        
        sachProdLbl=Label(prodContCan,text="Search By Name",bg='#ffffff',font=myfont,fg='black',bd=0,compound=RIGHT)
        sachProdLbl.place(relx=0.7,rely=0.15,relheight=0.05)
        searchProd_ent=Entry(prodContCan,bg='#ffffff',textvariable=searchProd_entV,font=myfont,fg='black',bd=0)
        searchProd_ent.place(relx=0.78,rely=0.159)
        
        Frame(prodContCan,bg='brown').place(relx=0.78,rely=0.188,relwidth=0.12,relheight=0.001)
        
        prodTreeCan=Canvas(prodContCan,highlightthickness=0,bg='#ffffff')
        prodTreeCan.place(relx=0.1,rely=0.2,relheight=0.6,relwidth=0.8)
        # Creating a tree
        style=Style()
        style.theme_use('clam')
        prodTree=Treeview(prodTreeCan,columns=("column1","column2","column3","column4","column5"),show='headings',selectmode='browse')
        
        prodTree.column("column1",anchor=CENTER,width=80)
        prodTree.column("column2",anchor=CENTER,width=80)
        prodTree.column("column3",anchor=CENTER,width=80)
        prodTree.column("column4",anchor=CENTER,width=80)
        prodTree.column("column5",anchor=CENTER,width=80)
        
        prodTree.heading("#1",text="Product Name",anchor=CENTER)
        prodTree.heading("#2",text="Company Name",anchor=CENTER)
        prodTree.heading("#3",text="Quantity",anchor=CENTER)
        prodTree.heading("#4",text="Price",anchor=CENTER)
        prodTree.heading("#5",text="Use",anchor=CENTER)
        
        prodTree.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        # alternating colors
        prodTree.tag_configure("odd",background="#eee")
        prodTree.tag_configure("even",background="#ddd")
        
        # attaching scroll bars
        sb_vertical=Scrollbar(prodTreeCan,orient='vertical',command=prodTree.yview)
        sb_horizontal=Scrollbar(prodTreeCan,orient='horizontal',command=prodTree.xview)
        prodTree.configure(yscrollcommand=sb_vertical.set,xscrollcommand=sb_horizontal.set)
        sb_vertical.grid(row=0,column=1,sticky='ns')
        sb_horizontal.grid(row=1,column=0,sticky='ew')
        
        # configure position of grid for treeview
        prodTreeCan.grid_rowconfigure(0,weight=1)
        prodTreeCan.grid_columnconfigure(0,weight=1)
        
        # \\\\\\\\\\\\\\\\\insert product\\\\\\\\\\\\\\\\\
        insertProdCan=Canvas(prodContCan,highlightthickness=0,bg='#ffffff',bd=2,relief=RIDGE)
        # insertCan.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.48)
        
        closeInsertProdLbl=Label(insertProdCan,text='x',bg='#ffffff',fg='black',font=myfont3)
        closeInsertProdLbl.place(relx=0.96,rely=0.02)
        
        # creating profile image
        prodProfileImg2=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/product.png")
        prodProfileImg2=prodProfileImg2.resize((150,100),Image.ANTIALIAS)
        prodProfileImg2=ImageTk.PhotoImage(prodProfileImg2,master=main_window)
        Label(insertProdCan,text='',bg='beige',fg='black',image=prodProfileImg2,font=myfontb,bd=0).place(relx=0.44,rely=0.02)
        
        Label(insertProdCan,text='Product Name',bg='#ffffff',fg='black',font=myfontb).place(relx=0.3,rely=0.2)
        Label(insertProdCan,text='Conpany Name',bg='#ffffff',fg='black',font=myfontb).place(relx=0.3,rely=0.3)
        Label(insertProdCan,text='Quantity',bg='#ffffff',fg='black',font=myfontb).place(relx=0.3,rely=0.4)
        Label(insertProdCan,text='Price',bg='#ffffff',fg='black',font=myfontb).place(relx=0.3,rely=0.5)
        Label(insertProdCan,text='Product Use',bg='#ffffff',fg='black',font=myfontb).place(relx=0.3,rely=0.6)
        # Label(insertProdCan,text='Confirm Password',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.7)
        
        prodNameEnt=Entry(insertProdCan,font=myfont,textvariable=prodNameEntVar,bg='#ffffff',bd=0,fg='#333333')
        prodNameEnt.place(relx=0.3,rely=0.24,relwidth=0.46)
        prodCompanyEnt=Entry(insertProdCan,font=myfont,bg='#ffffff',textvariable=prodCompanyEntVar,bd=0,fg='#333333')
        prodCompanyEnt.place(relx=0.3,rely=0.34,relwidth=0.46)
        prodQtyEnt=Entry(insertProdCan,font=myfont,bg='#ffffff',textvariable=prodQtyEntVar,bd=0,fg='#333333')
        prodQtyEnt.place(relx=0.3,rely=0.44,relwidth=0.46)
        prodPriceEnt=Entry(insertProdCan,font=myfont,textvariable=prodPriceEntVar,bg='#ffffff',bd=0,fg='#333333')
        prodPriceEnt.place(relx=0.3,rely=0.54,relwidth=0.46)
        prodUseEnt=Entry(insertProdCan,font=myfont,bg='#ffffff',textvariable=prodUseEntVar,bd=0,fg='#333333')
        prodUseEnt.place(relx=0.3,rely=0.64,relwidth=0.46)
        cPassEnt=Entry(insertProdCan,font=myfont,bg='#ffffff',bd=0,fg='#333333')
        # cPassEnt.place(relx=0.3,rely=0.74,relwidth=0.45)
        
        # creating q image
        squizImg2=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/qa.jpg")
        squizImg2=squizImg2.resize((30,30),Image.ANTIALIAS)
        squizImg2=ImageTk.PhotoImage(squizImg2,master=main_window)
        Label(insertProdCan,text='',bg='#ffffff',fg='black',image=squizImg2,font=myfont,bd=0).place(relx=0.75,rely=0.735)
        
        # lines
        Frame(insertProdCan,bg='black').place(relx=0.3,rely=0.28,relwidth=0.46)
        Frame(insertProdCan,bg='black').place(relx=0.3,rely=0.38,relwidth=0.46)
        Frame(insertProdCan,bg='black').place(relx=0.3,rely=0.48,relwidth=0.46)
        Frame(insertProdCan,bg='black').place(relx=0.3,rely=0.58,relwidth=0.46)
        Frame(insertProdCan,bg='black').place(relx=0.3,rely=0.68,relwidth=0.46)
        Frame(insertProdCan,bg='black').place(relx=0.3,rely=0.18,relwidth=0.46)
        
        # Label(root1,text='Already signed up?',bg='#ffffff',fg='black',font=myfont).place(relx=0,rely=0.03) 
        # backLbl=Label(root1,text='Login',bg='#ffffff',fg='black',font=myfont1,bd=2,relief=RIDGE)
        # backLbl.place(relx=0.09,rely=0.03,relwidth=0.07)
        saveProdLbl=Label(insertProdCan,text='Save',bg='beige',fg='black',font=myfont1,bd=2,relief=RIDGE)
        saveProdLbl.place(relx=0.3,rely=0.8,relwidth=0.46)
        
        clrProdLbl=Label(insertProdCan,text='Clear',bg='beige',fg='black',font=myfont1,bd=2,relief=RIDGE)
        clrProdLbl.place(relx=0.3,rely=0.9,relwidth=0.15)
        updProdLbl=Label(insertProdCan,text='Update',bg='beige',fg='black',font=myfont1,bd=2,relief=RIDGE)
        updProdLbl.place(relx=0.46,rely=0.9,relwidth=0.15)
        dltProdLbl=Label(insertProdCan,text='Delete',bg='beige',fg='black',font=myfont1,bd=2,relief=RIDGE)
        dltProdLbl.place(relx=0.62,rely=0.9,relwidth=0.14)
        # /////////////////End of Insert Product///////////////////////////////////
        # ============End of product can=================================
        
        # ============contents of customer can=============================
        
        customerContCan=Canvas(customer_can,highlightthickness=0,bg='#ffffff')
        customerContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        
        # add back image
        cusBackImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/back2.png")
        cusBackImg5=cusBackImg5.resize((50,40),Image.ANTIALIAS)
        cusBackImg5=ImageTk.PhotoImage(cusBackImg5,master=main_window)
        cusDashLbl=Label(customerContCan,text="Back to Dashboard",bg='#ffffff',font=myfont,fg='black',image=cusBackImg5,compound=LEFT)
        cusDashLbl.place(relx=0.1,rely=0.08,relwidth=0.12)
        
        # add employee image
        
        insertCusLbl=Label(customerContCan,text="Add Customer",bg='#ffffff',font=myfont,bd=2,relief=GROOVE,fg='black',image=addCus_img,compound=RIGHT)
        insertCusLbl.place(relx=0.738,rely=0.08,relwidth=0.1)
        
        csvLbl=Label(customerContCan,text="Import CSV",bg='#ffffff',font=myfont,fg='black',bd=2,relief=GROOVE,compound=RIGHT)
        csvLbl.place(relx=0.84,rely=0.08,relheight=0.05)
        
        sachLbl=Label(customerContCan,text="Search",bg='lightgreen',font=myfont,fg='black',bd=2,relief=GROOVE,compound=RIGHT)
        sachLbl.place(relx=0.738,rely=0.14,relheight=0.05)
        serch_ent=Entry(customerContCan,bg='#ffffff',font=myfont,fg='black',bd=0)
        serch_ent.place(relx=0.78,rely=0.155)
        Frame(customerContCan,bg='brown').place(relx=0.78,rely=0.188,relwidth=0.12,relheight=0.001)
        
        cusTreeCan=Canvas(customerContCan,highlightthickness=0,bg='#ffffff')
        cusTreeCan.place(relx=0.1,rely=0.2,relheight=0.6,relwidth=0.8)
        # Creating a tree
        style=Style()
        style.theme_use('clam')
        cusTree=Treeview(cusTreeCan,columns=("column1","column2","column3","column4","column5"),show='headings',selectmode='browse')
        
        cusTree.column("column1",anchor=CENTER,width=80)
        cusTree.column("column2",anchor=CENTER,width=80)
        cusTree.column("column3",anchor=CENTER,width=80)
        cusTree.column("column4",anchor=CENTER,width=80)
        cusTree.column("column5",anchor=CENTER,width=80)
        
        cusTree.heading("#1",text="Product Name",anchor=CENTER)
        cusTree.heading("#2",text="Company Name",anchor=CENTER)
        cusTree.heading("#3",text="Quantity",anchor=CENTER)
        cusTree.heading("#4",text="Price",anchor=CENTER)
        cusTree.heading("#5",text="Use",anchor=CENTER)
        
        cusTree.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        # alternating colors
        cusTree.tag_configure("odd",background="#eee")
        cusTree.tag_configure("even",background="#ddd")
        
        # attaching scroll bars
        sb_vertical=Scrollbar(cusTreeCan,orient='vertical',command=cusTree.yview)
        sb_horizontal=Scrollbar(cusTreeCan,orient='horizontal',command=cusTree.xview)
        cusTree.configure(yscrollcommand=sb_vertical.set,xscrollcommand=sb_horizontal.set)
        sb_vertical.grid(row=0,column=1,sticky='ns')
        sb_horizontal.grid(row=1,column=0,sticky='ew')
        
        # configure position of grid for treeview
        cusTreeCan.grid_rowconfigure(0,weight=1)
        cusTreeCan.grid_columnconfigure(0,weight=1)
        
        # \\\\\\\\\\\\\\\\\insert Customer\\\\\\\\\\\\\\\\\
        insertCusCan=Canvas(customerContCan,highlightthickness=0,bg='#ffffff',bd=2,relief=RIDGE)
        # insertCan.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.48)
        
        closeInsertCusLbl=Label(insertCusCan,text='x',bg='#ffffff',fg='black',font=myfont3)
        closeInsertCusLbl.place(relx=0.96,rely=0.02)
        
        # creating profile image
        signProfileImg2=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/customer.jpg")
        signProfileImg2=signProfileImg2.resize((150,100),Image.ANTIALIAS)
        signProfileImg2=ImageTk.PhotoImage(signProfileImg2,master=main_window)
        Label(insertCusCan,text='',bg='beige',fg='black',image=signProfileImg2,font=myfont,bd=0).place(relx=0.44,rely=0.02)
        
        Label(insertCusCan,text='User Name',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.2)
        Label(insertCusCan,text='Last Name',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.3)
        Label(insertCusCan,text='Total',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.4)
        Label(insertCusCan,text='Location',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.5)
        Label(insertCusCan,text='Frequency',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.6)
        # Label(insertProdCan,text='Confirm Password',bg='#ffffff',fg='black',font=myfont).place(relx=0.3,rely=0.7)
        
        cusUserEnt=Entry(insertCusCan,font=myfont,textvariable=prodNameEntVar,bg='#ffffff',bd=0,fg='#191C1E')
        cusUserEnt.place(relx=0.3,rely=0.24,relwidth=0.46)
        cusLastEnt=Entry(insertCusCan,font=myfont,bg='#ffffff',textvariable=prodCompanyEntVar,bd=0,fg='#191C1E')
        cusLastEnt.place(relx=0.3,rely=0.34,relwidth=0.46)
        cusTotalEnt=Entry(insertCusCan,font=myfont,bg='#ffffff',textvariable=prodQtyEntVar,bd=0,fg='black')
        cusTotalEnt.place(relx=0.3,rely=0.44,relwidth=0.46)
        cusLocEnt=Entry(insertCusCan,font=myfont,textvariable=prodPriceEntVar,bg='#ffffff',bd=0,fg='black')
        cusLocEnt.place(relx=0.3,rely=0.54,relwidth=0.46)
        cusFreqEnt=Entry(insertCusCan,font=myfont,bg='#ffffff',textvariable=prodUseEntVar,bd=0,fg='black')
        cusFreqEnt.place(relx=0.3,rely=0.64,relwidth=0.46)
        cPassEnt=Entry(insertCusCan,font=myfont,bg='#ffffff',bd=0,fg='black')
        # cPassEnt.place(relx=0.3,rely=0.74,relwidth=0.45)
        
        # creating q image
        squizImg2=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/qa.jpg")
        squizImg2=squizImg2.resize((30,30),Image.ANTIALIAS)
        squizImg2=ImageTk.PhotoImage(squizImg2,master=main_window)
        Label(insertCusCan,text='',bg='#ffffff',fg='black',image=squizImg2,font=myfont,bd=0).place(relx=0.75,rely=0.735)
        
        # lines
        Frame(insertCusCan,bg='black').place(relx=0.3,rely=0.28,relwidth=0.46)
        Frame(insertCusCan,bg='black').place(relx=0.3,rely=0.38,relwidth=0.46)
        Frame(insertCusCan,bg='black').place(relx=0.3,rely=0.48,relwidth=0.46)
        Frame(insertCusCan,bg='black').place(relx=0.3,rely=0.58,relwidth=0.46)
        Frame(insertCusCan,bg='black').place(relx=0.3,rely=0.68,relwidth=0.46)
        Frame(insertCusCan,bg='black').place(relx=0.3,rely=0.18,relwidth=0.46)
        
        # Label(root1,text='Already signed up?',bg='#ffffff',fg='black',font=myfont).place(relx=0,rely=0.03) 
        # backLbl=Label(root1,text='Login',bg='#ffffff',fg='black',font=myfont1,bd=2,relief=RIDGE)
        # backLbl.place(relx=0.09,rely=0.03,relwidth=0.07)
        saveCusLbl=Label(insertCusCan,text='Save',bg='beige',fg='black',font=myfont1,bd=2,relief=RIDGE)
        saveCusLbl.place(relx=0.3,rely=0.8,relwidth=0.46)
        
        saveCusLbl=Label(insertCusCan,text='Save',bg='beige',fg='black',font=myfont1,bd=2,relief=RIDGE)
        saveCusLbl.place(relx=0.3,rely=0.8,relwidth=0.46)
        # ==========================End of Customer Can============================
        
        # ============contents of orders can=============================
        
        ordersContCan=Canvas(order_can,highlightthickness=0,bg='#ffffff')
        ordersContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        # add employee image
        addOderImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/addemp.png")
        addOderImg5=addOderImg5.resize((50,40),Image.ANTIALIAS)
        addOderImg5=ImageTk.PhotoImage(addOderImg5,master=main_window)
        addOrderLbl=Label(ordersContCan,text="Add Employees",bg='#ffffff',font=myfont,fg='black',image=addOderImg5,compound=RIGHT)
        addOrderLbl.place(relx=0.2,rely=0.01,relwidth=0.1)
        # add back image
        ordBackImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/back2.png")
        ordBackImg5=ordBackImg5.resize((50,40),Image.ANTIALIAS)
        ordBackImg5=ImageTk.PhotoImage(ordBackImg5,master=main_window)
        ordDashLbl=Label(ordersContCan,text="Back to Dashboard",bg='#ffffff',font=myfont,fg='black',image=ordBackImg5,compound=LEFT)
        ordDashLbl.place(relx=0,rely=0,relwidth=0.12)
        # ==========================End of order Can============================
        
        # ============contents of menu can=============================
        
        menuContCan=Canvas(menu_can,highlightthickness=0,bg='#ffffff')
        menuContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        # add employee image
        addmenuImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/addemp.png")
        addmenuImg5=addmenuImg5.resize((50,40),Image.ANTIALIAS)
        addmenuImg5=ImageTk.PhotoImage(addmenuImg5,master=main_window)
        addmenuLbl=Label(menuContCan,text="Add Employees",bg='#ffffff',font=myfont,fg='black',image=addmenuImg5,compound=RIGHT)
        addmenuLbl.place(relx=0.2,rely=0.01,relwidth=0.1)
        # add back image
        menuBackImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/back2.png")
        menuBackImg5=menuBackImg5.resize((50,40),Image.ANTIALIAS)
        menuBackImg5=ImageTk.PhotoImage(menuBackImg5,master=main_window)
        menuDashLbl=Label(menuContCan,text="Back to Dashboard",bg='#ffffff',font=myfont,fg='black',image=menuBackImg5,compound=LEFT)
        menuDashLbl.place(relx=0,rely=0,relwidth=0.12)
        # ==========================End of order Can============================
        
        # ============contents of location can=============================
        
        locContCan=Canvas(location_can,highlightthickness=0,bg='#ffffff')
        locContCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        # add employee image
        addLocImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/addemp.png")
        addLocImg5=addLocImg5.resize((50,40),Image.ANTIALIAS)
        addLocImg5=ImageTk.PhotoImage(addLocImg5,master=main_window)
        addLocLbl=Label(locContCan,text="Add Employees",bg='#ffffff',font=myfont,fg='black',image=addLocImg5,compound=RIGHT)
        addLocLbl.place(relx=0.2,rely=0.01,relwidth=0.1)
        # add back image
        locBackImg5=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dash_img/back2.png")
        locBackImg5=locBackImg5.resize((50,40),Image.ANTIALIAS)
        locBackImg5=ImageTk.PhotoImage(locBackImg5,master=main_window)
        locDashLbl=Label(locContCan,text="Back to Dashboard",bg='#ffffff',font=myfont,fg='black',image=locBackImg5,compound=LEFT)
        locDashLbl.place(relx=0,rely=0,relwidth=0.12)
        # ==========================End of location Can============================
        
        #====================== content of body can=================
        # Calculator screen
        screenCan=Canvas(body_can,highlightthickness=0,bg='#252526')
        screenCan.place(relx=0,rely=0,relheight=0.12,relwidth=0.28)
        
        
        
        # 'btn_click' function : 
        # This Function continuously updates the 
        # input field whenever you enter a number

        def btn_click(item):
            global expression
            expression = expression + str(item)
            input_text.set(expression)
            
        # 'StringVar()' :It is used to get the instance of input field
        input_text = StringVar()
        
        screenEnt=Entry(screenCan,bg='#252526',textvariable=input_text,font=myfont3,fg='#ffffff')
        screenEnt.pack(fill=BOTH,expand=True)
        
        admLbl=Label(body_can,text='Dashboard',bg='blue',font=myfont,fg='#ffffff')
        # admLbl.place(relx=0.05,rely=0.08,relheight=0.04)
        
        outLbl=Label(body_can,text='LOGOUT',bg='blue',font=myfont,fg='#ffffff')
        # outLbl.place(relx=0.2,rely=0.08,relheight=0.04)
        
        # ==================================Product Table===========================================
        # side can
        itemFrame=LabelFrame(body_can,text='Items in the inventory',bg='#ffffff',font=myfont,fg='blue')
        itemFrame.place(relx=0,rely=0.12,relheight=0.7,relwidth=0.28)
        
        closeItem_lbl=Label(itemFrame,text='X',bg='lightgreen',fg='#ffffff',font=('Arial',15))
        # closeItem_lbl.place(relx=0.95,rely=0)
        
        prodTreeCan1=Canvas(itemFrame,highlightthickness=0,bg='#ffffff')
        prodTreeCan1.place(relx=0,rely=0,relheight=1,relwidth=1)
        # Creating a product tree
        
        prodTree1=Treeview(prodTreeCan1,columns=("column1","column2","column3","column4","column5"),show='headings',selectmode='browse')
        
        prodTree1.column("column1",anchor=CENTER,width=80)
        prodTree1.column("column2",anchor=CENTER,width=80)
        prodTree1.column("column3",anchor=CENTER,width=80)
        prodTree1.column("column4",anchor=CENTER,width=80)
        prodTree1.column("column5",anchor=CENTER,width=80)
        
        
        
        prodTree1.heading("#1",text="Product Name",anchor=CENTER)
        prodTree1.heading("#2",text="Company Name",anchor=CENTER)
        prodTree1.heading("#3",text="Quantity",anchor=CENTER)
        prodTree1.heading("#4",text="Price",anchor=CENTER)
        prodTree1.heading("#5",text="Use",anchor=CENTER)
        
        prodTree1.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        # alternating colors
        prodTree.tag_configure("odd",background="#eee")
        prodTree.tag_configure("even",background="#ddd")
        
        # attaching scroll bars
        sb_vertical=Scrollbar(prodTreeCan1,orient='vertical',command=prodTree1.yview)
        sb_horizontal=Scrollbar(prodTreeCan1,orient='horizontal',command=prodTree1.xview)
        prodTree1.configure(yscrollcommand=sb_vertical.set,xscrollcommand=sb_horizontal.set)
        sb_vertical.grid(row=0,column=1,sticky='ns')
        sb_horizontal.grid(row=1,column=0,sticky='ew')
        
        # configure position of grid for treeview
        prodTreeCan1.grid_rowconfigure(0,weight=1)
        prodTreeCan1.grid_columnconfigure(0,weight=1)
        
        
        
        # ==========================Cart==================================
        cartFrame=LabelFrame(body_can,text='Items Selected',bg='lavender',font=myfont,fg='blue')
        cartFrame.place(relx=0,rely=0.7,relheight=0.3,relwidth=0.28)
        
        # Creating a tree
        style=Style()
        style.theme_use('clam')
        cartTree=Treeview(cartFrame,columns=("column1","column2","column3","column4"),show='headings',selectmode='browse')
        
        cartTree.column("column1",anchor=CENTER,width=80)
        cartTree.column("column2",anchor=CENTER,width=80)
        cartTree.column("column3",anchor=CENTER,width=80)
        cartTree.column("column4",anchor=CENTER,width=80)
        # cartTree.column("column5",anchor=CENTER,width=80)
        
        cartTree.heading("#1",text="Product Name",anchor=CENTER)
        
        cartTree.heading("#2",text="Quantity",anchor=CENTER)
        cartTree.heading("#3",text="Price",anchor=CENTER)
        cartTree.heading("#4",text="Total",anchor=CENTER)
        
        cartTree.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        # attaching scroll bars
        sb_vertical=Scrollbar(cartFrame,orient='vertical',command=cartTree.yview)
        sb_horizontal=Scrollbar(cartFrame,orient='horizontal',command=cartTree.xview)
        cartTree.configure(yscrollcommand=sb_vertical.set,xscrollcommand=sb_horizontal.set)
        sb_vertical.grid(row=0,column=1,sticky='ns')
        sb_horizontal.grid(row=1,column=0,sticky='ew')
        
        # configure position of grid for treeview
        cartFrame.grid_rowconfigure(0,weight=1)
        cartFrame.grid_columnconfigure(0,weight=1)
        
        
        
        # # Label(admFrame,text='Enter items into the database',bg='green',fg='#ffffff',font="Arial 20 bold underline").place(relx=0.1,rely=0)
        # Label(itemFrame,text='Bamburi Cement..................250 bags......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.07)
        # Label(itemFrame,text='Simba Cement..................250 bags......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.14)
        # Label(itemFrame,text='Nguvu Cement..................250 bags......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.21)
        # Label(itemFrame,text='Jembe..................250 items......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.28)
        # Label(itemFrame,text='T12 Doshi..................250 rods......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.35)
        # Label(itemFrame,text='Bamburi Cement..................250 bags......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.42)
        # Label(itemFrame,text='Simba Cement..................250 bags......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.49)
        # Label(itemFrame,text='Nguvu Cement..................250 bags......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.56)
        # Label(itemFrame,text='Jembe..................250 items......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.63)
        # Label(itemFrame,text='T12 Doshi..................250 rods......@900',bg='lightgreen',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.70)
        
        # Dashboard
        admFrame=LabelFrame(body_can,text='Dashboard',bg='lightgreen',font=myfont,fg='beige')
        # admFrame.place(relx=0,rely=0.12,relheight=1,relwidth=0.28)
        
        close_lbl=Label(admFrame,text='X',bg='green',fg='#ffffff',font=('Arial',15))
        close_lbl.place(relx=0.95,rely=0)
        
        Label(admFrame,text='Enter items into the database',bg='green',fg='#ffffff',font="Arial 20 bold underline").place(relx=0.1,rely=0)
        Label(admFrame,text='Enter Item',bg='green',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.07)
        Label(admFrame,text='Enter Quantity',bg='green',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.14)
        Label(admFrame,text='Enter price/kg',bg='green',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.21)
        Label(admFrame,text='Enter items',bg='green',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.28)
        Label(admFrame,text='Enter items',bg='green',fg='#ffffff',font=('Arial',15)).place(relx=0.04,rely=0.35)
        
        itemEnt=Entry(admFrame,font=myfont,bg='beige',fg='green')
        itemEnt.place(relx=0.34,rely=0.07)
        itemEnt=Entry(admFrame,font=myfont,bg='beige',fg='green')
        itemEnt.place(relx=0.34,rely=0.14)
        itemEnt=Entry(admFrame,font=myfont,bg='beige',fg='green')
        itemEnt.place(relx=0.34,rely=0.21)
        itemEnt=Entry(admFrame,font=myfont,bg='beige',fg='green')
        itemEnt.place(relx=0.34,rely=0.28)
        itemEnt=Entry(admFrame,font=myfont,bg='beige',fg='green')
        itemEnt.place(relx=0.34,rely=0.35)
        # itemEnt=Entry(admFrame,font=myfont,bg='beige',fg='green')
        # itemEnt.place(relx=0.34,rely=0.07)
        
        admLbl=Label(admFrame,text='Submit',bg='blue',font=myfont,fg='#ffffff')
        admLbl.place(relx=0.35,rely=0.4,relheight=0.04)
        
        
        # separator can 
        separatorCan=Canvas(body_can,highlightthickness=0,bg='black')
        separatorCan.place(relx=0.28,rely=0,relheight=1,relwidth=0.05)
        # concan
        contCa=Canvas(body_can,highlightthickness=0,bg='lightgreen')
        contCa.place(relx=0.33,rely=0,relheight=1,relwidth=0.7)
        
        # function to resize image
        def resizeImage(image):
            img=Image.open(image)
            img=img.resize((70,70),Image.ANTIALIAS)
            img=ImageTk.PhotoImage(img)
            return img
        
        cart_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/cart2.jpg")
        # cart_img=ImageTk.PhotoImage(image1)
        overide_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/overide.jpg")
        # overide_img=ImageTk.PhotoImage(image2)
        dolar_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/dolar.jpg")
        # dolar_img=ImageTk.PhotoImage(image3)
        void_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/x.jpg")
        # void_img=ImageTk.PhotoImage(image4)
        pesa_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/pesa.jpg")
        # pesa_img=ImageTk.PhotoImage(image5)
        file_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/file.jpg")
        # file_img=ImageTk.PhotoImage(image6)
        xchange_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/exchange.jpg")
        # xchange_img=ImageTk.PhotoImage(image7)
        change_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/change.jpg")
        # change_img=ImageTk.PhotoImage(image8)
        box_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/box.jpg")
        # box_img=ImageTk.PhotoImage(image9)
        voucher_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/voucher.jpg")
        # voucher_img=ImageTk.PhotoImage(image10)
        off_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/pesaOff.jpg")
        # off_img=ImageTk.PhotoImage(image11)
        eft_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/offEft.jpg")
        # eft_img=ImageTk.PhotoImage(image12)
        lock_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/lock.jpg")
        # lock_img=ImageTk.PhotoImage(image13)
        foreign_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/foreign.jpg")
        # foreign_img=ImageTk.PhotoImage(image14)
        evoucher_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/evoucher.jpg")
        # evoucher_img=ImageTk.PhotoImage(image15)
        quantity_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/quantity.jpg")
        # quantity_img=ImageTk.PhotoImage(image16)
        layby_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/layby.jpg")
        # layby_img=ImageTk.PhotoImage(image17)
        buyer_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/buyer.jpg")
        # buyer_img=ImageTk.PhotoImage(image18)
        clear_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/clear.jpg")
        # clear_img=ImageTk.PhotoImage(image19)
        nsale_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/nsale.jpg")
        # nsale_img=ImageTk.PhotoImage(image20)
        onEft_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/onEft.jpg")
        # onEft_img=ImageTk.PhotoImage(image21)
        enter_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/enter.jpg")
        # enter_img=ImageTk.PhotoImage(image22)
        total_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/total.jpg")
        # total_img=ImageTk.PhotoImage(image23)
        cash_img=resizeImage(r"C:/Users/Clone Technologies/Downloads/projects/pos system/cash.jpg")
        # cash_img=ImageTk.PhotoImage(image24)
        # cart_img=ImageTka
        
        image_carefor=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/care.jpg")
        image_carefor=image_carefor.resize((150,100),Image.ANTIALIAS)
        image_carefor=ImageTk.PhotoImage(image_carefor,master=main_window)
        
        careLbl=Label(contCa,text='',font=myfont2,bg='#ffffff',fg='blue',width=210,height=142,image=image_carefor,bd=2,relief=RIDGE,compound=BOTTOM)
        careLbl.grid(row=0,column=0)
        titfr=Frame(contCa,bg='#ffffff',bd=3,relief=RIDGE,width=54,height=4)
        titfr.place(relx=0.1598,rely=0,relwidth=0.645,relheight=0.163)
        
        # titCan=Canvas(titfr,bg='red',highlightthickness=0)
        # titCan.place(relx=0,rely=0,relwidth=1,relheight=1)
        # # adding background image
        # main_window.update_idletasks()
        # imgWidth=titCan.winfo_width()
        # imgHeight=titCan.winfo_height()
        # titImg=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/shop.jpg" )
        # titImg=titImg.resize((500,170),Image.ANTIALIAS)
        # titImg=ImageTk.PhotoImage(titImg,master=main_window)
        # titCan.create_image(0,0,anchor="nw",image=titImg)
        # titCan.image=titImg
        
        # i,age for label
        shop_img=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/shop.jpg")
        shop_img=shop_img.resize((150,100),Image.ANTIALIAS)
        shop_img=ImageTk.PhotoImage(shop_img,master=main_window)
        
        picLbl=Label(titfr,text='',font=myfont,bg='#ffffff',fg='blue',width=210,height=142,image=shop_img,bd=0)
        picLbl.place(relx=0.5,rely=0,relheight=1,relwidth=0.5)
        saleLbl=Label(titfr,text='SALES TERMINAL',font=('Arial',45,'bold'),bg='#ffffff',fg='blue',bd=0,relief=RIDGE)
        saleLbl.place(relx=0.03,rely=0.21)
        
        careLbl=Label(contCa,text='',font=myfont,bg='#ffffff',fg='blue',width=210,height=142,image=image_carefor,bd=2,relief=RIDGE)
        careLbl.grid(row=0,column=5)
        
        image_cart=Image.open(r"C:/Users/Clone Technologies/Downloads/projects/pos system/cart2.jpg")
        image_cart=image_cart.resize((70,70),Image.ANTIALIAS)
        image_cart=ImageTk.PhotoImage(image_cart,master=main_window)
        
        careLbl=Label(contCa,text='Cart',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=image_cart,bd=2,relief=RIDGE,compound=TOP)
        careLbl.image=cart_img
        careLbl.grid(row=1,column=0)
        careLbl=Label(contCa,text='Price Overide',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=overide_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=1,column=1)
        careLbl=Label(contCa,text='Overide',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=dolar_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=1,column=2)
        careLbl=Label(contCa,text='Void',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=void_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=1,column=3)
        careLbl=Label(contCa,text='MPESA G2',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=pesa_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=1,column=4)
        careLbl=Label(contCa,text='LPO',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=file_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=1,column=5)
        
        careLbl=Label(contCa,text='Exchange',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=xchange_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=2,column=0)
        careLbl=Label(contCa,text='Change',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=change_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=2,column=1)
        careLbl=Label(contCa,text='Pickup',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=box_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=2,column=2)
        careLbl=Label(contCa,text='Gift Voucher',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=voucher_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=2,column=3)
        careLbl=Label(contCa,text='MPESA offline',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=off_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=2,column=4)
        careLbl=Label(contCa,text='Offline EFT',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=eft_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=2,column=5)
        
        
        logoutLbl=Label(contCa,text='sign on/off',font=myfont,bg='#ffffff',fg='blue',width=210,height=125,image=lock_img,bd=2,relief=RIDGE,compound=TOP)
        logoutLbl.grid(row=3,column=3)
        careLbl=Label(contCa,text='Foreign Currency',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=foreign_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=3,column=4)
        careLbl=Label(contCa,text='E-Voucher icon',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=evoucher_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=3,column=5)
        
        
        # careLbl.grid(row=4,column=2,padx=(0,2),pady=2)
        careLbl=Label(contCa,text='Quantity',font=myfont,bg='#ffffff',fg='blue',width=210,height=125,image=quantity_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=4,column=3)
        careLbl=Label(contCa,text='Lay By',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=layby_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=4,column=4)
        careLbl=Label(contCa,text='Buyer Pin',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=buyer_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=4,column=5)
        
        
        # careLbl.grid(row=5,column=2,padx=(0,2),pady=2)
        clrBtn=Button(contCa,text='Clear',font=myfont,bg='#ffffff',fg='blue',width=208,height=123,image=clear_img,bd=2,relief=RIDGE,compound=TOP,command=lambda:btn_click(""))
        clrBtn.grid(row=5,column=3)
        careLbl=Label(contCa,text='No Sale',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=nsale_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=5,column=4)
        careLbl=Label(contCa,text='Online EFT',font=myfont,bg='#eee',fg='blue',width=210,height=125,image=onEft_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=5,column=5)
        
        
        enterLbl=Label(contCa,text='Enter',font=myfont,bg='#ffffff',fg='blue',width=210,height=100,image=enter_img,bd=2,relief=RIDGE,compound=TOP)
        enterLbl.grid(row=6,column=3)
        careLbl=Label(contCa,text='Total',font=myfont,bg='#eee',fg='blue',width=210,height=100,image=total_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=6,column=4)
        careLbl=Label(contCa,text='Cash',font=myfont,bg='#eee',fg='blue',width=210,height=100,image=cash_img,bd=2,relief=RIDGE,compound=TOP)
        careLbl.grid(row=6,column=5)
        
        # Button cnavas
        butCan=Frame(contCa,highlightthickness=0,bd=2,relief=RIDGE)
        butCan.place(relx=0,rely=0.45,relheight=0.55,relwidth=0.482)
        
        
        
        sevenbl=Button(butCan,text='7',font=myfont,bg='#ffffff',fg='blue',width=19,height=5,bd=1,relief=RIDGE,cursor='hand2',command=lambda:btn_click("7"))
        sevenbl.grid(row=0,column=0)
        eightLbl=Button(butCan,text='8',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=5,cursor='hand2',command=lambda:btn_click("8"))
        eightLbl.grid(row=0,column=1,padx=1)
        nineLbl=Button(butCan,text='9',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=5,cursor='hand2',command=lambda:btn_click("9"))
        nineLbl.grid(row=0,column=2)
        
        fourLbl=Button(butCan,text='4',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=5,cursor='hand2',command=lambda:btn_click("4"))
        fourLbl.grid(row=1,column=0)
        fiveLbl=Button(butCan,text='5',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=5,cursor='hand2',command=lambda:btn_click("5"))
        fiveLbl.grid(row=1,column=1,padx=1)
        sixBtn=Button(butCan,text='6',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=5,cursor='hand2',command=lambda:btn_click("6"))
        sixBtn.grid(row=1,column=2)
        
        oneLbl=Button(butCan,text='1',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=5,cursor='hand2',command=lambda:btn_click("1"))
        oneLbl.grid(row=2,column=0)
        twoLbl=Button(butCan,text='2',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=5,cursor='hand2',command=lambda:btn_click("2"))
        twoLbl.grid(row=2,column=1,padx=1)
        threeLbl=Button(butCan,text='3',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=5,cursor='hand2',command=lambda:btn_click("3"))
        threeLbl.grid(row=2,column=2)
        
        zeroLbl=Button(butCan,text='0',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=4,cursor='hand2',command=lambda:btn_click("0"))
        zeroLbl.grid(row=3,column=0)
        clearLbl=Button(butCan,text='C',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=4,cursor='hand2',command=lambda:btn_click(""))
        clearLbl.grid(row=3,column=1,padx=1)
        divideBtn=Button(butCan,text='/',font=myfont,bg='#ffffff',fg='blue',bd=1,relief=RIDGE,width=19,height=4,cursor='hand2',command=lambda:btn_click("/"))
        divideBtn.grid(row=3,column=2)
        
        
        
        # --------------------------------INSERT EMPLOYEE-------------------------------
        def insertEmployee(event):
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            
            if useEnt.get()=='' or lastEnt.get()=='' or roleEnt.get()=='' or idEnt.get()=='':
                response=messagebox.showerror("Error","Please complete the required fields")
            else:
                # print('==========Connect to db=============')
                c.execute("SELECT * FROM eployee WHERE 'username'=%s",(useEntVar.get(),))
                # print('==========Almost there to db=============')
                if c.fetchone() is not None:
                    response=messagebox.showerror("Unsuccesful","Username already exist")
                else:
                    
                    c.execute("INSERT INTO eployee(username,last_name,role,password,national_id) VALUES (%s,%s,%s,%s,%s)",
                            (useEntVar.get(),lastEntVar.get(),roleEntVar.get(),passEntVar.get(),idEntVar.get())
                            )
                    conn.commit()
                    conn.close()
                    closeAddEmployee(event)
                    displayEmployee()
                    useEntVar.set('')
                    lastEntVar.set('')
                    roleEntVar.set('')
                    passEntVar.set('')
                    idEntVar.set('')
                    response=messagebox.showinfo("succesful","Data inserted succesfully")
                # root1.destroy()
                
        signEmpLbl.bind("<ButtonPress>",insertEmployee)
        signLbl.bind("<ButtonPress>",insertEmployee)
        
        def displayEmployee():
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            c.execute("SELECT * FROM eployee")
            fetch=c.fetchall()
            
            for i in empTree.get_children():
                empTree.delete(i)
            main_window.update()
            style.map("TreeView",background=[('selected','blue')])
            empTree.tag_configure('oddrow',background='lime')
            empTree.tag_configure('evenrow',background='lavender')
            # getch data and change color of rows
            x=1
            for data in fetch:
                if x % 2==0:
                    empTree.insert('','end',values=data,tags=('evenrow','row'))
                else:
                    empTree.insert('','end',values=data,tags=("oddrow","row"))
                    x+=1
        displayEmployee()
        
        def log_in(event):
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            
            username = logUseEntVar.get()
            password = logPassEntVar.get()
            
            if logUseEntVar.get()=='' or logPassEntVar.get()=='':
                response=messagebox.showerror("Error","Please complete the required fields")
            else:
                select_query = 'SELECT * FROM `eployee` WHERE `username` = %s and password = %s'
                vals = (username, password,)
                c.execute(select_query, vals)
                #print(c.fetchall())
                user = c.fetchone()
                if user is not None:
                    #messagebox.showinfo('Login', 'Yes')
                    # mainformwindow = tk.Toplevel()
                    # app = mainform(mainformwindow)
                    # root.withdraw()
                    # mainformwindow.protocol('WM_DELETE_WINDOW', close_window)
                    
                    response=messagebox.showinfo("Success","Query Executed successfully")
                    loadBodyCan(event)
                    
                else:
                    messagebox.showwarning('Error', 'Enter a Valid Username & Password')
                    
                    # conn.commit()
                    conn.close()
                    
                
                
        logLbl.bind("<ButtonPress>",log_in)
        
        # ----------------------------------------CLOSE INSERT EMPLOYEE----------------------------
        
        # -=----------------------------INSERT PRODUCT--------------------------------------
        
        def insertpRODUCT(event):
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            
            if prodNameEntVar.get()=='' or prodCompanyEntVar.get()=='' or prodQtyEntVar.get()=='' or prodPriceEntVar.get()=='':
                response=messagebox.showerror("Error","Please complete the required fields")
            else:
                # print('==========Connect to db=============')
                c.execute("SELECT * FROM product WHERE 'product_name'=%s",(prodNameEntVar.get(),))
                # print('==========Almost there to db=============')
                if c.fetchone() is not None:
                    response=messagebox.showerror("Unsuccesful","Product name already exist")
                else:
                    
                    c.execute("INSERT INTO product(product_name,company,quantity,price,product_use) VALUES (%s,%s,%s,%s,%s)",
                            (prodNameEntVar.get(),prodCompanyEntVar.get(),prodQtyEntVar.get(),prodPriceEntVar.get(),prodUseEntVar.get())
                            )
                    conn.commit()
                    conn.close()
                    closeAddProduct(event)
                    displayProduct()
                    displayProduct1()
                    prodNameEntVar.set('')
                    prodCompanyEntVar.set('')
                    prodQtyEntVar.set('')
                    prodPriceEntVar.set('')
                    prodUseEntVar.set('')
                    response=messagebox.showinfo("succesful","Data inserted succesfully")
                # root1.destroy()
                
        saveProdLbl.bind("<ButtonPress>",insertpRODUCT)
        
        def displayProduct():
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            c.execute("SELECT product_name,company,quantity,price,product_use FROM product")
            fetch=c.fetchall()
            
            for i in prodTree.get_children():
                prodTree.delete(i)
            main_window.update()
            # getch data and change color of rows
            x=1
            for data in fetch:
                if x % 2==0:
                    prodTree.insert('','end',values=data,tags=('even','row'))
                else:
                    prodTree.insert('','end',values=data,tags=("odd","row"))
                    x+=1
        displayProduct()
        def displayProduct1():
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            c.execute("SELECT product_name,company,quantity,price,product_use FROM product")
            fetch=c.fetchall()
            
            for i in prodTree1.get_children():
                prodTree1.delete(i)
            main_window.update()
            # getch data and change color of rows
            x=1
            for data in fetch:
                if x % 2==0:
                    prodTree1.insert('','end',values=data,tags=('even','row'))
                else:
                    prodTree1.insert('','end',values=data,tags=("odd","row"))
                    x+=1
        displayProduct1()
        
        # display cart
        def displayCart():
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            c.execute("SELECT product_name,quantity,price FROM product")
            fetch=c.fetchall()
            
            for i in cartTree.get_children():
                cartTree.delete(i)
            main_window.update()
            # getch data and change color of rows
            x=1
            for data in fetch:
                if x % 2==0:
                    cartTree.insert('','end',values=data,tags=('even','row'))
                else:
                    cartTree.insert('','end',values=data,tags=("odd","row"))
                    x+=1
        displayCart()
        
        def searchProd(ev):
            
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            
            try:
                c.execute("SELECT * FROM product WHERE product_name LIKE '%"+searchProd_entV.get()+"%'")
                row=c.fetchall()
                
                if len(row) > 0:
                    prodTree.delete(*prodTree.get_children())
                    for i in row:
                        prodTree.insert('', END,values=i)
                        
                else:
                    prodTree.delete(*prodTree.get_children())
                    
            except Exception as ex:
                response=messagebox.showerror("Error","Error due to {str(ex)}")
        searchProd_ent.bind("<Key>",searchProd)
        
        
        
                
        # selecting a produt to edit        # 
        def selectProd(event):
            # clear the fields
            prodNameEntVar.set('')
            prodCompanyEntVar.set('')
            prodQtyEntVar.set('')
            prodPriceEntVar.set('')
            prodUseEntVar.set('')
            
            # grab record number
            selected=prodTree.focus()
            # grab record values
            values=prodTree.item(selected,'values')
            insertProdCan.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.48)
            # output to entry boxes
            prodNameEnt.insert(0,values[0])
            prodCompanyEnt.insert(0,values[1])
            prodQtyEnt.insert(0,values[2])
            prodPriceEnt.insert(0,values[3])
            prodUseEnt.insert(0,values[4])
        prodTree.bind("<ButtonRelease-1>",selectProd)
        
        def clrProd(event):
            # clear the fields
            prodNameEntVar.set('')
            prodCompanyEntVar.set('')
            prodQtyEntVar.set('')
            prodPriceEntVar.set('')
            prodUseEntVar.set('')
            
        clrProdLbl.bind("<ButtonPress>",clrProd)
        
        # update product
        def updProd(event):
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="pos.db")
            c=conn.cursor()
            fetch=c.execute("SELECT * FROM product WHERE 'product_name'=%s",(prodNameEntVar.get(),))
            fetch=fetch.fetchone()
            prodname=fetch[0]
            
            c.execute("UPDATE product SET 'company'=%s,'quantity'=%s,'price'=%s,'product_use'=%s WHERE product_name={prodname}",
                      (prodCompanyEnt.get(),prodQtyEntVar.get(),prodPriceEntVar.get(),prodUseEntVar.get(),))
            if c.fetchone()
            fetch=c.fetchone()
            # # product_name,company,quantity,price,product_use
            # product_name=fetch[0]
            # company=fetch[1]
            # quantity=fetch[2]
            # pr
            
    
        #=====================  Calculator functions============================
        # 'bt_clear' function :This is used to clear 
        # the input field

        def bt_clear(event): 
            global expression 
            expression = "" 
            screenEnt.set("")
        clearLbl.bind('<ButtonPress>',bt_clear)
        
        # 'btn_click' function : 
        # This Function continuously updates the 
        # input field whenever you enter a number

        
            
        def openDashboard(event):
            # itemFrame.place_forget()
            admFrame.place(relx=0,rely=0.12,relheight=1,relwidth=0.28)
        admLbl.bind("<ButtonPress>",openDashboard)
        
        def closeDashboard(event):
            admFrame.place_forget()
            itemFrame.place(relx=0,rely=0.12,relheight=1,relwidth=0.28)
        close_lbl.bind("<ButtonPress>",closeDashboard)
        
        def closeDatabase(event):
            itemFrame.place_forget()
            admFrame.place(relx=0,rely=0.12,relheight=1,relwidth=0.28)
        closeItem_lbl.bind("<ButtonPress>",closeDatabase)
        
        def press(num):
            # point out the global expression variable
            global expression
        
            # concatenation of string
            expression = expression + str(num)
        
            # update the expression by using set method
            # equation.set(expression)
            
        # forget multcan
        def forgetContentCan(event):
            for canvas in content_list:
                canvas.place_forget()
                
        # functions to load canvases
        def loadLogCan(event):
            forgetContentCan(event)
            log_can.place(relx=0,rely=0,relwidth=1,relheight=1)
        backLbl.bind('<ButtonPress>',loadLogCan)
        outLbl.bind('<ButtonPress>',loadLogCan)
        adminOutLbl.bind('<ButtonPress>',loadLogCan)
        logoutLbl.bind('<ButtonPress>',loadLogCan)
            
        def loadSignCan(event):
            forgetContentCan(event)
            sign_can.place(relx=0,rely=0,relwidth=1,relheight=1)
        # logLbl.bind('<ButtonPress>',loadSignCan)
        
        def loadBodyCan(event):
            forgetContentCan(event)
            body_can.place(relx=0,rely=0,relwidth=1,relheight=1)
        # signLbl.bind('<ButtonPress>',loadBodyCan)
        toSignLbl.bind('<ButtonPress>',loadBodyCan)
        
        # [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ Dashboard ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
        def loadAdminCan(event):
            forgetContentCan(event)
            self.admin_can.place(relx=0,rely=0,relwidth=1,relheight=1)
            # ADMINDASHBOARD(event)
        admLogLbl.bind('<ButtonPress>',loadAdminCan)
        EmpDashLbl.bind('<ButtonPress>',loadAdminCan)
        prodDashLbl.bind('<ButtonPress>',loadAdminCan)
        enterLbl.bind('<ButtonPress>',loadAdminCan)
        cusDashLbl.bind('<ButtonPress>',loadAdminCan)
        ordDashLbl.bind('<ButtonPress>',loadAdminCan)
        menuDashLbl.bind('<ButtonPress>',loadAdminCan)
        locDashLbl.bind('<ButtonPress>',loadAdminCan)
        
        
        
        def loadEmpCan(event):
            forgetContentCan(event)
            emp_can.place(relx=0,rely=0,relwidth=1,relheight=1)
            # ADMINDASHBOARD(event)
        employee_openLbl.bind('<ButtonPress>',loadEmpCan)
        # enterLbl.bind('<ButtonPress>',loadAdminCan)
        
        def loadProdCan(event):
            forgetContentCan(event)
            prod_can.place(relx=0,rely=0,relwidth=1,relheight=1)
            # ADMINDASHBOARD(event)
        prodOpenLbl.bind('<ButtonPress>',loadProdCan)
        # enterLbl.bind('<ButtonPress>',loadProdCan)
        
        def loadCustomerCan(event):
            forgetContentCan(event)
            customer_can.place(relx=0,rely=0,relwidth=1,relheight=1)
            # ADMINDASHBOARD(event)
        CustOpenLbl.bind('<ButtonPress>',loadCustomerCan)
        # enterLbl.bind('<ButtonPress>',loadProdCan)
        
        def loadOrderCan(event):
            forgetContentCan(event)
            order_can.place(relx=0,rely=0,relwidth=1,relheight=1)
            # ADMINDASHBOARD(event)
        OrdOpenLbl.bind('<ButtonPress>',loadOrderCan)
        # enterLbl.bind('<ButtonPress>',loadProdCan)
        
        def loadMenuCan(event):
            forgetContentCan(event)
            menu_can.place(relx=0,rely=0,relwidth=1,relheight=1)
            # ADMINDASHBOARD(event)
        MenuOpenLbl.bind('<ButtonPress>',loadMenuCan)
        # enterLbl.bind('<ButtonPress>',loadProdCan)
        
        def loadLocationCan(event):
            forgetContentCan(event)
            location_can.place(relx=0,rely=0,relwidth=1,relheight=1)
            # ADMINDASHBOARD(event)
        locOpenLbl.bind('<ButtonPress>',loadLocationCan)
        # enterLbl.bind('<ButtonPress>',loadProdCan)
        
        # add employee
        def addEmployee(event):
            insertCan.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.48)
            useEntVar.set('')
            lastEntVar.set('')
            roleEntVar.set('')
            passEntVar.set('')
            idEntVar.set('')
        insertEmpLbl.bind("<ButtonPress>",addEmployee)
        
        def closeAddEmployee(event):
            insertCan.place_forget()
        closeInsertLbl.bind("<ButtonPress>",closeAddEmployee)
        
        # add product
        def addProduct(event):
            insertProdCan.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.48)
            prodNameEntVar.set('')
            prodCompanyEntVar.set('')
            prodQtyEntVar.set('')
            prodPriceEntVar.set('')
            prodUseEntVar.set('')
        insertProdLbl.bind("<ButtonPress>",addProduct)
        
        def closeAddProduct(event):
            insertProdCan.place_forget()
        closeInsertProdLbl.bind("<ButtonPress>",closeAddProduct)
        
        # add customer
        def addCustomer(event):
            insertCusCan.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.48)
        insertCusLbl.bind("<ButtonPress>",addCustomer)
        
        def closeAddCustomer(event):
            insertCusCan.place_forget()
        closeInsertCusLbl.bind("<ButtonPress>",closeAddCustomer)
        
        # Functionality to enable dragging the window
        def save_last_pos(event):
            global lastClickX,lastClickY
            lastClickx=event.x
            lastClicky=event.y
            
        def dragging(event):
            x,y=event.x-lastClickX + main_window.winfo_x(),event.y - lastClickY + main_window.winfo_y()
            main_window.geometry("+{0}+{1}".format(x,y))
            
        closeCan.bind("<ButtonPress>",dragging)
        closeCan.bind("<ButtonPress>",save_last_pos)
        
        def minimize_window():
            main_window.wm_overrideredirect(0)
            main_window.iconify()
            
        def winfocuse():
            if main_window.state()=='normal':
                main_window.overrideredirect(1)
                
        def hover(event):
            close_lbl.configure(foreground='red')
            closeInsertLbl.configure(foreground='red')
            closeItem_lbl.configure(foreground='red')
            closeInsertProdLbl.configure(foreground='red')
        
        def leave(event):
            close_lbl.configure(foreground='white')
            
        def hover1(event):
            minimize_lbl.configure(foreground='cyan')
        def leave1(event):
            minimize_lbl.configure(foreground='white')
                
        winfocuse()
        
        minimize_lbl.bind('<ButtonPress>',minimize_window)
        
        log_can.place(relx=0,rely=0,relheight=1,relwidth=1)
        
        main_window.mainloop()
 

        
MAINAPPLICATION()
