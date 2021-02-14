''' Notice:this program contain functions in function.
I added two line gap before every comment(when required.) in this Code
to make the code  easy to read...Thanks.'''


#A app made for shop keepers


# i edited pywhatkit module exception and changed it's folder name to simkit
# simkit floder provided on github..
import simkit
from tkinter import *
from datetime import datetime


#creating a function for startup of the GUI app and exit root of the App
def main_startup():
    startroot.destroy()
#you can see on line 82 that what is startroot


#exit root function to exit from the app
    def exit():


#         this function will create a window when you will click on exit button in main window
        exitroot=Tk()
        exitroot.configure(bg='cyan')
        exitroot.title('EXIT')
        exitroot.geometry('70x70')
        exitroot.minsize(70,70)
        exitroot.maxsize(70,70)
        text=Label(exitroot,text='Are you sure.',relief='sunken',fg='green').grid() 


#main window function
        def destroy():
            root.destroy()
            exitroot.destroy()
             


#exit root destroy function
        def exitrootdestroy():
            exitroot.destroy()
             
        
        
        #adding button in exitroot window
        button1=Button(exitroot,text='Yes',bg='red',relief='ridge',command=destroy).grid(row=1,column=2)
        button2=Button(exitroot,text='No',bg='green',relief='ridge',command=exitrootdestroy).grid(row=2,column=2)
        exitroot.mainloop()


#     saving the detail
    def save_detail():
        file1=open('Shopkeeper.txt','a')
        file1.write(customername.get())
        file1.write(addressvar.get())
        file1.write(phonenumber.get())
        file1.write(Amountnumber.get())
        file1.close()


#Mainwidow code is here
    root=Tk()
    root.configure(bg='cyan')
    root.title('Shopbingoo')
    root.geometry('330x190')
    root.minsize(330,190)
    root.maxsize(330,190)#adding text in mainwindow
    banner=Label(text='Shopbingoo',relief='raised',font='cosmicsan 20 bold italic',bg='green',fg='red')
    banner.grid(row=0,column=0)
    customer=Label(text='Customer         :',relief='sunken',font='cosmicsan 10 bold italic',bg='blue',padx=20).grid(row=1,column=0)
    address=Label(text='address            :',relief='sunken',font='cosmicsan 10 bold italic',bg='blue',padx=20).grid(row=2,column=0)
    phonenum=Label(text='phone number :',relief='sunken',font='cosmicsan 10 bold italic',bg='blue',padx=20).grid(row=3,column=0)
    amount=Label(text='Amount            :',relief='sunken',font='cosmicsan 10 bold italic',bg='blue',padx=20).grid(row=4,column=0)
    created=Label(text='<created by Ambrish>',relief='groove',font='cosmicsan 10 underline bold italic',bg='yellow',padx=20).grid(row=5,column=0)


#creating a string variable to take input
    customername=StringVar()
    addressvar=StringVar()
    phonenumber=StringVar()
    Amountnumber=StringVar()


#adding input area to enter detail 
    Entry(textvariable=customername,relief='groove').grid(row=1,column=1)
    Entry(textvariable=addressvar).grid(row=2,column=1)
    Entry(textvariable=phonenumber).grid(row=3,column=1)
    Entry(textvariable=Amountnumber).grid(row=4,column=1)


#     taking the detail written by the user
    customername.get()
    addressvar.get()
    phonenumber.get()
    Amountnumber.get()
    senddew='Dear coustmer you Amount dew will be send to within few minutes '
    amountdew=senddew
    
    
    #setting time to send message
    now=datetime.now()
    qhour=now.strftime('%H')
    qminute=now.strftime('%M')
    hour=int(qhour)
    minute=int(qminute)
    lastminute=minute+2
    rupeeminute=minute+4
    
    
    #fuction to send message on whatsapp
    def sendmessageonwhatsapp():
        simkit.sendwhatmsg(phonenumber.get(),amountdew,hour,lastminute)
        simkit.sendwhatmsg(phonenumber.get(),Amountnumber.get(),hour,rupeeminute)


#     adding button and checkbutton in main window
    Button(text='Save',command=save_detail,bg='green2',relief='ridge').grid(row=6,column=1)
    Button(text='exit',bg='red',command=exit,relief='ridge').grid(row=6,column=0)
    Checkbutton(text='send it on whatsapp',fg='purple',bg='yellow',relief='ridge',command=sendmessageonwhatsapp).grid(row=5,column=1)
    root.mainloop()
    
    
# startup window
startroot=Tk()
startroot.configure(bg='cyan')
startroot.title('Shopbingoo')
startroot.geometry('313x70')
Button(text='Start',relief='ridge',bg='purple',command=main_startup).grid()
Label(text='NOTE: Use space button after typing every detail',bg='black',fg='white',relief='groove',font='cosmicsan 10 underline bold').grid(row=2,column=0)
Label(text='NOTE: Phone number must include country code ',bg='black',fg='white',relief='sunken',font='cosmicsan 10 underline bold').grid(row=3,column=0)
startroot.mainloop()