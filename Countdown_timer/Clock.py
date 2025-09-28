import time
import pygame
import customtkinter
import threading

pygame.mixer.init()
alarm_time=""
alarm_status=False

def update_clock():
    global alarm_status
    global alarm_time
    current_time=time.strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    app.after(1000,update_clock)
        
def check_alarm():
    global alarm_status
    while True:
        if alarm_status:
            current_time=time.strftime("%H:%M")

            if current_time==alarm_time:
                print("ALARM! Wake Up!")
                pygame.mixer.music.load(r"C:\Users\DELL\Downloads\mixkit-classic-alarm-995.wav")
                pygame.mixer.music.play(loops=-1)
                alarm_status=False
        time.sleep(1) 

def stop_alarm_sound():
    pygame.mixer.music.stop()
    print("Alarm stopped")


def set_alarm_action():
    global alarm_status
    alarm_status=True
    selected_hour=hour_menu.get()
    selected_min=minute_menu.get()
    print(f"Alarm set for {selected_hour}:{selected_min}")
    global alarm_time
    alarm_time=f"{selected_hour}:{selected_min}"  



customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
app=customtkinter.CTk()
app.title("My first clock App")
app.geometry("550x300")

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
set_alarm.pack(side="left")

stop_alarm=customtkinter.CTkButton(master=control_frame,corner_radius=15,text="Stop",command=stop_alarm_sound)
stop_alarm.pack(side="left")

alarm_thread=threading.Thread(target=check_alarm,daemon=True)
alarm_thread.start()

update_clock()

app.mainloop()