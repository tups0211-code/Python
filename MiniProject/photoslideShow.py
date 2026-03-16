#slideshow  app

import tkinter as tk
import time
from PIL import Image,ImageTk

#main window
root = tk.Tk()
root.title("Photo SlideShow")
root.geometry("900x900")

#list of img path
image_path =[
    r"C:\Users\a\Desktop\images\img1.png",
    r"C:\Users\a\Desktop\images\img2.png",
    r"C:\Users\a\Desktop\images\img3.png",
    r"C:\Users\a\Desktop\images\img4.png",
    r"C:\Users\a\Desktop\images\img5.png",
]
image_size = (700 , 450)
images =[]
for path in image_path:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img)

final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

image_label = tk.Label(root)
image_label.pack(pady=30)

def slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(1)

play_button = tk.Button(
    root,
    text = "play the slide show",
    font=("Arial",17),
    command=slideshow
)
play_button.pack(pady=40)

root.mainloop()

