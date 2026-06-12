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


#navbar buttons
home_button = customtkinter.CTkButton(app, text ="Home", command= Home).grid(row=0,column=5)
menu_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)



#slide
image1 = customtkinter.CTkImage(light_image=Image.open("image.png"), size=(910,500))
image1_label = customtkinter.CTkLabel(home_page_frame, text="", image=image1 )
image1_label.grid(row=1, column=1)
#menu

#classic waffle
def classic_waffle():
    global classic_waffle_label
    classic_waffle_label.grid(row=3, column=3)
classic_waffle_label = customtkinter.CTkLabel(menu_page_frame, text="Classic waffle")
image2 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image2_button = customtkinter.CTkButton(menu_page_frame, text="Classic waffle", image=image2, command= classic_waffle )
image2_button.grid(row=3, column=1)

#bubble waffle
def bubble_waffle():
    global bubble_waffle_label
    bubble_waffle_label.grid(row=3, column=4)
bubble_waffle_label = customtkinter.CTkLabel(menu_page_frame, text="bubble waffle")
image3 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image3_button = customtkinter.CTkButton(menu_page_frame, text="bubble waffle", image=image3, command= bubble_waffle )
image3_button.grid(row=3, column=2)

#waffle_fries
def waffle_fries():
    global waffle_fries_label
    waffle_fries_label.grid(row=3, column=5)
waffle_fries_label = customtkinter.CTkLabel(menu_page_frame, text="waffle fries")
image4 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image4_button = customtkinter.CTkButton(menu_page_frame, text="waffle fries", image=image3, command= waffle_fries)
image4_button.grid(row=3, column=3)

#waffle bites
def waffle_bites():
    global waffle_bites_label
    waffle_bites_label.grid(row=3, column=4)
waffle_bites_label = customtkinter.CTkLabel(menu_page_frame, text="waffle_bites")
image5 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image5_button = customtkinter.CTkButton(menu_page_frame, text="waffle_bites", image=image2, command= waffle_bites)
image5_button.grid(row=4, column=1)

#waffle cake
def waffle_cake():
    global waffle_cake_label
    waffle_cake_label.grid(row=4, column=5)
waffle_cake_label = customtkinter.CTkLabel(menu_page_frame, text="Classic waffle")
image6 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image6_button = customtkinter.CTkButton(menu_page_frame, text="waffle_cake", image=image2, command= classic_waffle )
image6_button.grid(row=4, column=2)

#Coffee
def coffee():
    global coffee_label
    coffee_label.grid(row=4, column=4)
coffee_label = customtkinter.CTkLabel(menu_page_frame, text="Coffee")
image7 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image7_button = customtkinter.CTkButton(menu_page_frame, text="coffee", image=image2, command= coffee )
image7_button.grid(row=5, column=1)


#iced lattes
def iced_lattes():
    global iced_lattes_label
    iced_lattes_label.grid(row=3, column=3)
iced_lattes_label = customtkinter.CTkLabel(menu_page_frame, text="iced lattes")
image8 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image8_button = customtkinter.CTkButton(menu_page_frame, text="iced lattes", image=image2, command= iced_lattes )
image8_button.grid(row=5, column=2)

#Choclate drinks
def choclate_drink():
    global choclate_drink_label
    choclate_drink_label.grid(row=3, column=3)
choclate_drink_label = customtkinter.CTkLabel(menu_page_frame, text="Choclate drinks")
image9 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image9_button = customtkinter.CTkButton(menu_page_frame, text="Choclate drink", image=image2, command= choclate_drink )
image9_button.grid(row=5, column=3)

#smoothies
def smoothies():
    global smoothies_label
    smoothies_label.grid(row=3, column=3)
smoothies_label = customtkinter.CTkLabel(menu_page_frame, text="smoothies")
image10 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image10_button = customtkinter.CTkButton(menu_page_frame, text="smoothies", image=image2, command= smoothies )
image10_button.grid(row=6, column=1)

#slushies
def slushies():
    global slushies_label
    slushies_label.grid(row=3, column=3)
slushies_label = customtkinter.CTkLabel(menu_page_frame, text="slushies")
image11 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image11_button = customtkinter.CTkButton(menu_page_frame, text="slushies", image=image2, command= slushies )
image11_button.grid(row=6, column=2)


app.mainloop()




























