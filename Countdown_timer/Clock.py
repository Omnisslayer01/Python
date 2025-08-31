import time
import pygame
import msvcrt
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
app=customtkinter.CTk()
app.title("My first clock App")
app.geometry("450x300")

frame=customtkinter.CTkFrame(master=app,corner_radius=15,fg_color="#1E1E2E")
frame.pack(pady=20)

time_label=customtkinter.CTkLabel(master=frame,text="",font=("Helvetica",50),text_color="#00BFFF")
time_label.pack(pady=20,padx=20,anchor="center")
def update_clock():
    current_time=time.strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    app.after(1000,update_clock)

control_frame=customtkinter.CTkFrame(master=app)
control_frame.pack(pady=10)

hours=[f"{i:02}" for i in range(0,24)]
minutes=[f"{i:02}"for i in range(0,60)]

hour_menu=customtkinter.CTkComboBox(master=control_frame,values=hours)
hour_menu.pack(side="left", pady=10)
hour_menu.set("- -")

minute_menu=customtkinter.CTkComboBox(master=control_frame,values=minutes)
minute_menu.pack(side="left", pady=10)
minute_menu.set("- -")

set_alarm=customtkinter.CTkButton(master=control_frame,corner_radius=15,text="Set Alarm")
set_alarm.pack(side="bottom",pady=20)


update_clock()

app.mainloop()