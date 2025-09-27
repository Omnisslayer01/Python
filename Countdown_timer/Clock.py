import time
import pygame
import msvcrt
import customtkinter
import sys
import threading


alarm_time=""
alarm_status=False

def update_clock():
    global alarm_status
    global alarm_time
    current_time=time.strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    app.after(1000,update_clock)
    list=alarm_time.split(":")
    print(list)
    if current_time.split(":")[0]==list[0]:
        if current_time.split(":")[1]==list[1]:
            alarm_status=True
            list=[]
            alarm_sound()
        

def alarm_sound():
    if alarm_status==True:
        pygame.mixer.init()
        alarm_sound=pygame.mixer.Sound(r"C:\Users\DELL\Downloads\mixkit-classic-alarm-995.wav")
        alarm_sound.play()    

def set_alarm_action():
    selected_hour=hour_menu.get()
    selected_min=minute_menu.get()
    print(f"Alarm set for {selected_hour}:{selected_min}")
    global alarm_time
    alarm_time=f"{selected_hour}:{selected_min}"  



customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
app=customtkinter.CTk()
app.title("My first clock App")
app.geometry("450x300")

frame=customtkinter.CTkFrame(master=app,corner_radius=15,fg_color="#1E1E2E")
frame.pack(pady=20)

time_label=customtkinter.CTkLabel(master=frame,text="",font=("Helvetica",50),text_color="#00BFFF")
time_label.pack(pady=20,padx=20,anchor="center")


control_frame=customtkinter.CTkFrame(master=app)
control_frame.pack(pady=10)

hours=[f"{i:02}" for i in range(0,24)]
minutes=[f"{i:02}"for i in range(0,60)]

hour_menu=customtkinter.CTkComboBox(master=control_frame,values=hours)
hour_menu.pack(side="left", pady=10)
hour_menu.set("--")

minute_menu=customtkinter.CTkComboBox(master=control_frame,values=minutes)
minute_menu.pack(side="left", pady=10)
minute_menu.set("--")

set_alarm=customtkinter.CTkButton(master=control_frame,corner_radius=15,text="Set Alarm",command=set_alarm_action)
set_alarm.pack(side="bottom",pady=20)


update_clock()

app.mainloop()