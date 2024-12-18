from tkinter import *
from tkinter import messagebox


dic = {'yacolate': '950519'}


# 登入邏輯函數
def login():
    username = entry_username.get()
    password = entry_password.get()
    if username in dic:
        if dic[username] == password:
            openTempWindow()
        else:
            messagebox.showerror('ERROR', "Account or Password wrong")
    else:
        messagebox.showerror('Error', "Account doesn't exist")


def openTempWindow():
    root.withdraw()
    temp_window = Toplevel(root)
    temp_window.title('Welcome')
    temp_window.geometry('500x400')
    temp_window.configure(bg='white')

    canvas = Canvas(temp_window, width=500, height=400)
    canvas.pack(fill = 'both')
    create_gradient(canvas, 500, 400, "#FFEFDB", "#FFA07A") 
    
    frame_buttons = Frame(temp_window ,bg = 'white')
    frame_buttons.pack(fill = 'both' , expand = True)
    
    Snake_game = Button(temp_window , text = '貪吃蛇遊戲' , font = ('Arial',20,'bold') , command = Snake_game_window).pack(pady = 20)
    Draw_game = Button(temp_window , text = '辨識小畫家' , font = ('Arial',20,'bold') , command = Draw_game_window).pack(pady = 20)

def Snake_game_window():
    return 

def Draw_game_window():
    return

def close_login_Window(window):
    root.deiconify()
    window.destroy()


# 建立漸變背景
def create_gradient(canvas, width, height, color1, color2):
    """ 用 Canvas 繪製漸變背景 """
    steps = 100  # 漸變的層數越多越平滑
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)
    r_ratio = (r2 - r1) / steps
    g_ratio = (g2 - g1) / steps
    b_ratio = (b2 - b1) / steps

    for i in range(steps):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr >> 8:02x}{ng >> 8:02x}{nb >> 8:02x}'  # 顏色轉換
        y0 = int(i * (height / steps))
        y1 = int((i + 1) * (height / steps))
        canvas.create_rectangle(0, y0, width, y1, outline="", fill=color)


#main
root = Tk()
root.title("Sign in to your account")
root.geometry("500x400")

#background
canvas = Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, 500, 400, "#FFEFDB", "#FFA07A")  # 淺橙色漸變

# 主要框架
frame = Frame(canvas, bg="white", bd=2, relief="flat")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

# 標題
label_title = Label(frame, text="Sign in to your account", font=("Arial", 16, "bold"), bg="white", fg="#333")
label_title.pack(pady=15)

# 使用者名稱輸入框
label_username = Label(frame, text="Email or username", font=("Arial", 10), bg="white", fg="#555")
label_username.pack(anchor="w", padx=20)
entry_username = Entry(frame, font=("Arial", 12))
entry_username.pack(padx=20, pady=5, fill="x")

# 密碼輸入框
label_password = Label(frame, text="Password", font=("Arial", 10), bg="white", fg="#555")
label_password.pack(anchor="w", padx=20)
entry_password = Entry(frame, show="*", font=("Arial", 12))
entry_password.pack(padx=20, pady=5, fill="x")

# 忘記密碼
label_forgot = Label(frame, text="Forgot password?", font=("Arial", 9), fg="#FF4500", bg="white", cursor="hand2")
label_forgot.pack(anchor="e", padx=20, pady=5)

# 登入按鈕
btn_login = Button(frame, text="SIGN IN", font=("Arial", 12, "bold"), bg="#FF4500", fg="white", bd=0, cursor="hand2",
                      command=login)
btn_login.pack(pady=10, fill="x", padx=20)

# 註冊按鈕
label_register = Label(frame, text="New to the system? ", font=("Arial", 10), bg="white", fg="#333")
label_register.pack(side="left", padx=50, pady=10)

btn_register = Button(frame, text="Register", font=("Arial", 10, "bold"), fg="#FF4500", bg="white", relief="flat",
                         cursor="hand2", command=lambda: messagebox.showinfo("Register", "Register Logic Here"))
btn_register.pack(side="right", padx=50)

# 啟動視窗
root.mainloop()
