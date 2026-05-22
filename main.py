import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")
#the grid and size of my page
app = customtkinter.CTk()
app.geometry('910x900')
app.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1, uniform='x')
app.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform='x')
app.title('Waffle cafe')

# #navbar
def Home():
    global home_page_frame
    global menu_page_frame
    menu_page_frame.place_forget()
    home_page_frame.place(x=1, y=1, relwidth=1, relheight=1)
def menu_bt():
     global home_page_frame
     global menu_page_frame
     home_page_frame.place_forget()
     menu_page_frame.place(x=1, y=1, relwidth=1, relheight=1)

#home page frame
home_page_frame = customtkinter.CTkScrollableFrame(app)
home_page_frame.config(bg="yellow")
#menu page frame
menu_page_frame = customtkinter.CTkScrollableFrame(app)
menu_page_frame.config(bg="blue")

#navbar buttons
home_button = customtkinter.CTkButton(app, text ="Home", command= Home).grid(row=0,column=5)
menu_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)



#slide
image1 = customtkinter.CTkImage(light_image=Image.open("image.png"), size=(910,500))
image1_label = customtkinter.CTkLabel(home_page_frame, text="", image=image1 )
image1_label.grid(row=1, column=1)

#menu

#classic waffle
classic_waffle_img = customtkinter.CTkImage(menu_page_frame, light_image=Image.open("classic waffle.png"), size=(300,300))
classic_waffle_lable = customtkinter.CTkLabel(menu_page_frame, text="", image=classic_waffle_img )
classic_waffle_lable.grid(row=2, column=1)
app.mainloop()





































