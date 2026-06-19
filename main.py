import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image

price = 0

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")
#the grid and size of my page
app = customtkinter.CTk()
app.geometry('850x500')
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
home_page_frame.place(x=1, y=1, relwidth=1, relheight=1)
home_page_frame.config(bg="yellow")
#menu page frame
menu_page_frame = customtkinter.CTkScrollableFrame(app)


#navbar buttons
home_button = customtkinter.CTkButton(app, text ="Home", command= Home).grid(row=0,column=5)
menu_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)

coffee_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)
waffles_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)
cold_drinks_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)
hot_drinks_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)
lollies_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)
specials_button = customtkinter.CTkButton(app, text ="menu", command= menu_bt).grid(row=0, column=6)




#slide
image1 = customtkinter.CTkImage(light_image=Image.open("image.png"), size=(910,500))
image1_label = customtkinter.CTkLabel(home_page_frame, text="", image=image1 )
image1_label.grid(row=1, column=1)
#menu

#classic waffle
def classic_waffle():
    global price
    global classic_waffle_frame
    global menu_page_frame
    classic_waffle_frame.place(relx=0.5, rely=0.3, anchor="center")
    menu_page_frame.place_forget()
    price = +20.65
    print(price)

classic_waffle_frame = customtkinter.CTkScrollableFrame(app, width=650, border_width=2)
image2 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image2_button = customtkinter.CTkButton(menu_page_frame, image=image2, border_width= 1 ,command= classic_waffle )
image2_button.grid(row=3, column=1)
#bananas
banana_radio = customtkinter.StringVar()
banana = customtkinter.CTkRadioButton(classic_waffle_frame, text= "Banana", variable=banana_radio).grid(row=0, column=1, padx=20, pady=20, sticky="ew", columnspan=1)
no_banana = customtkinter.CTkRadioButton(classic_waffle_frame, text= "No Banana", variable=banana_radio).grid(row=0, column=2, padx=20, pady=20, sticky="e", columnspan=1)
#ice cream
icecream_radio = customtkinter.StringVar()
icecream = customtkinter.CTkRadioButton(classic_waffle_frame, text= "Ice cream", variable=icecream_radio).grid(row=1, column=1, padx=20, pady=20, columnspan=1)
no_icecream = customtkinter.CTkRadioButton(classic_waffle_frame, text= "No ice cream", variable=icecream_radio).grid(row=1, column=2, padx=20, pady=20, columnspan=1)
double_icecream = customtkinter.CTkRadioButton(classic_waffle_frame, text= "Double scoop", variable=icecream_radio).grid(row=1, column=3, padx=20, pady=20, columnspan=1)


def two_dollars():
    global price
    price = +2
    print(price)

Toppings_label = customtkinter.CTkLabel(classic_waffle_frame, text="Toppings").grid(row=0, column=0)
topping1 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Maple")
topping1.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping2 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Lotus Biscoff Sauce")
topping2.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping3 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Strawberry")
topping3.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping4 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Passion Fruit")
topping4.grid(row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping5 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Chocolate Sauce ")
topping5.grid(row=6, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping6 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Peanut Butter sauce")
topping6.grid(row=7, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping7= customtkinter.CTkCheckBox(classic_waffle_frame, text= "Fruit silk Sauce")
topping7.grid(row=8, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping8 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Citrus Peel topping")
topping8.grid(row=9, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping9 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Extra Ice Cream Scoop")
topping9.grid(row=10, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping10 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Lotus Biscoff Sauce")
topping10.grid(row=11, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping11 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Pistachio topping sauce")
topping11.grid(row=12, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping12 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Almond topping sauce")
topping12.grid(row=13, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping13 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Dulce de Leche Caramel")
topping13.grid(row=14, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping14 = customtkinter.CTkCheckBox(classic_waffle_frame, text= " hazelnut spread")
topping14.grid(row=15, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping15 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Extra Banana")
topping15.grid(row=16, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Fruit silk Sauce")
topping16.grid(row=17, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping17 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Peanut Butter sauce")
topping17.grid(row=18, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "Add Lotus Biscoff crumbles ")
topping16.grid(row=19, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "chopped up Whittaker's PEANUT SLAB ")
topping16.grid(row=20, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping8 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "chopped up Whittaker's Creamy Milk ")
topping8.grid(row=21, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping8 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "chopped up Whittaker's BERRY FOREST ")
topping8.grid(row=22, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping8 = customtkinter.CTkCheckBox(classic_waffle_frame, text= "chopped up Whittaker's Creamy Milk")
topping8.grid(row=23, column=0, padx=20, pady=20, sticky="ew", columnspan=2)






print(price)




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
image4_button.grid(row=4, column=1)

#waffle bites
def waffle_bites():
    global waffle_bites_label
    waffle_bites_label.grid(row=3, column=4)
waffle_bites_label = customtkinter.CTkLabel(menu_page_frame, text="waffle_bites")
image5 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image5_button = customtkinter.CTkButton(menu_page_frame, text="waffle_bites", image=image2, command= waffle_bites)
image5_button.grid(row=4, column=2)

#waffle cake
def waffle_cake():
    global waffle_cake_label
    waffle_cake_label.grid(row=4, column=5)
waffle_cake_label = customtkinter.CTkLabel(menu_page_frame, text="Classic waffle")
image6 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image6_button = customtkinter.CTkButton(menu_page_frame, text="waffle_cake", image=image2, command= classic_waffle )
image6_button.grid(row=5, column=1)

#Coffee
def coffee():
    global coffee_label
    coffee_label.grid(row=4, column=4)
coffee_label = customtkinter.CTkLabel(menu_page_frame, text="Coffee")
image7 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image7_button = customtkinter.CTkButton(menu_page_frame, text="coffee", image=image2, command= coffee )
image7_button.grid(row=5, column=2)


#iced lattes
def iced_lattes():
    global iced_lattes_label
    iced_lattes_label.grid(row=3, column=3)
iced_lattes_label = customtkinter.CTkLabel(menu_page_frame, text="iced lattes")
image8 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image8_button = customtkinter.CTkButton(menu_page_frame, text="iced lattes", image=image2, command= iced_lattes )
image8_button.grid(row=6, column=1)

#Choclate drinks
def choclate_drink():
    global choclate_drink_label
    choclate_drink_label.grid(row=3, column=3)
choclate_drink_label = customtkinter.CTkLabel(menu_page_frame, text="Choclate drinks")
image9 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image9_button = customtkinter.CTkButton(menu_page_frame, text="Choclate drink", image=image2, command= choclate_drink )
image9_button.grid(row=6, column=2)

#smoothies
def smoothies():
    global smoothies_label
    smoothies_label.grid(row=3, column=3)
smoothies_label = customtkinter.CTkLabel(menu_page_frame, text="smoothies")
image10 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image10_button = customtkinter.CTkButton(menu_page_frame, text="smoothies", image=image2, command= smoothies )
image10_button.grid(row=7, column=1)

#slushies
def slushies():
    global slushies_label
    slushies_label.grid(row=3, column=3)
slushies_label = customtkinter.CTkLabel(menu_page_frame, text="slushies")
image11 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image11_button = customtkinter.CTkButton(menu_page_frame, text="slushies", image=image2, command= slushies )
image11_button.grid(row=7, column=2)


app.mainloop()




























