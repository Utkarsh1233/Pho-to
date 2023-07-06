import datetime
import os
import time
import requests
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

op = CTk()

set_appearance_mode('dark')
set_default_color_theme('green')

op.title('ᴘʜᴏ-ᴛᴏ')
op.iconbitmap("C:\\Users\\tiesa\\IdeaProjects\\CU BRO\\icon.ico")
op.maxsize(565,500)

bg = Image.open('C:\\Users\\tiesa\\IdeaProjects\\CU BRO\\img.jpg')
bgm = ImageTk.PhotoImage(bg)
Label(op,image=bgm).pack()

CTkFrame(op,350,330,20,bg_color="black").place(x=110, y=70)

#Upper Section
n1 = StringVar()
n2 = StringVar()

n1.set("Enter Image Address")
n2.set("Enter File Name")

p1 = CTkEntry(op,300,35,70,bg_color="#302c2c",textvariable=n1,border_width=1,border_color="light green",fg_color="black",placeholder_text="Enter Image URL")
p1.place(x=135,y=100)
p2 = CTkEntry(op,300,35,70,bg_color="#302c2c",border_width=1,textvariable=n2,border_color="light green",fg_color="black",placeholder_text="Enter File Name")
p2.place(x=135,y=150)

Label(op, text="𝐒𝐞𝐥𝐞𝐜𝐭 𝐅𝐢𝐥𝐞 𝐄𝐱𝐭𝐞𝐧𝐬𝐢𝐨𝐧", cursor="xterm", font=30, bg="#302c2c", fg="white").place(x=330, y=290)
p3 = CTkComboBox(op, width=300, height=35,bg_color="#302c2c", corner_radius=18,dropdown_fg_color="black",border_color="light green",button_color="green", values=["PNG","JPG","JPEG"], fg_color="black",border_width=1, button_hover_color="dark green")
p3.place(x=135,y=220)

Label(op, text="𝐒𝐞𝐥𝐞𝐜𝐭 𝐈𝐦𝐚𝐠𝐞 𝐐𝐮𝐚𝐥𝐢𝐭𝐲", cursor="xterm", font=30, bg="#302c2c", fg="white").place(x=330, y=395)
p4 = CTkComboBox(op,border_color="light green", width=300, height=35,bg_color="#302c2c", corner_radius=18,dropdown_fg_color="black",border_width=1,button_hover_color="dark green",button_color="green", values=["High","Median","Low"], fg_color="black")
p4.place(x=135,y=290)

def Save():
    p1.configure(border_color="light green")
    p2.configure(border_color="light green")
    global response, image_file, im
    try:
        if p3.get() == "PNG" or p3.get() == "JPG" or p3.get() == "JPEG"  and (("http://" or "https://") in n1.get()):
            p3.configure(button_color="green", button_hover_color="dark green", border_color="light green")
            f = (n2.get()+"."+p3.get().lower())
            response = requests.get(n1.get())

            if response.status_code == 200:
                if (("'" not in p2.get()) and ('"' not in p2.get()) and ('^' not in p2.get()) and ('%' not in p2.get()) and ('#' not in p2.get()) and ('@' not in p2.get()) and ("<" not in p2.get()) and (">" not in p2.get())):
                    p4.configure(button_color="green", button_hover_color="dark green", border_color="light green")
                    fp = open(f, 'wb')
                    fp.write(response.content)
                    fp.close()

                    im = str(os.getcwd())+"\\"+f

                    image_path = im
                    image_file = Image.open(image_path)
                else:
                    p2.configure(border_color="red")
            else:
                p1.configure(border_color="red")

            if p4.get() == "High":
                image_file.save(f, quality=95)
                p4.configure(button_color="green", button_hover_color="dark green", border_color="light green")
                messagebox.showinfo("ᴘʜᴏ-ᴛᴏ", f"ɪᴍᴀɢᴇ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ\n{im}")
            elif p4.get() == "Median":
                 image_file.save(f, quality=25)
                 p4.configure(button_color="green", button_hover_color="dark green", border_color="light green")
                 messagebox.showinfo("ᴘʜᴏ-ᴛᴏ", f"ɪᴍᴀɢᴇ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ\n{im}")
            elif p4.get() == "Low":
                image_file.save(f, quality=1)
                p4.configure(button_color="green", button_hover_color="dark green", border_color="light green")
                messagebox.showinfo("ᴘʜᴏ-ᴛᴏ", f"ɪᴍᴀɢᴇ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ\n{im}")
            elif p4.get() != "Low" or "High" or "Median":
                p4.configure(button_color="red", button_hover_color="dark red", border_color="red")
                messagebox.showerror("ᴘʜᴏ-ᴛᴏ","ǫᴜᴀʟɪᴛʏ ɪs ɴᴏᴛ ᴀᴘᴘʟɪᴇᴅ ɪɴ ʏᴏᴜʀ ɪᴍᴀɢᴇ\nᴜɴᴋɴᴏᴡɴ ɪᴍᴀɢᴇ ǫᴜᴀʟɪᴛʏ !")

            n1.set("Enter Image Address")
            n2.set("Enter Image Name")
            response.close()
        else:
            p3.configure(button_color="red", button_hover_color="dark red", border_color="red")
            messagebox.showerror("ᴘʜᴏ-ᴛᴏ", f"ᴜɴᴋɴᴏᴡɴ ғɪʟᴇ ᴇxᴛᴇɴsɪᴏɴ !")
            n1.set("Enter Image Address")
            n2.set("Enter Image Name")

    except(FileNotFoundError, FileExistsError, ValueError, NameError, RuntimeError, TypeError, InterruptedError, IOError):
        messagebox.showerror("ᴘʜᴏ-ᴛᴏ", "ᴛʜᴇʀᴇ ɪs sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ !")

CTkButton(op, border_width=1,command=Save, border_color="light green", font=("Bold",15), border_spacing=1, text="Save", corner_radius=80).place(x=215, y=350)
# Upper Section

op.mainloop()