from string import whitespace

import customtkinter
from tkinter import messagebox, Spinbox
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
    global classic_waffle_frame
    global bubble_waffle_frame
    global waffle_bites_frame
    global waffle_cake_frame
    global waffle_fries_frame
    global iced_choclate_frame
    iced_choclate_frame.place_forget()
    classic_waffle_frame.place_forget()
    bubble_waffle_frame.place_forget()
    waffle_bites_frame.place_forget()
    waffle_cake_frame.place_forget()
    waffle_fries_frame.place_forget()
    home_page_frame.place(x=1, y=1, relwidth=1, relheight=1)
    menu_page_frame.place_forget()
def menu_bt():
     global home_page_frame
     global menu_page_frame
     global classic_waffle_frame
     global bubble_waffle_frame
     global waffle_bites_frame
     global waffle_cake_frame
     global waffle_fries_frame
     global iced_choclate_frame
     iced_choclate_frame.place_forget()
     classic_waffle_frame.place_forget()
     bubble_waffle_frame.place_forget()
     waffle_bites_frame.place_forget()
     waffle_cake_frame.place_forget()
     waffle_fries_frame.place_forget()
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

# cold_drinks_lable = customtkinter.CTkLabel(menu_page_frame, text ="cold_drinks").grid(row=0, column=6)
# lollies_lable = customtkinter.CTkLabel(menu_page_frame, text ="lollies").grid(row=0, column=6)
# specials_lable = customtkinter.CTkLabel(menu_page_frame, text ="specials").grid(row=0, column=6)




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

waffles_lable = customtkinter.CTkLabel(menu_page_frame, text ="waffles").grid(row=0, column=2)
classic_waffle_frame = customtkinter.CTkScrollableFrame(app, width=650, border_width=2)
image2 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image2_button = customtkinter.CTkButton(menu_page_frame, image=image2, border_width= 1, text="",fg_color= "white",hover_color="lightgray",command= classic_waffle )
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
confirm_classic = customtkinter.CTkButton(classic_waffle_frame, text= "confirm").grid(row=5, column=3, padx=20, pady=20, columnspan=1)
# number of items
number_of_items_label = customtkinter.CTkLabel(classic_waffle_frame, text= "Number of items" )
number_of_items_label.grid(column=2, row=3, columnspan=3)
number_of_items = Spinbox(classic_waffle_frame, from_=1, to=1000000000,font=("Arial", 14), width=10)
number_of_items.grid(column=2, row=4, columnspan=3)
def two_dollars():
    global price
    price = +2
    print(price)
#bubble waffle
def bubble_waffle():
    global price
    global bubble_waffle_frame
    global menu_page_frame
    bubble_waffle_frame.place(relx=0.5, rely=0.3, anchor="center")
    menu_page_frame.place_forget()
    price = +20.65
    print(price)

bubble_waffle_frame = customtkinter.CTkScrollableFrame(app, width=750, border_width=2)
image3 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image3_button = customtkinter.CTkButton(menu_page_frame, text="",fg_color= "white",hover_color="lightgray", image=image3, command= bubble_waffle )
image3_button.grid(row=3, column=2)
#bananas
banana_radio = customtkinter.StringVar()
banana = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "Banana", variable=banana_radio).grid(row=0, column=1, padx=20, pady=20, sticky="ew", columnspan=1)
no_banana = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "No Banana", variable=banana_radio).grid(row=0, column=2, padx=20, pady=20, sticky="e", columnspan=1)
#ice cream
icecream_radio = customtkinter.StringVar()
icecream = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "Ice cream", variable=icecream_radio).grid(row=1, column=1, padx=20, pady=20, columnspan=1)
no_icecream2 = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "No ice cream", variable=icecream_radio).grid(row=1, column=2, padx=20, pady=20, columnspan=1)
double_icecream = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "Double scoop", variable=icecream_radio).grid(row=1, column=3, padx=20, pady=20, columnspan=1)
confirm_classic = customtkinter.CTkButton(bubble_waffle_frame, text= "confirm").grid(row=5, column=3, padx=20, pady=20, columnspan=1)
#type
type_radio = customtkinter.StringVar()
plate = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "Bubble waffle on a plate ", variable=type_radio).grid(row=2, column=2, padx=20, pady=20, columnspan=1)
cone = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "Bubble waffle cone", variable=type_radio).grid(row=2, column=3, padx=20, pady=20, columnspan=1)
# number of items
number_of_items_label = customtkinter.CTkLabel(bubble_waffle_frame, text= "Number of items" )
number_of_items_label.grid(column=2, row=3, columnspan=3)
number_of_items = Spinbox(bubble_waffle_frame, from_=1, to=1000000000,font=("Arial", 14), width=10)
number_of_items.grid(column=2, row=4, columnspan=3)
# waffle fries
def waffle_fries():
    global price
    global waffle_fries
    global menu_page_frame
    waffle_fries_frame.place(relx=0.5, rely=0.3, anchor="center")
    menu_page_frame.place_forget()
    price = +20.65
    print(price)


waffle_fries_frame = customtkinter.CTkScrollableFrame(app, width=650, border_width=2)
image2 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image2_button = customtkinter.CTkButton(menu_page_frame, image=image2, border_width= 1 ,text="",fg_color= "white",hover_color="lightgray",command= waffle_fries )
image2_button.grid(row=3, column=3)
#bananas
banana_radio = customtkinter.StringVar()
banana = customtkinter.CTkRadioButton(waffle_fries_frame, text= "Banana", variable=banana_radio).grid(row=0, column=1, padx=20, pady=20, sticky="ew", columnspan=1)
no_banana = customtkinter.CTkRadioButton(waffle_fries_frame, text= "No Banana", variable=banana_radio).grid(row=0, column=2, padx=20, pady=20, sticky="e", columnspan=1)
#ice cream
whiped_cream_radio = customtkinter.StringVar()
whiped_cream = customtkinter.CTkRadioButton(waffle_fries_frame, text= "Whiped cream", variable=icecream_radio).grid(row=1, column=1, padx=20, pady=20, columnspan=1)
no_whiped_cream = customtkinter.CTkRadioButton(waffle_fries_frame, text= "No whiped cream", variable=icecream_radio).grid(row=1, column=2, padx=20, pady=20, columnspan=1)
confirm_classic = customtkinter.CTkButton(waffle_fries_frame, text= "confirm").grid(row=5, column=3, padx=20, pady=20, columnspan=1)
# number of items
number_of_items_label = customtkinter.CTkLabel(waffle_fries_frame, text= "Number of items" )
number_of_items_label.grid(column=2, row=3, columnspan=3)
number_of_items = Spinbox(waffle_fries_frame, from_=1, to=1000000000,font=("Arial", 14), width=10)
number_of_items.grid(column=2, row=4, columnspan=3)
#waffle bites
def waffle_bites():
    global waffle_bites_frame
    global price
    global menu_page_frame
    waffle_bites_frame.place(relx=0.5, rely=0.3, anchor="center")
    menu_page_frame.place_forget()
    price = +20.65
    print(price)
waffle_bites_frame = customtkinter.CTkScrollableFrame(app, width=750, border_width=2)
image5 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image5_button = customtkinter.CTkButton(menu_page_frame, text="",fg_color= "white",hover_color="lightgray", image=image2, command= waffle_bites)
image5_button.grid(row=4, column=1)

#waffle cake
def waffle_cake():
    global price
    global waffle_cake_frame
    global menu_page_frame
    waffle_cake_frame.place(relx=0.5, rely=0.3, anchor="center")
    menu_page_frame.place_forget()
    price = +20.65
    print(price)

waffle_cake_frame = customtkinter.CTkScrollableFrame(app, width=750, border_width=2)
image3 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image3_button = customtkinter.CTkButton(menu_page_frame, text="",fg_color= "white",hover_color="lightgray", image=image3, command= waffle_cake )
image3_button.grid(row=4, column=2)
#bananas
banana_radio = customtkinter.StringVar()
banana = customtkinter.CTkRadioButton(waffle_cake_frame, text= "Banana", variable=banana_radio).grid(row=0, column=1, padx=20, pady=20, sticky="ew", columnspan=1)
no_banana = customtkinter.CTkRadioButton(waffle_cake_frame, text= "No Banana", variable=banana_radio).grid(row=0, column=2, padx=20, pady=20, sticky="e", columnspan=1)
#ice cream
icecream_radio = customtkinter.StringVar()
icecream = customtkinter.CTkRadioButton(waffle_cake_frame, text= "Ice cream", variable=icecream_radio).grid(row=1, column=1, padx=20, pady=20, columnspan=1)
no_icecream2 = customtkinter.CTkRadioButton(waffle_cake_frame, text= "No ice cream", variable=icecream_radio).grid(row=1, column=2, padx=20, pady=20, columnspan=1)
double_icecream = customtkinter.CTkRadioButton(waffle_cake_frame, text= "Double scoop", variable=icecream_radio).grid(row=1, column=3, padx=20, pady=20, columnspan=1)
confirm_classic = customtkinter.CTkButton(waffle_cake_frame, text= "confirm").grid(row=5, column=3, padx=20, pady=20, columnspan=1)
number_of_items_label = customtkinter.CTkLabel(waffle_fries_frame, text= "Number of items" )
number_of_items_label.grid(column=2, row=3, columnspan=3)
number_of_items = Spinbox(waffle_fries_frame, from_=1, to=1000000000,font=("Arial", 14), width=10)
number_of_items.grid(column=2, row=4, columnspan=3)


cold_drinks_lable = customtkinter.CTkLabel(menu_page_frame, text ="Iced Menu").grid(row=5, column=2)
#Choclate drinks
def iced_choclate():
    global price
    global iced_choclate_frame
    global menu_page_frame
    iced_choclate_frame.place(relx=0.5, rely=0.3, anchor="center")
    menu_page_frame.place_forget()
    price = +20.65
    print(price)



iced_choclate_frame = customtkinter.CTkScrollableFrame(app, width=750, border_width=2)
image9 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image9_button = customtkinter.CTkButton(menu_page_frame, text="",fg_color= "white",hover_color="lightgray", image=image3, command= iced_choclate)
image9_button.grid(row=6, column=1)
#size
size_radio = customtkinter.StringVar()
normal = customtkinter.CTkRadioButton(iced_choclate_frame, text= "normal", variable=banana_radio).grid(row=0, column=1, padx=20, pady=20, sticky="ew", columnspan=1)
large = customtkinter.CTkRadioButton(iced_choclate_frame, text= "large", variable=banana_radio).grid(row=0, column=2, padx=20, pady=20, sticky="e", columnspan=1)
#whipped cream
hiped_cream_radio = customtkinter.StringVar()
whiped_cream = customtkinter.CTkRadioButton(iced_choclate_frame, text= "Whiped cream", variable=icecream_radio).grid(row=1, column=1, padx=20, pady=20, columnspan=1)
no_whiped_cream = customtkinter.CTkRadioButton(iced_choclate_frame, text= "No whiped cream", variable=icecream_radio).grid(row=1, column=2, padx=20, pady=20, columnspan=1)
number_of_items_label = customtkinter.CTkLabel(iced_choclate_frame, text= "Number of items" )
number_of_items_label.grid(column=2, row=3, columnspan=3)
number_of_items = Spinbox(iced_choclate_frame, from_=1, to=1000000000,font=("Arial", 14), width=10)
number_of_items.grid(column=2, row=4, columnspan=3)


#smoothies
def smoothies():
    global smoothies_label
    smoothies_frame.place(relx=0.5, rely=0.3, anchor="center")
smoothies_frame = customtkinter.CTkScrollableFrame(app, width=750, border_width=2)
image10 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image10_button = customtkinter.CTkButton(menu_page_frame, text="",fg_color= "white",hover_color="lightgray", image=image2, command= smoothies )
image10_button.grid(row=6, column=3)
#flavours
flavours_label = customtkinter.CTkLabel(smoothies_frame, text= "flavours" )
flavours_label.grid(column=2, row=2, columnspan=3)
flavours_radio = customtkinter.StringVar()
banana = customtkinter.CTkRadioButton(smoothies_frame, text= "Banana", variable=flavours_radio).grid(row=3, column=1, padx=20, pady=20, columnspan=1)
strawberry = customtkinter.CTkRadioButton(smoothies_frame, text= "strawberry", variable=flavours_radio).grid(row=3, column=2, padx=20, pady=20, columnspan=1)
blueberry = customtkinter.CTkRadioButton(smoothies_frame, text= "blueberry", variable=flavours_radio).grid(row=3, column=3, padx=20, pady=20, columnspan=1)
mango = customtkinter.CTkRadioButton(smoothies_frame, text= "mango", variable=flavours_radio).grid(row=4, column=1, padx=20, pady=20, columnspan=1)
date = customtkinter.CTkRadioButton(smoothies_frame, text= "date", variable=flavours_radio).grid(row=4, column=2, padx=20, pady=20, columnspan=1)
confirm_classic = customtkinter.CTkButton(smoothies_frame, text= "confirm").grid(row=7, column=3, padx=20, pady=20, columnspan=1)
#size
size_radio = customtkinter.StringVar()
normal = customtkinter.CTkRadioButton(smoothies_frame, text= "normal", variable=banana_radio).grid(row=0, column=1, padx=20, pady=20, sticky="ew", columnspan=1)
large = customtkinter.CTkRadioButton(smoothies_frame, text= "large", variable=banana_radio).grid(row=0, column=2, padx=20, pady=20, sticky="e", columnspan=1)
#whipped cream
whiped_cream_radio = customtkinter.StringVar()
whiped_cream = customtkinter.CTkRadioButton(smoothies_frame, text= "Whiped cream", variable=icecream_radio).grid(row=1, column=1, padx=20, pady=20, columnspan=1)
no_whiped_cream = customtkinter.CTkRadioButton(smoothies_frame, text= "No whiped cream", variable=icecream_radio).grid(row=1, column=2, padx=20, pady=20, columnspan=1)
number_of_items_label = customtkinter.CTkLabel(smoothies_frame, text= "Number of items" )
number_of_items_label.grid(column=2, row=3, columnspan=3)
number_of_items = Spinbox(smoothies_frame, from_=1, to=1000000000,font=("Arial", 14), width=10)
number_of_items.grid(column=2, row=4, columnspan=3)

#slushies
def slushies():
    global slushies_label
    slushies_label.grid(row=3, column=3)
slushies_label = customtkinter.CTkLabel(menu_page_frame, text="slushies")
image11 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image11_button = customtkinter.CTkButton(menu_page_frame, text="",fg_color= "white",hover_color="lightgray", image=image2, command= slushies )
image11_button.grid(row=7, column=1)

hot_drinks_lable = customtkinter.CTkLabel(menu_page_frame, text ="hot_drinks").grid(row=8, column=2)

#Coffee
def coffee():
    global coffee_label
    coffee_label.grid(row=4, column=4)
coffee_label = customtkinter.CTkLabel(menu_page_frame, text="Coffee")
image7 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image7_button = customtkinter.CTkButton(menu_page_frame, text="",fg_color= "white",hover_color="lightgray", image=image2, command= coffee )
image7_button.grid(row=9, column=1)
#hot Choclate

def hot_choclate():
    global choclate_drink_label
    choclate_drink_label.grid(row=3, column=3)
choclate_drink_label = customtkinter.CTkLabel(menu_page_frame, text="hot_choclate")
image9 = customtkinter.CTkImage(light_image=Image.open("classic waffle.png"), size=(200,200))
image9_button = customtkinter.CTkButton(menu_page_frame, text="",fg_color= "white",hover_color="lightgray", image=image2, command= hot_choclate )
image9_button.grid(row=9, column=2)





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
#bubble
Toppings_label = customtkinter.CTkLabel(bubble_waffle_frame, text="Toppings").grid(row=0, column=0)
topping1 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Maple")
topping1.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping2 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Lotus Biscoff Sauce")
topping2.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping3 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Strawberry")
topping3.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping4 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Passion Fruit")
topping4.grid(row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping5 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Chocolate Sauce ")
topping5.grid(row=6, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping6 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Peanut Butter sauce")
topping6.grid(row=7, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping7= customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Fruit silk Sauce")
topping7.grid(row=8, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping8 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Citrus Peel topping")
topping8.grid(row=9, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping9 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Extra Ice Cream Scoop")
topping9.grid(row=10, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping10 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Lotus Biscoff Sauce")
topping10.grid(row=11, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping11 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Pistachio topping sauce")
topping11.grid(row=12, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping12 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Almond topping sauce")
topping12.grid(row=13, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping13 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Dulce de Leche Caramel")
topping13.grid(row=14, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping14 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= " hazelnut spread")
topping14.grid(row=15, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping15 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Extra Banana")
topping15.grid(row=16, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Fruit silk Sauce")
topping16.grid(row=17, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping17 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Peanut Butter sauce")
topping17.grid(row=18, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "Add Lotus Biscoff crumbles ")
topping16.grid(row=19, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "chopped up Whittaker's PEANUT SLAB ")
topping16.grid(row=20, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping8 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "chopped up Whittaker's Creamy Milk ")
topping8.grid(row=21, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping8 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "chopped up Whittaker's BERRY FOREST ")
topping8.grid(row=22, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping8 = customtkinter.CTkCheckBox(bubble_waffle_frame, text= "chopped up Whittaker's Creamy Milk")
topping8.grid(row=23, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
#fries
Toppings_label = customtkinter.CTkLabel(waffle_fries_frame, text="Toppings").grid(row=0, column=0)
topping1 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Maple")
topping1.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping2 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Lotus Biscoff Sauce")
topping2.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping3 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Strawberry")
topping3.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping4 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Passion Fruit")
topping4.grid(row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping5 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Chocolate Sauce ")
topping5.grid(row=6, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping6 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Peanut Butter sauce")
topping6.grid(row=7, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping7= customtkinter.CTkCheckBox(waffle_fries_frame, text= "Fruit silk Sauce")
topping7.grid(row=8, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping8 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Citrus Peel topping")
topping8.grid(row=9, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping9 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Extra Ice Cream Scoop")
topping9.grid(row=10, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping10 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Lotus Biscoff Sauce")
topping10.grid(row=11, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping11 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Pistachio topping sauce")
topping11.grid(row=12, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping12 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Almond topping sauce")
topping12.grid(row=13, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping13 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Dulce de Leche Caramel")
topping13.grid(row=14, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping14 = customtkinter.CTkCheckBox(waffle_fries_frame, text= " hazelnut spread")
topping14.grid(row=15, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping15 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Extra Banana")
topping15.grid(row=16, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Fruit silk Sauce")
topping16.grid(row=17, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping17 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Peanut Butter sauce")
topping17.grid(row=18, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "Add Lotus Biscoff crumbles ")
topping16.grid(row=19, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_fries_frame, text= "chopped up Whittaker's PEANUT SLAB ")
topping16.grid(row=20, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
#bites
Toppings_label = customtkinter.CTkLabel(waffle_cake_frame, text="Toppings").grid(row=0, column=0)
topping1 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Maple")
topping1.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping2 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Lotus Biscoff Sauce")
topping2.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping3 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Strawberry")
topping3.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping4 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Passion Fruit")
topping4.grid(row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping5 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Chocolate Sauce ")
topping5.grid(row=6, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping6 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Peanut Butter sauce")
topping6.grid(row=7, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping7= customtkinter.CTkCheckBox(waffle_cake_frame, text= "Fruit silk Sauce")
topping7.grid(row=8, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping8 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Citrus Peel topping")
topping8.grid(row=9, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping9 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Extra Ice Cream Scoop")
topping9.grid(row=10, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping10 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Lotus Biscoff Sauce")
topping10.grid(row=11, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping11 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Pistachio topping sauce")
topping11.grid(row=12, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping12 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Almond topping sauce")
topping12.grid(row=13, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping13 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Dulce de Leche Caramel")
topping13.grid(row=14, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping14 = customtkinter.CTkCheckBox(waffle_cake_frame, text= " hazelnut spread")
topping14.grid(row=15, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping15 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Extra Banana")
topping15.grid(row=16, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Fruit silk Sauce")
topping16.grid(row=17, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping17 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Peanut Butter sauce")
topping17.grid(row=18, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Add Lotus Biscoff crumbles ")
topping16.grid(row=19, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "chopped up Whittaker's PEANUT SLAB ")
topping16.grid(row=20, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
#cake
Toppings_label = customtkinter.CTkLabel(waffle_cake_frame, text="Toppings").grid(row=0, column=0)
topping1 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Maple")
topping1.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping2 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Lotus Biscoff Sauce")
topping2.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping3 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Strawberry")
topping3.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping4 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Passion Fruit")
topping4.grid(row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping5 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Chocolate Sauce ")
topping5.grid(row=6, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping6 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Peanut Butter sauce")
topping6.grid(row=7, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping7= customtkinter.CTkCheckBox(waffle_cake_frame, text= "Fruit silk Sauce")
topping7.grid(row=8, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping8 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Citrus Peel topping")
topping8.grid(row=9, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

topping9 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Extra Ice Cream Scoop")
topping9.grid(row=10, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping10 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Lotus Biscoff Sauce")
topping10.grid(row=11, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping11 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Pistachio topping sauce")
topping11.grid(row=12, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping12 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Almond topping sauce")
topping12.grid(row=13, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping13 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Dulce de Leche Caramel")
topping13.grid(row=14, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping14 = customtkinter.CTkCheckBox(waffle_cake_frame, text= " hazelnut spread")
topping14.grid(row=15, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping15 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Extra Banana")
topping15.grid(row=16, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Fruit silk Sauce")
topping16.grid(row=17, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping17 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Peanut Butter sauce")
topping17.grid(row=18, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "Add Lotus Biscoff crumbles ")
topping16.grid(row=19, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

topping16 = customtkinter.CTkCheckBox(waffle_cake_frame, text= "chopped up Whittaker's PEANUT SLAB ")
topping16.grid(row=20, column=0, padx=20, pady=20, sticky="ew", columnspan=2)







app.mainloop()