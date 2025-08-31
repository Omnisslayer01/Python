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

update_clock()

app.mainloop()