import time
import customtkinter
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
app=customtkinter.CTk()
app.title("My Clock")
app.geometry("450x300")


hello_label=customtkinter.CTkLabel(master=app,text="Hello",font=("Arial",20),fg_color="blue",text_color="white")
hello_label.pack(padx=20,pady=20)

time_label=customtkinter.CTkLabel(master=app,text="",font=("Helvetica",50),text_color="white")
time_label.pack(padx=20,pady=50,anchor="center")
def update_time():
    current_time=time.strftime("%I:%M:%S %p")
    time_label.configure(text=current_time)
    app.after(1000,update_time)
    
    

update_time()
app.mainloop()