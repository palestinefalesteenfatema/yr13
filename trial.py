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

root.mainloop()
