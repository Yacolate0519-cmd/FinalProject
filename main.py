from tkinter import *
from tkinter import messagebox
import random
from PIL import Image , ImageGrab
from tkinter import ttk
import tkinter as tk

dic = {'yacolate':'950519'}


# 登入
def login():
    username = entry_username.get()
    password = entry_password.get()
    if username in dic:
        if dic[username] == password:
            #開新視窗
            openTempWindow()
        else:
            messagebox.showerror('ERROR',"Account or Password wroung")
    else:
        messagebox.showerror('Error' , "Account doen't exists")

# 註冊
def register():
    username = entry_username.get()
    password = entry_password.get()
    if username in dic:
        messagebox.showerror('ERROR',"Account already exits")
    else:
        dic[username] = password

def openTempWindow():
    global TempWindow
    root.withdraw()
    TempWindow = Toplevel(root)
    TempWindow.title('TempWindow')
    TempWindow.geometry('500x400')

    canvas = Canvas(TempWindow, width=500, height=400)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)  # 設置 Canvas 作為背景
    create_gradient(canvas, 500, 400, "#FFEFDB", "#FFA07A") 

    
    snake_game_button = Button(TempWindow, text='貪吃蛇', font=('Arial', 20, 'bold'),
                                command = open_snake_window , cursor = 'hand2')
    snake_game_button.place(relx=0.5, rely=0.3, anchor="center")  # 使用 place() 進行精確定位

    Draw_game_button = Button(TempWindow, text='小畫家', font=('Arial', 20, 'bold'), 
                          command=open_draw_window, 
                            relief=RAISED, cursor='hand2')
    Draw_game_button.place(relx=0.5, rely=0.5, anchor='center')


    close_button = Button(TempWindow, text='Close', font=('Arial', 15),
                          command=lambda: closeWindow(TempWindow) , cursor = 'hand2')
    close_button.place(relx=0.5, rely=0.7, anchor="center")  # 定位第二個按鈕

    
    
    
#Temp Button package    
def open_snake_window():
    TempWindow.withdraw()
    snake_game_window = Toplevel()
    snake_game_window.geometry('500x500')
    snake_game_window.title('Snake_Game')
    
    btn = Button(snake_game_window , text = 'Close' , command = close_snake_window).pack()

def close_snake_window():
    global snake_game_window
    snake_game_window.destroy()
    snake_game_window = None
    TempWindow.deiconify()

# snake_game_window.mainloop()
    
    

def open_draw_window():
    return 
    
def closeWindow(self):
    root.deiconify()
    entry_username.delete(0,END)
    entry_password.delete(0,END)
    self.destroy()


    
    
    
#log in window package
# 建立視窗
root = Tk()
root.title("Sign in to your account")
root.geometry("500x400")

# 背景
def create_gradient(canvas , width , height , color1 , color2):
    steps = 100
    r1,g1,b1 = root.winfo_rgb(color1)
    r2,g2,b2 = root.winfo_rgb(color2)
    r_ratio = (r2 - r1) / steps
    g_ratio = (g2 - g1) / steps
    b_ratio = (b2 - b1) / steps
    
    for i in range(steps):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr >> 8:02x}{ng >> 8:02x}{nb >> 8:02x}'
        y0 = int(i * (height / steps))
        y1 = int((i+1)*(height / steps))
        canvas.create_rectangle(0 , y0 , width , y1 , outline = '' , fill = color)

canvas = Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, 500, 400, "#FFEFDB", "#FFA07A")  # 淺橙色漸變
    

# 主要框架
frame = Frame(canvas, bg="#FFEFDB", bd=2, relief="flat")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

# 標題
label_title = Label(frame, text="Sign in to your account", font=("Arial", 16, "bold"), bg="#FFEFDB", fg="#333")
label_title.pack(pady=15)

# 使用者名稱輸入框
label_username = Label(frame, text="Email or username", font=("Arial", 10), bg="#FFEFDB", fg="#555")
label_username.pack(anchor="w", padx=20)
entry_username = Entry(frame, font=("Arial", 12))
entry_username.pack(padx=20, pady=5, fill="x")

# 密碼輸入框
label_password = Label(frame, text="Password", font=("Arial", 10), bg="#FFEFDB", fg="#555")
label_password.pack(anchor="w", padx=20)
entry_password = Entry(frame, show="*", font=("Arial", 12))
entry_password.pack(padx=20, pady=5, fill="x")

# 忘記密碼
label_forgot = Label(frame, text="Forgot password?", font=("Arial", 9), fg="#FF4500", bg="#FFEFDB", cursor="hand2")
label_forgot.pack(anchor="e", padx=20, pady=5)

# 登入按鈕
btn_login = Button(frame, text="Log IN", font=("Arial", 12, "bold"), bg="#FF4500", fg="red", bd=0, cursor="hand2", command=login)
btn_login.pack(pady=10, fill="x", padx=20)

# 註冊按鈕
label_register = Label(frame, text="New to the system? ", font=("Arial", 10), bg="#FFEFDB", fg="#333")
label_register.pack(side="left", padx=50, pady=10)

btn_register = Button(frame, text="Register", font=("Arial", 10, "bold"), fg="#FF4500", bg="#FFEFDB", relief="flat", cursor="hand2", command=register)
btn_register.pack(side="right", padx=50)


root.mainloop()
