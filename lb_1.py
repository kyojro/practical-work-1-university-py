import os
from pathlib import Path
from shutil import rmtree
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()


root["bg"] = "#fafafa"
root.title("tool key")
root.geometry("300x80")
root.resizable(width = True, height = True)
    
Path_1 = Path("/home/ros/Desktop/lb").glob("**/*")

lb_path = ("/home/ros/Desktop/lb/lab_1.py")

Folder_chek = "/home/ros/Desktop/lb"
def clear_folder():
    if not os.listdir(Folder_chek):
        messagebox.showinfo(title = "info", \
                            message = "your directory is empty")
    else:
        for path in Path_1:
            print(Path_1)
            if path == lb_path:
                continue
            
            elif path.is_file():
                path.unlink()
                
            elif path.is_dir():
                rmtree(path)
        messagebox.showinfo(title = "info", \
                            message = "directory clear. End!")
        
            
def close_prog():
        root.destroy()
        
                      
lb_1 = Label(root, text = " click the clean button to empty the folder ", bg = "#fafafa")


closeButton = Button(root, text = "     Cancel     ", command = close_prog)


okButton = Button(root, text = "     Clear      ", \
                  command = clear_folder)


lb_1.place(x = 9, y = 0)
okButton.place(x = 80, y = 23)
closeButton.place(x = 162, y = 23)


root.mainloop()
