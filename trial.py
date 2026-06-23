import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Background widget using relative positioning
bg_label = tk.Label(root, text="Background", bg="yellow",
                   font=("Arial", 20))
bg_label.place(relx=0.5, rely=0.5, anchor="center")

# Overlapping widget
overlay_button = tk.Button(root, text="Overlay Button", bg="red", fg="white")
overlay_button.place(relx=0.5, rely=0.5, anchor="center")



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
image3_button = customtkinter.CTkButton(menu_page_frame, text="bubble waffle", image=image3, command= bubble_waffle )
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
confirm_classic = customtkinter.CTkButton(bubble_waffle_frame, text= "confirm").grid(row=3, column=3, padx=20, pady=20, columnspan=1)
#type
type_radio = customtkinter.StringVar()
plate = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "Bubble waffle on a plate ", variable=type_radio).grid(row=2, column=2, padx=20, pady=20, columnspan=1)
cone = customtkinter.CTkRadioButton(bubble_waffle_frame, text= "Bubble waffle cone", variable=type_radio).grid(row=2, column=3, padx=20, pady=20, columnspan=1)

root.mainloop()
