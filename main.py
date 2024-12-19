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
    
    btn = Button(snake_game_window , text = 'Close' , command = lambda : close_game_window(snake_game_window)).pack()

#################################################################


# #######################################################






# snake_game_window.mainloop()

def open_draw_window():
    TempWindow.withdraw()
    draw_window = Toplevel()
    draw_window.title('Draw Game')
    # draw_window.geometry('800x600')

    def get_current_color():
        return f'#{red.get():02x}{green.get():02x}{blue.get():02x}'

    def update_preview(*args):
        color_preview.config(bg=get_current_color())

    def paint(event):
        x1, y1 = (event.x - brush_size.get()), (event.y - brush_size.get())
        x2, y2 = (event.x + brush_size.get()), (event.y + brush_size.get())
        color = get_current_color()
        canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def clear_canvas():
        canvas.delete('all')

    def capture():
        x0 = canvas.winfo_rootx()
        y0 = canvas.winfo_rooty()
        x1 = x0 + canvas.winfo_width()
        y1 = y0 + canvas.winfo_height()
        im = ImageGrab.grab((x0, y0, x1, y1))
        im.save('mypic.png')

    # Variables for brush size and color
    brush_size = tk.DoubleVar(value=5)
    red = IntVar(value=0)
    green = IntVar(value=0)
    blue = IntVar(value=0)

    # Canvas for drawing
    canvas = Canvas(draw_window, bg='white', width=800, height=500)
    canvas.grid(row=0, column=0, columnspan=4, pady=10)
    canvas.bind("<B1-Motion>", paint)

    # Control Frame
    control_frame = tk.Frame(draw_window)
    control_frame.grid(row=1, column=0, columnspan=4, pady=10)

    Label(control_frame, text='紅色', font=('Arial', 10)).grid(row=0, column=0, padx=5)
    Scale(control_frame, from_=0, to=255, variable=red, orient='horizontal', command=update_preview).grid(row=0, column=1, padx=5)

    Label(control_frame, text='綠色', font=('Arial', 10)).grid(row=1, column=0, padx=5)
    Scale(control_frame, from_=0, to=255, variable=green, orient='horizontal', command=update_preview).grid(row=1, column=1, padx=5)

    Label(control_frame, text='藍色', font=('Arial', 10)).grid(row=2, column=0, padx=5)
    Scale(control_frame, from_=0, to=255, variable=blue, orient='horizontal', command=update_preview).grid(row=2, column=1, padx=5)

    Label(control_frame, text='顏色預覽', font=('Arial', 10)).grid(row=0, column=2, padx=5)
    color_preview = Label(control_frame, bg=get_current_color(), width=10, height=1)
    color_preview.grid(row=1, column=2, padx=5, rowspan=2)

    # Buttons
    clear_button = Button(control_frame, text='清除畫布', command=clear_canvas, bg='red', fg='black')
    clear_button.grid(row=3, column=0, columnspan=2, pady=10)

    predict_button = Button(control_frame, text='儲存圖像', command=capture, bg='blue', fg='black')
    predict_button.grid(row=3, column=2, pady=10)

    close_button = Button(draw_window, text='Close', command=lambda: close_game_window(draw_window), bg='gray', fg='black')
    close_button.grid(row=4, column=0, columnspan=4, pady=10)

    update_preview()


##############################################################
    btn = Button(draw_window , text = 'Close' , command = lambda : close_game_window(draw_window)).pack()
    

    
def close_game_window(game_window):
    TempWindow.deiconify()
    game_window.destroy()
        
def closeWindow(self):
    root.deiconify()
    self.destroy()

# 註冊
def register():
    username = entry_username.get()
    password = entry_password.get()
    if username in dic:
        messagebox.showerror('ERROR',"Account already exits")
    else:
        dic[username] = password
    
    
    
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

print('Test')
root.mainloop()
