# (Make sure you have Pillow installed: pip install Pillow)

import customtkinter
from PIL import Image

# ==========================================================
#  MAIN APP SETUP
# ==========================================================
app = customtkinter.CTk()
app.title("Pomodoro Timer")
app.geometry("450x300")
customtkinter.set_appearance_mode("Dark") # Start in Dark mode

# --- Configure the main grid layout ---
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# ==========================================================
#  THEME CHANGE LOGIC
# ==========================================================
# This function is now very simple. It only needs to change the
# global appearance mode. CustomTkinter handles swapping the icon.
def change_theme():
    current_mode = customtkinter.get_appearance_mode()
    if current_mode == "Dark":
        customtkinter.set_appearance_mode("Light")
    else:
        customtkinter.set_appearance_mode("Dark")

# ==========================================================
#  WIDGET CREATION
# ==========================================================

# --- Main Widgets using .grid() ---
time_label = customtkinter.CTkLabel(master=app, text="25:00", font=("Helvetica", 80))
time_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

start_button = customtkinter.CTkButton(master=app, text="Start", font=("Helvetica", 24))
start_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

reset_button = customtkinter.CTkButton(master=app, text="Reset", font=("Helvetica", 24))
reset_button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")


# --- Theme Icon Button using .place() ---
try:
    # IMPORTANT: Load both your sun and moon icons here
    theme_icon = customtkinter.CTkImage(
        light_image=Image.open("sun.png"),   # Image for Light Mode
        dark_image=Image.open("moon.png"),   # Image for Dark Mode
        size=(30, 30)
    )

    theme_button = customtkinter.CTkButton(
        app,
        text="",
        image=theme_icon,
        width=40,
        height=40,
        fg_color="transparent",
        hover_color="#4A4A4A",
        command=change_theme
    )
    theme_button.place(relx=1.0, rely=0.0, x=-10, y=10, anchor="ne")

except FileNotFoundError:
    print("Warning: 'sun.png' or 'moon.png' not found. Theme button not created.")


# ==========================================================
#  START THE APP
# ==========================================================
app.mainloop()