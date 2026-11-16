import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image 
from rembg import remove
import os
def make_sticker():
    file = filedialog.askopenfilename(filetypes=[("images","*.png *.jpg *.jpeg")])
    if file:
        image = Image.open(file)
        sticker = remove(image)
        sticker = remove(image)
        sticker.thumbnail((512,512))
        name = os.path.splitext(file)[0]
        sticker.save(name + "_sticker.png")
        messagebox.showinfo("Success","Sticker created Successfully!")
root = tk.Tk()
root.title("AI Sticker Maker")
root.geometry("400x300")
title = tk.Label(root, text="AI Sticker Maler", font = ("Arial",20))
title.pack(pady=40)
button = tk.Button(root, text = "Upload Image",command=make_sticker)
button.pack(pady=20)
root.mainloop()