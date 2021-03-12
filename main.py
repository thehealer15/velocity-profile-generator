import tkinter as tk
import datetime
import time
import csv
import pymsgbox as pmb

# defining global variables
CSV_FILE_NAME =""
VELOCITY=0
ACCELARATION=0 # will be input
RETARDATION =0 # will be input
MAX_SPEED= 60 # m/s i.e 216 km/hr
TIME_OF_UPDATE=1
KMPH=" Km/ hr"
START_TIME=time.time()
PROG_TIME=0

# functions starts here
def Acelarate(event):
    """
        When key is pressed this function will increase Speed
        If MAX Speed is reached speed will be same
        else VELOCITY is increased by Accelaration
    """
    global VELOCITY
    
    if ( VELOCITY + ACCELARATION > MAX_SPEED):
        pmb.alert("MAX Speed is reached")
    else:
        VELOCITY = VELOCITY+ ACCELARATION
    global PROG_TIME,TIME_OF_UPDATE
    if(PROG_TIME%TIME_OF_UPDATE==0):
        update_CSV()
    
    label.config(text=str(round(VELOCITY*18/5,2))+KMPH)



def brake_Applied(event):
    """
    If velocity == 0, alert and keep velovity 0 no reductions  
    """ 
    global VELOCITY
    if(VELOCITY-RETARDATION<0):
        pmb.alert("Speed is 0")
    else:
        VELOCITY=VELOCITY-RETARDATION
    global PROG_TIME, TIME_OF_UPDATE
    if(PROG_TIME%TIME_OF_UPDATE==0):
        update_CSV()
    label.config(text=str(round(VELOCITY*18/5,2))+KMPH)

def create_file():
    """
    Function to create and initialize file i.e. csv file
    initilise =  writing fields
    """
    global CSV_FILE_NAME
    CSV_FILE_NAME=pmb.prompt("Enter CSV File Name: ")
    CSV_FILE_NAME+=".csv"
    fields = ['Time ','Veclocity (km/s)']
    with open(CSV_FILE_NAME,'w') as csvfile:
        csvwr=csv.writer(csvfile)
        csvwr.writerow(fields) 
        
    
        
def getInputs():
    global  VELOCITY, ACCELARATION, RETARDATION ,MAX_SPEED , TIME_OF_UPDATE
    temp=str(pmb.prompt("Please Enter in sequence mentioned\nAccelaration (m/s) -> Time of Update(s) -> Decleration(m/s) -> Max Speed(km/hr)")).split(" ")
    ACCELARATION, TIME_OF_UPDATE, RETARDATION, MAX_SPEED = temp
    ACCELARATION=float(ACCELARATION)
    RETARDATION=float(RETARDATION)
    MAX_SPEED=float(MAX_SPEED)
    TIME_OF_UPDATE=float(TIME_OF_UPDATE)
    MAX_SPEED = MAX_SPEED*5/18 # to convert into m/s 

def update_CSV():
    global CSV_FILE_NAME
    with open(CSV_FILE_NAME,'a') as csvfile:
        csvwr=csv.writer(csvfile)
        csvwr.writerow([str(datetime.datetime.now())[11:19],round(VELOCITY*18/5,2)])


if __name__ == "__main__":
    

    root= tk.Tk()
    root.geometry("800x450")
    root.title("Simult-OR")
    getInputs()
    create_file()
    # global START_TIME
    PROG_TIME=time.time()-START_TIME

    
    label= tk.Label(root,text=0,font=("Arial",25))
    label.pack(side='top')
    tk.Label(root,text="Accelaration is: "+str(ACCELARATION)+" m/s ").pack()
    tk.Label(root,text="Retardation is : "+str(RETARDATION)+" m/s ").pack()
    tk.Label(root,text="Maximum Speed is: "+str(MAX_SPEED*18/5)+" Km/Hr ").pack()
    frame= tk.Frame(root,height=50,width=50)
    bt= tk.Button(frame,text="submit")
    bt.pack()

    # if(PROG_TIME%TIME_OF_UPDATE==0):
    #     update_CSV()
    # else:
    #     print("A")

    root.bind("<Up>",Acelarate)
    root.bind("<Down>",brake_Applied)
    frame.pack()


    root.mainloop()
