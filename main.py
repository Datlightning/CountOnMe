# import customtkinter
#
# customtkinter.set_appearance_mode("light")
# customtkinter.set_default_color_theme("dark-blue")
#
# root = customtkinter.CTk()
# root.geometry("500x350")
#
# def login():
#     print("Test")
#
#
# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20,padx=60, fill="both", expand=True)
#
# label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
# label.pack(pady=12, padx=10)
#
# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)
#
# entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show = "*")
# entry2.pack(pady=12, padx=10)
#
# button = customtkinter.CTkButton(frame, text="Login", command=login)
# button.pack(pady = 12, padx = 10)
#
# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
# checkbox.pack(pady=12, padx = 10)
#
# root.mainloop()
import customtkinter

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()