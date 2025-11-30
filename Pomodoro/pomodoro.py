import customtkinter
import pygame
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
app=customtkinter.CTk()
app.title("Pomodoro Timer")
app.geometry("450x350")

is_light_mode=True

def change_theme():
    global is_light_mode
    if is_light_mode:
        customtkinter.set_appearance_mode("Light")
        is_light_mode=False
    else:
        customtkinter.set_appearance_mode("Dark")
        is_light_mode=True

theme=customtkinter.CTkButton(master=app,
        text="", # No text
        image=sun.png,
        width=35,
        height=35,
        fg_color="transparent",
        hover_color="#4A4A4A",
        command=change_theme) # Direct command, no lambda or cooldown needed
theme.place(relx=1.0,rely=0.0,anchor="ne")

app.mainloop()