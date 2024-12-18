from tkinter import *
from tkinter import messagebox


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

    Draw_game_button = Button(TempWindow , text = '小畫家' , font = ('Arial' , 20 , 'bold') 
                              , command = lambda : open_draw_window(TempWindow),
                              relief = RAISED , cursor = 'hand2')
    Draw_game_button.place(relx = 0.5 , rely = 0.5 , anchor = 'center')

    close_button = Button(TempWindow, text='Close', font=('Arial', 15),
                          command=lambda: closeWindow(TempWindow) , cursor = 'hand2')
    close_button.place(relx=0.5, rely=0.7, anchor="center")  # 定位第二個按鈕

    
    
    
#Temp Button package    
def open_snake_window():
    TempWindow.withdraw()
    snake_game_window = Toplevel()
    snake_game_window.geometry('500x500')
    snake_game_window.title('Snake_Game')
    
    Game_width = 500
    Game_height = 500
    canvas = Canvas(snake_game_window , width = Game_width , height = Game_height , bg = 'black')
    canvas.pack(fill = 'both' , expand = True)
    
    title = Label(snake_game_window , text = 'Snake Game' , font = ("Arial" , 20) , fg = 'white' , bg = 'black').pack()
    
    Board_size = 20
    speed = 100
    body_length = 3
    body_color = 'green'
    food_color = 'red'
    
    snake_parts = []
    for i in range(body_length):
        x = 100 - i * Board_size
        y = 100
        part = canvas.create_rectangle(x , y , x + Board_size , y + Board_size , fill = 'green' , outline = '')
        snake_parts.append(part)
        
        
    direction = 'right'
    
    def move_snake():
        global snake_parts , direction
        head_coords = canvas.coords(snake_parts[0])
        x1,y1,x2,y2 = head_coords
        
        if direction == 'right':
            new_head = canvas.create_rectangle(x1 + Board_size , y1 , x2 + Board_size , y2 , fill = 'green' , outline = '')
        elif direction == 'left':
            new_head = canvas.create_rectangle(x1 - Board_size , y1 , x2 - Board_size , y2 , fill = 'green' , outline = '')
        elif direction == 'up':
            new_head = canvas.create_rectangle(x1  , y1 - Board_size , x2 , y2 - Board_size, fill = 'green' , outline = '')
        elif direction == 'down':
            new_head = canvas.create_rectangle(x1 , y1 + Board_size , x2  , y2 + Board_size, fill = 'green' , outline = '')
    
        snake_parts.insert(0,new_head)
        canvas.delete(snake_parts.pop())
        snake_game_window.after(speed , move_snake)
    
    def change_direction(event):
        if event.keysym == 'Up' and direction != 'down':
            direction = 'up'
        elif event.keysym == 'Down' and direction != 'up':
            direction = 'down'
        elif event.keysym == 'Left' and direction != 'right':
            direction = 'left'
        elif event.keysym == 'Right' and direction != 'left':
            direction = 'right'
            
    snake_game_window.bind('<Up>', change_direction)
    snake_game_window.bind('<Down>', change_direction)
    snake_game_window.bind('<Left>', change_direction)
    snake_game_window.bind('<Right>', change_direction)
    
    move_snake()
    
    def close_snake_window():
        global snake_game_window
        snake_game_window
        snake_game_window.destroy()
        snake_game_window = None
        TempWindow.deiconify()
    
    snake_game_window.mainloop()
    
    
# def open_snake_window():
#     global snake_game_window
#     if snake_game_window is None or not snake_game_window.winfo_exists():  # 確保視窗不重複打開
#         TempWindow.withdraw()
#         snake_game_window = Toplevel()
#         snake_game_window.geometry('500x500')
#         snake_game_window.title('Snake_Game')

#         Game_width = 500
#         Game_height = 500
#         Board_size = 20  # 每個區塊的大小
#         speed = 100  # 蛇移動的速度

#         # Canvas 遊戲背景
#         canvas = Canvas(snake_game_window, width=Game_width, height=Game_height, bg='black')
#         canvas.pack()

#         # 蛇的初始參數
#         body_length = 3
#         snake_parts = []
#         direction = 'right'

#         # 初始蛇身
#         for i in range(body_length):
#             x = 100 - i * Board_size
#             y = 100
#             part = canvas.create_rectangle(x, y, x + Board_size, y + Board_size, fill='green', outline='')
#             snake_parts.append(part)

#         # 移動蛇的邏輯
#         def move_snake():
#             nonlocal direction
#             head_coords = canvas.coords(snake_parts[0])  # 獲取蛇頭座標
#             x1, y1, x2, y2 = head_coords

#             # 根據方向移動蛇頭
#             if direction == 'right':
#                 new_head = canvas.create_rectangle(x1 + Board_size, y1, x2 + Board_size, y2, fill='green', outline='')
#             elif direction == 'left':
#                 new_head = canvas.create_rectangle(x1 - Board_size, y1, x2 - Board_size, y2, fill='green', outline='')
#             elif direction == 'up':
#                 new_head = canvas.create_rectangle(x1, y1 - Board_size, x2, y2 - Board_size, fill='green', outline='')
#             elif direction == 'down':
#                 new_head = canvas.create_rectangle(x1, y1 + Board_size, x2, y2 + Board_size, fill='green', outline='')

#             # 加入新蛇頭並刪除蛇尾
#             snake_parts.insert(0, new_head)
#             canvas.delete(snake_parts.pop())

#             # 每次移動後持續調用自己
#             snake_game_window.after(speed, move_snake)

#         # 控制蛇方向
#         def change_direction(event):
#             nonlocal direction
#             if event.keysym == 'Up' and direction != 'down':
#                 direction = 'up'
#             elif event.keysym == 'Down' and direction != 'up':
#                 direction = 'down'
#             elif event.keysym == 'Left' and direction != 'right':
#                 direction = 'left'
#             elif event.keysym == 'Right' and direction != 'left':
#                 direction = 'right'

#         # 綁定鍵盤按鍵
#         snake_game_window.bind('<Up>', change_direction)
#         snake_game_window.bind('<Down>', change_direction)
#         snake_game_window.bind('<Left>', change_direction)
#         snake_game_window.bind('<Right>', change_direction)

#         # 開始移動蛇
#         move_snake()

#         # 關閉視窗並回到主視窗
#         def close_snake_window():
#             global snake_game_window
#             snake_game_window.destroy()
#             snake_game_window = None
#             TempWindow.deiconify()

#         snake_game_window.protocol("WM_DELETE_WINDOW", close_snake_window)
    


def open_draw_window():
    return 
    
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
btn_login = Button(frame, text="Log IN", font=("Arial", 12, "bold"), bg="#FF4500", fg="red", bd=0, cursor="hand2", command=login)
btn_login.pack(pady=10, fill="x", padx=20)

# 註冊按鈕
label_register = Label(frame, text="New to the system? ", font=("Arial", 10), bg="white", fg="#333")
label_register.pack(side="left", padx=50, pady=10)

btn_register = Button(frame, text="Register", font=("Arial", 10, "bold"), fg="#FF4500", bg="white", relief="flat", cursor="hand2", command=register)
btn_register.pack(side="right", padx=50)


root.mainloop()
