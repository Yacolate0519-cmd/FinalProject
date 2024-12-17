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
    root.withdraw()
    TempWindow = Toplevel(root)
    TempWindow.title('TempWindow')
    TempWindow.geometry('500x400')
    btn = Button(TempWindow , text = 'close' , command = lambda : closeWindow(TempWindow)).pack()
    
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
    
    
# 建立視窗
root = Tk()
root.title("Sign in to your account")
root.geometry("500x400")

# 背景
gradient = Canvas(root, width=500, height=400)
gradient.pack(fill="both", expand=True)
gradient.create_rectangle(0, 0, 500, 400, fill="#FFEFDB", outline="")  # 淺色背景
gradient.create_rectangle(0, 300, 500, 400, fill="#FFA07A", outline="")  # 淺橙漸變底部

# 主要框架
frame = Frame(gradient, bg="white", bd=2, relief="flat")
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
btn_login = Button(frame, text="SIGN IN", font=("Arial", 12, "bold"), bg="#FF4500", fg="white", bd=0, cursor="hand2", command=login)
btn_login.pack(pady=10, fill="x", padx=20)

# 註冊按鈕
label_register = Label(frame, text="New to the system? ", font=("Arial", 10), bg="white", fg="#333")
label_register.pack(side="left", padx=50, pady=10)

btn_register = Button(frame, text="Register", font=("Arial", 10, "bold"), fg="#FF4500", bg="white", relief="flat", cursor="hand2", command=register)
btn_register.pack(side="right", padx=50)


root.mainloop()
