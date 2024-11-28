from tkinter import ttk
import tkinter as tk
from tkinter import *
from PIL import Image , ImageGrab

def get_current_color():
        return f'#{red.get():02x}{green.get():02x}{blue.get():02x}'
    
def update_preview(*args):
    color_preview.config(bg = get_current_color())

def paint(event):
    x1,y1 = (event.x - brush_size.get()),(event.y - brush_size.get())
    x2,y2 = (event.x - brush_size.get()),(event.y - brush_size.get())
    color = get_current_color()
    canvas.create_oval(x1,y1,x2,y2,fill = color , outline = color)

def clear_canvas():
    canvas.delete('all')
    
def capture():
    x0 = canvas.winfo_rootx()
    y0 = canvas.winfo_rooty()
    x1 = x0 + canvas.winfo_width()
    y1 = y0 + canvas.winfo_height()
    
    im = ImageGrab.grab((x0,y0,x1,y1))
    im.save('mypic.png')

if __name__ == '__main__':
    # def update_preview(value = None):
    #     color_preview.config(bg = get_current_color())

    root = Tk()
    root = root
    root.title("畫布")
    # root.grid_propagate(False)
    # root.geometry('700x400+1000+500')
    
    brush_size = tk.DoubleVar(value = 5)
    red = IntVar(value = 0)
    green = IntVar(value = 0)
    blue = IntVar(value = 0)
    
    
    #畫布
    
    canvas = Canvas(root , bg = 'white' , width = 800 , height = 800)
    canvas.grid(row = 0 , column = 0 , columnspan = 5 , pady = 10)
    
    #因為在macos上結果不如預期，所以直接指定畫布大小
    canvas.config(width = 800 , height = 500)
    
    #點擊左建開始繪畫
    canvas.bind("<B1-Motion>", paint)
    
    
    control_frame = tk.Frame(root)
    control_frame.grid(row = 1, column = 0 , rowspan = 3 , padx = 10)
    
    Label(control_frame , text = '紅色' , font = ('Arial' , 20 , 'bold')).grid(row = 1 , column = 0 , padx = 5)
    Scale(control_frame , from_ = 0 , to = 255 , variable = red  , orient = 'horizontal' , command = update_preview).grid(row = 1 , column = 1 , padx =5)
    
    Label(control_frame , text = '綠色' , font = ('Arial' , 20 , 'bold')).grid(row = 2 , column = 0 , padx = 5)
    Scale(control_frame , from_ = 0 , to = 255 , variable = green  , orient = 'horizontal' , command = update_preview).grid(row = 2 , column = 1 , padx = 5)
    
    Label(control_frame , text = '藍色' , font = ('Arial' , 20 , 'bold')).grid(row = 3 , column = 0 , padx = 5)
    Scale(control_frame , from_ = 0 , to = 255 , variable = blue  , orient = 'horizontal' , command = update_preview).grid(row = 3 , column = 1 , padx = 5)
    
    Label(root , text = '顏色預覽' , font = ('Arial' , 20 , 'bold')).grid(row = 4 , column = 0 , padx = 5)
    
    color_preview = Label(root , bg = get_current_color() , width = 20 , height = 10)
    color_preview.grid(row = 4 , column = 1 , pady = 5)
    
    clear_button = Button(control_frame , text = '清除畫布' , command = clear_canvas , bg = 'red' , fg = 'white').grid(row = 5 , column = 0 , columnspan = 2 , pady = 10)
    
    predict_button = Button(root , text = 'Predict' , command = capture).grid()
    
    update_preview()
    
    # app = Preview(root)
    root.mainloop()