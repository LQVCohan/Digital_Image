# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:14:21 2023

@author: Cohan
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
from tkinter import *
import tkinter.simpledialog as tsd
from tkinter import filedialog
import cv2,os
import time

def TrainingImage():
    try: 
        
        os.system('cmd /k "python src/align_dataset_mtcnn.py  Dataset/FaceData/raw Dataset/FaceData/processed --image_size 160 --margin 32  --random_order --gpu_memory_fraction 0.25"')
        tk.messagebox.showinfo(title="Notice", message="Command excuted")
    except: 
        print("Couldn't excute !")
    return 0;

def TrackingImage():
    try: 
        os.system('cmd /k "python src/classifier.py TRAIN Dataset/FaceData/processed Models/20180402-114759.pb Models/facemodel.pkl --batch_size 1000"')
        tk.messagebox.showinfo(title="Notice", message="Command excuted")
    except: 
        print("Couldn't excute !")
    return 0;

def openfn():
    filename = filedialog.askopenfilename(title = "open")
    return filename

def TakeImages():
    localtime = time.asctime( time.localtime(time.time()) )
    times = localtime.replace(" ", "")
    times = times[6:]
    times = times.replace(":", "")
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                os.makedirs("./DataSet/FaceData/raw/" + name,exist_ok=True)
                cv2.imwrite("./DataSet/FaceData/raw/" + name + "/" + Id + times+ ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
  
def cameraTesting():
    try: 
        os.system('cmd /k "python src/face_rec_cam.py"')
        tk.messagebox.showinfo(title="Notice", message="Command excuted")
    except: 
        print("Couldn't excute !")
    return 0;
    
def open_img():
    Id = (txt.get())
    name = (txt2.get())
    
    localtime = time.asctime( time.localtime(time.time()) )
    times = localtime.replace(" ", "")
    times = times[6:]
    times = times.replace(":", "")
    if Id != '' and name != '':

        x = openfn()
        Id = (txt.get())
        name = (txt2.get())
        img = cv2.imread(x,cv2.IMREAD_COLOR)
        os.makedirs("./DataSet/FaceData/raw/" + name,exist_ok=True)
        path = "./Dataset/FaceData/raw/"+name+"/"+Id+"_"+times+".jpg" 
        message.configure(text=path)
        cv2.imwrite(path,img)
    else: 
        tk.messagebox.showinfo(title="Notice", message="Empty information")
    return 0


global times1

def open_vid():
    localtime = time.asctime( time.localtime(time.time()) )
    times1 = localtime.replace(" ", "")
    times1 = times1[6:]
    times1 = times1.replace(":", "")
    x = openfn()
    pathVid = x
    video = cv2.VideoCapture(pathVid)
    W = int(video.get(3))
    H = int(video.get(4))
    pathTesting = "./video/"+times1+".avi"
    out = cv2.VideoWriter(pathTesting,cv2.VideoWriter_fourcc('X','V','I','D'),60,(W,H))
    while video.isOpened():
        ret, frame = video.read()
        if ret == False:
            break
        cv2.imshow('frame', frame)
        out.write(frame)
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            break
    video.release()
    out.release()
    cv2.destroyAllWindows()
    message.configure(text=pathVid)
    return times1

def videoTesting():
    times1=open_vid()
    os.system('cmd /k "python src/face_rec.py --path video/'+times1+'.avi"')
    tk.messagebox.showinfo(title="Notice", message="Command excuted")
    return 0

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#262523')

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)




head2 = tk.Label(frame2, text="                       For New Registrations                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                       For Already Registered                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=173)


message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)





###################### BUTTONS ##################################
loadButton = tk.Button(frame2, text = "Upload Image", command=open_img, fg="white",bg="green",width=34,height=1,activebackground="white",font=('times', 11, ' bold '))
loadButton.place(x=90, y = 258)

clearButton = tk.Button(frame2, text="Clear", command="*",fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=335, y=86)
clearButton2 = tk.Button(frame2, text="Clear", command="*"  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=335, y=172)    
takeImg = tk.Button(frame2, text="Take Images", command=TakeImages ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="Save Profile", command=TrainingImage,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="Train All", command=TrackingImage ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=30,y=50)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)
takeImg = tk.Button(frame1, text="Camera Testing", command=cameraTesting ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame1, text="Video Testing", command=videoTesting,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=30, y=380)

##################### END ######################################


window.mainloop()

####################################################################################################
