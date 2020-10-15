import tkinter
from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk 
import time
import datetime

root = Tk()
root.geometry("1390x1400")
root.title("Cafeso")
color = 'black'
root.configure(background='grey25')
Tops = Frame(root,bg="white",width = 1200,height=40,relief='sunken',borderwidth=2)
Tops.pack(side=TOP)
#------------------TIME--------------
logo =Label(Tops,relief='raise',borderwidth=2,bg=color)
logo_open = Image.open('a.jpg')
logo_img = ImageTk.PhotoImage(logo_open) 
logo.config(image=logo_img)
logo.grid(row=0,column=1)



lblinfo1 = Label(Tops, font=( 'arial' ,20 ),text="Cafeso",fg="black",bd=10,anchor='w')
lblinfo1.grid(row=0,column=0)
def tick():
    localtime=time.strftime("Time: %H:%M:%S:%p")
    clock.config(text=localtime)
    clock.after(1000,tick)
clock=Label(Tops,font=("times",15))
clock.grid(row=1,column=1)
tick()
localdate=datetime.date.today().strftime("Date: %d-%m-%Y")
date=Label(Tops,font=("times",15))
date.grid(row=1,column=0)
date.config(text=localdate)
#--------------------------------------------------------------
global pizza1_quantity
pizza1_total=0
pizza1_quantity = 0
def pizza1_click():
    global pizza1_quantity
    pizza1_quantity += 1
    pizza1_label.config(text = pizza1_quantity)
#------
global pizza2_quantity
pizza2_total=0
pizza2_quantity = 0
def pizza2_click():
    global pizza2_quantity
    pizza2_quantity += 1
    pizza2_label.config(text = pizza2_quantity)
#------
global pizza3_quantity
pizza3_total=0
pizza3_quantity = 0
def pizza3_click():
    global pizza3_quantity
    pizza3_quantity += 1
    pizza3_label.config(text = pizza3_quantity)
#------
global drink1_quantity
drink1_total=0
drink1_quantity = 0
def drink1_click():
    global drink1_quantity
    drink1_quantity+=1
    drink1_label.config(text=drink1_quantity)
#------
global drink2_quantity
drink2_total=0
drink2_quantity = 0
def drink2_click():
    global drink2_quantity
    drink2_quantity+=1
    drink2_label.config(text=drink2_quantity)
#------
global drink3_quantity
drink3_total=0
drink3_quantity = 0
def drink3_click():
    global drink3_quantity
    drink3_quantity+=1
    drink3_label.config(text=drink3_quantity)
#------

global icecream_quantity
icecream_total=0
icecream_quantity = 0
def icecream_click():
    global icecream_quantity
    icecream_quantity+=1
    icecream_label.config(text=icecream_quantity)
#------
global donut_quantity
donut_total=0
donut_quantity = 0
def donut_click():
    global donut_quantity
    donut_quantity+=1
    donut_label.config(text=donut_quantity)



total=0
total_quantity=0
def total_click():
     global pizza1_total
     global pizza2_total
     global pizza3_total
     global drink1_total
     global drink2_total
     global drink3_total
     global icecream_total
     global donut_total
     global total
     global total_quantity
     pizza1_total=pizza1_quantity*500
     pizza2_total=pizza2_quantity*400
     pizza3_total=pizza3_quantity*350
     drink1_total=drink1_quantity*100
     drink2_total=drink2_quantity*90
     drink3_total=drink3_quantity*80
     icecream_total=icecream_quantity*100
     donut_total=donut_quantity*150
     total=(pizza1_total+pizza2_total+pizza3_total+drink1_total+drink2_total+drink3_total+icecream_total+donut_total)
     totalprice_label.config(text=total)
     total_quantity=(pizza1_quantity+pizza2_quantity+pizza3_quantity+drink1_quantity+drink2_quantity+drink3_quantity+icecream_quantity+donut_quantity)
     



def order_click():
    
        ##############################################################################################
        windows1= Toplevel(root)
        windows1.title("BIll")
        windows1.geometry("500x700+0+0")
        logo1 =Label(windows1,relief='raise',borderwidth=2)
        lblinfo1 = Label(windows1, font=( 'arial' ,20 ),text="Cafeso",fg="black",bd=10,anchor='w')
        lblinfo1.place(x=210,y=5)
        bill_time=time.asctime(time.localtime(time.time()))
        bill_timel=Label(windows1,text="",font=("Verdana",10))
        bill_timel.place(x=20,y=130)
        bill_timel.config(text=bill_time)

       
        foodname_bill=Label(windows1,text="food items",font=("Verdana",9),relief="solid")
        foodname_bill.place(x=20,y=180)
        foodquantity_bill=Label(windows1,text="Quantity",font=("Verdana",9),relief="solid")
        foodquantity_bill.place(x=210,y=180)
        foodprice_bill=Label(windows1,text="Price: Rs.",font=("Verdana",9),relief="solid")
        foodprice_bill.place(x=350,y=180)

        pizza1n_bill=Label(windows1,text="Fully Loaded Pizza",font=("Verdana",9),relief="sunken")
        pizza1n_bill.place(x=20,y=220)
        pizza1q_bill=Label(windows1,text="0",font=("Verdana",9))
        pizza1q_bill.place(x=210,y=220)
        pizza1q_bill.config(text = pizza1_quantity)
        pizza1t_bill=Label(windows1,text="0",font=("Verdana",9))
        pizza1t_bill.place(x=350,y=220)
        pizza1t_bill.config(text = pizza1_total)

        pizza2n_bill=Label(windows1,text="Paneer Pizza",font=("Verdana",9),relief="sunken")
        pizza2n_bill.place(x=20,y=270)
        pizza2q_bill=Label(windows1,text="0",font=("Verdana",9))
        pizza2q_bill.place(x=210,y=270)
        pizza2q_bill.config(text = pizza2_quantity)
        pizza2t_bill=Label(windows1,text="0",font=("Verdana",9))
        pizza2t_bill.place(x=350,y=270)
        pizza2t_bill.config(text = pizza2_total)

        pizza3n_bill=Label(windows1,text="Pepperoni Pizza",font=("Verdana",9),relief="sunken")
        pizza3n_bill.place(x=20,y=320)
        pizza3q_bill=Label(windows1,text="0",font=("Verdana",9))
        pizza3q_bill.place(x=210,y=320)
        pizza3q_bill.config(text = pizza3_quantity)
        pizza3t_bill=Label(windows1,text="0",font=("Verdana",9))
        pizza3t_bill.place(x=350,y=320)
        pizza3t_bill.config(text = pizza3_total)

        drink1n_bill=Label(windows1,text="Oreo Milkshake",font=("Verdana",9),relief="sunken")
        drink1n_bill.place(x=20,y=370)
        drink1q_bill=Label(windows1,text="0",font=("Verdana",9))
        drink1q_bill.place(x=210,y=370)
        drink1q_bill.config(text = drink1_quantity)
        drink1t_bill=Label(windows1,text="0",font=("Verdana",9))
        drink1t_bill.place(x=350,y=370)
        drink1t_bill.config(text = drink1_total)

        drink2n_bill=Label(windows1,text="Pomegranate Juice",font=("Verdana",9),relief="sunken")
        drink2n_bill.place(x=20,y=420)
        drink2q_bill=Label(windows1,text="0",font=("Verdana",9))
        drink2q_bill.place(x=210,y=420)
        drink2q_bill.config(text = drink2_quantity)
        drink2t_bill=Label(windows1,text="0",font=("Verdana",9))
        drink2t_bill.place(x=350,y=420)
        drink2t_bill.config(text = drink2_total)

        drink3n_bill=Label(windows1,text="Orange Juice",font=("Verdana",9),relief="sunken")
        drink3n_bill.place(x=20,y=470)
        drink3q_bill=Label(windows1,text="0",font=("Verdana",9))
        drink3q_bill.place(x=210,y=470)
        drink3q_bill.config(text = drink3_quantity)
        drink3t_bill=Label(windows1,text="0",font=("Verdana",9))
        drink3t_bill.place(x=350,y=470)
        drink3t_bill.config(text = drink3_total)

        icecreamn_bill=Label(windows1,text="Ice-Cream",font=("Verdana",9),relief="sunken")
        icecreamn_bill.place(x=20,y=520)
        icecreamq_bill=Label(windows1,text="0",font=("Verdana",9))
        icecreamq_bill.place(x=210,y=520)
        icecreamq_bill.config(text = icecream_quantity)
        icecreamt_bill=Label(windows1,text="0",font=("Verdana",9))
        icecreamt_bill.place(x=350,y=520)
        icecreamt_bill.config(text = icecream_total)


        donutn_bill=Label(windows1,text="Ice-Donut",font=("Verdana",9),relief="sunken")
        donutn_bill.place(x=20,y=570)
        donutq_bill=Label(windows1,text="0",font=("Verdana",9))
        donutq_bill.place(x=210,y=570)
        donutq_bill.config(text = donut_quantity)
        donutt_bill=Label(windows1,text="0",font=("Verdana",9))
        donutt_bill.place(x=350,y=570)
        donutt_bill.config(text = icecream_total)

        null1=Label(windows1,text="---------------------------------------------------------------------------------",font=("Verdana",9))
        null1.place(x=20,y=600)

        totaln_bill=Label(windows1,text="Total",font=("Verdana",9),relief="raised")
        totaln_bill.place(x=20,y=630)
        totalq_bill=Label(windows1,text="0",font=("Verdana",9))
        totalq_bill.place(x=210,y=630)
        totalq_bill.config(text = total_quantity)
        totalp_bill=Label(windows1,text="0",font=("Verdana",9))
        totalp_bill.place(x=350,y=630)
        totalp_bill.config(text =total)

     
#---------------------------------------------------------------#################################################------------------------------
#---------------------------------------------------------------#################################################------------------------------

pizza_btn1 =Button(root,text="Fully Loaded Pizza",command = pizza1_click,width=200,height=200,relief='raised',borderwidth=2,bg=color)
pizza1 = Image.open('pizza_btn1.jpg')
pizza1_img = ImageTk.PhotoImage(pizza1) 
pizza_btn1.config(image=pizza1_img)
pizza_btn1.place(x=40,y=125)

pizza1_name=Label(text="Fully Loaded Pizza",font=("bold",16),background='alice blue',relief='raised',borderwidth=2,fg="black")
pizza1_name.place(x=250,y=125)
pizza1_name=Label(text="price:Rs 500",font=("bold",15),background='alice blue',relief='raised',borderwidth=2,fg="black")
pizza1_name.place(x=250,y=168)
pizza1_name=Label(text="quantity",font=("bold",19),background='alice blue',width=10,relief='raised',borderwidth=2,fg="black")
pizza1_name.place(x=260,y=215)
pizza1_label=Label(text="0",font=("bold",25),relief='raised',width=8,borderwidth=2,fg="black")
pizza1_label.place(x=260,y=253)
# <----------
pizza_btn2 =Button(root,text="Paneer Pizza",command = pizza2_click,width=200,height=200,relief='raised',borderwidth=2,bg=color)
pizza2 = Image.open('pizza_btn2.jpg')
pizza2_img = ImageTk.PhotoImage(pizza2) 
pizza_btn2.config(image=pizza2_img)
pizza_btn2.place(x=40,y=345)

pizza2_name=Label(text="Paneer Pizza",font=("bold",20),background='alice blue',relief='raised',borderwidth=2,fg="black")
pizza2_name.place(x=250,y=345)
pizza2_name=Label(text="price:Rs 400",font=("bold",15),background='alice blue',relief='raised',borderwidth=2,fg="black")
pizza2_name.place(x=250,y=390)
pizza2_name=Label(text="quantity",font=("bold",19),background='alice blue',width=10,relief='raised',borderwidth=2,fg="black")
pizza2_name.place(x=260,y=440)
pizza2_label=Label(text="0",font=("bold",25),relief='raised',width=8,borderwidth=2,fg="black")
pizza2_label.place(x=260,y=480)
# <----------
pizza_btn3 =Button(root,text=color,command = pizza3_click,width=200,height=195,relief='raised',borderwidth=2,bg=color)
pizza3 = Image.open('pizza_btn3.jpg')
pizza3_img = ImageTk.PhotoImage(pizza3) 
pizza_btn3.config(image=pizza3_img)
pizza_btn3.place(x=40,y=572)

pizza3_name=Label(text="Pepperoni Pizza",font=("bold",20),background='alice blue',relief='raised',borderwidth=2,fg="black")
pizza3_name.place(x=250,y=572)
pizza3_name=Label(text="price:Rs 350",font=("bold",15),background='alice blue',relief='raised',borderwidth=2,fg="black")
pizza3_name.place(x=250,y=615)
pizza3_name=Label(text="quantity",font=("bold",19),background='alice blue',width=10,relief='raised',borderwidth=2,fg="black")
pizza3_name.place(x=260,y=665)
pizza3_label=Label(text="0",font=("bold",25),relief='raised',width=8,borderwidth=2,fg="black")
pizza3_label.place(x=260,y=703)
# <----------

drink_btn1=Button(root,command=drink1_click,text="oreo milkshake",font=("bold",20),background="alice blue",relief='raised',borderwidth=2,fg="black")
drink1=Image.open('drink_btn1.jpg')
drink1_img=ImageTk.PhotoImage(drink1)
drink_btn1.config(image=drink1_img)
drink_btn1.place(x=500,y=125)

drink1_name=Label(text="oreo milkshake",font=("bold",20),background='alice blue',relief='raised',borderwidth=2,fg="black")
drink1_name.place(x=712,y=125)
drink1_name=Label(text="price:Rs 100",font=("bold",15),background='alice blue',relief='raised',borderwidth=2,fg="black")
drink1_name.place(x=712,y=168)
drink1_name=Label(text="quantity",font=("bold",19),background='alice blue',width=10,relief='raised',borderwidth=2,fg="black")
drink1_name.place(x=720,y=215)
drink1_label=Label(text="0",font=("bold",25),relief='raised',width=8,borderwidth=2,fg="black")
drink1_label.place(x=720,y=253)

# <----------

drink_btn2=Button(root,command=drink2_click,text="juice",font=("bold",20),background="alice blue",relief='raised',borderwidth=2,fg="black")
drink2=Image.open('drink_btn2.jpg')
drink2_img=ImageTk.PhotoImage(drink2)
drink_btn2.config(image=drink2_img)
drink_btn2.place(x=500,y=345)

drink2_name=Label(text="Pomegranate juice",font=("bold",18),background='alice blue',relief='raised',borderwidth=2,fg="black")
drink2_name.place(x=712,y=345)
drink2_name=Label(text="price:Rs 90",font=("bold",15),background='alice blue',relief='raised',borderwidth=2,fg="black")
drink2_name.place(x=712,y=390)
drink2_name=Label(text="quantity",font=("bold",19),background='alice blue',width=10,relief='raised',borderwidth=2,fg="black")
drink2_name.place(x=720,y=440)
drink2_label=Label(text="0",font=("bold",25),relief='raised',width=8,borderwidth=2,fg="black")
drink2_label.place(x=720,y=480)

# <----------

drink_btn3=Button(root,command=drink3_click,text="juice",font=("bold",20),background="alice blue",relief='raised',borderwidth=2,fg="black")
drink3=Image.open('drink_btn3.jpg')
drink3_img=ImageTk.PhotoImage(drink3)
drink_btn3.config(image=drink3_img)
drink_btn3.place(x=500,y=572)

drink3_name=Label(text="orange juice",font=("bold",20),background='alice blue',relief='raised',borderwidth=2,fg="black")
drink3_name.place(x=712,y=572)
drink3_name=Label(text="price:Rs 80",font=("bold",15),background='alice blue',relief='raised',borderwidth=2,fg="black")
drink3_name.place(x=712,y=615)
drink3_name=Label(text="quantity",font=("bold",19),background='alice blue',width=10,relief='raised',borderwidth=2,fg="black")
drink3_name.place(x=720,y=665)
drink3_label=Label(text="0",font=("bold",25),relief='raised',width=8,borderwidth=2,fg="black")
drink3_label.place(x=720,y=703)


# <----------

icecream_btn=Button(root,command=icecream_click,text="juice",font=("bold",20),background="alice blue",relief='raised',borderwidth=2,fg="black")
icecream=Image.open('icecream_btn.jpg')
icecream_img=ImageTk.PhotoImage(icecream)
icecream_btn.config(image=icecream_img)
icecream_btn.place(x=970,y=125)

icecream_name=Label(text="Ice-Cream",font=("bold",20),background='alice blue',relief='raised',borderwidth=2,fg="black")
icecream_name.place(x=1180,y=125)
icecream_name=Label(text="price:Rs 100",font=("bold",15),background='alice blue',relief='raised',borderwidth=2,fg="black")
icecream_name.place(x=1180,y=168)
icecream_name=Label(text="quantity",font=("bold",19),background='alice blue',width=10,relief='raised',borderwidth=2,fg="black")
icecream_name.place(x=1190,y=215)
icecream_label=Label(text="0",font=("bold",25),relief='raised',width=8,borderwidth=2,fg="black")
icecream_label.place(x=1190,y=253)

# <----------

donut_btn=Button(root,command=donut_click,text="juice",font=("bold",20),background="alice blue",relief='raised',borderwidth=2,fg="black")
donut=Image.open('donut_btn.jpg')
donut_img=ImageTk.PhotoImage(donut)
donut_btn.config(image=donut_img)
donut_btn.place(x=970,y=345)

donut_name=Label(text="Ice-donut",font=("bold",20),background='alice blue',relief='raised',borderwidth=2,fg="black")
donut_name.place(x=1180,y=345)
donut_name=Label(text="price:Rs 150",font=("bold",15),background='alice blue',relief='raised',borderwidth=2,fg="black")
donut_name.place(x=1180,y=390)
donut_name=Label(text="quantity",font=("bold",19),background='alice blue',width=10,relief='raised',borderwidth=2,fg="black")
donut_name.place(x=1190,y=440)
donut_label=Label(text="0",font=("bold",25),relief='raised',width=8,borderwidth=2,fg="black")
donut_label.place(x=1190,y=480)

# <--------------------------------------------------------------
bottom = Frame(root,bg="white",width =385,height=200,relief='raised',borderwidth=2)
bottom.place(x=970,y=572)
total_btn=Button(bottom,text="Total Price:",command=total_click,font=("bold",22),background="alice blue",width=9,relief='raised',borderwidth=2,fg="black")
total_btn.place(x=0,y=0)
totalprice_label=Label(bottom,text="0",font=("bold",20),background="alice blue",width=9,relief='raised',borderwidth=2,fg="black")
totalprice_label.place(x=220,y=0)
Rsprice_label=Label(bottom,text="Rs",font=("bold",20),background="alice blue",width=2,relief='raised',borderwidth=2,fg="black")
Rsprice_label.place(x=210,y=0)
order_btn=Button(bottom,text="Order",command=order_click,font=("bold",30),background="alice blue",relief='raised',borderwidth=2,fg="black")
order_btn.place(x=120,y=100)

#--------------------------------------------------------------
root.mainloop()
