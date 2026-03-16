#we use tkinter=module/library (module=single py file along with many fun and useful things)(lib-collection of many library )
#import tkinter for creating gui apps

import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

#functionality
text = tk.Text(
root,
wrap=tk.WORD,
font=("Helvetica",12)
)

text.pack(expand=True,fill=tk.BOTH)

#main logic

#func-1 to create new file

def new_file():
    text.delete(1.0, tk.END)
    

# fun-2 open a new file
def oepn_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path,"r") as file:
             text.delete(1.0, tk.END)
             text.insert(tk.END, file.read())

# fun-3 save file
def save_file():
     file_path = filedialog.asksaveasfilename(
       defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]  
     )

     if file_path:
         with open(file_path,"w") as file:
             file.write(text.get(1.0,tk.END))

     messagebox.showinfo("Info","file saved successfully")
 #create menubar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)


menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=oepn_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)




root.mainloop()

