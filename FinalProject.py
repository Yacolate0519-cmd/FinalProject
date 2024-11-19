from tkinter import ttk
import tkinter as tk

if __name__ == '__main__':
    def update_preview(value = None):
        color_preview.config(bg = get_current_color())
    
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

    root = tk.Tk()
    root = root
    root.title("畫布")
    # root.geometry('700x400+1000+500')
    
    brush_size = tk.DoubleVar(value = 5)
    red = tk.IntVar(value = 0)
    green = tk.IntVar(value = 0)
    blue = tk.IntVar(value = 0)
    
    
    #畫布
    canvas = tk.Canvas(root , bg = 'white' , width = 800 , height = 800)
    canvas.grid(row = 0 , column = 0 , columnspan = 5 , pady = 10)
    #點擊左建開始繪畫
    canvas.bind("<B1-Motion>", paint)
    
    
    control_frame = tk.Frame(root)
    control_frame.grid(row = 1, column = 0 , rowspan = 3 , padx = 10)
    
    ttk.Label(control_frame , text = '紅色' , font = ('Arial' , 20 , 'bold')).grid(row = 1 , column = 0 , padx = 5)
    ttk.Scale(control_frame , from_ = 0 , to = 255 , variable = red  , orient = 'horizontal' , command = update_preview).grid(row = 1 , column = 1 , padx =5)
    
    ttk.Label(control_frame , text = '綠色' , font = ('Arial' , 20 , 'bold')).grid(row = 2 , column = 0 , padx = 5)
    ttk.Scale(control_frame , from_ = 0 , to = 255 , variable = green  , orient = 'horizontal' , command = update_preview).grid(row = 2 , column = 1 , padx = 5)
    
    ttk.Label(control_frame , text = '藍色' , font = ('Arial' , 20 , 'bold')).grid(row = 3 , column = 0 , padx = 5)
    ttk.Scale(control_frame , from_ = 0 , to = 255 , variable = blue  , orient = 'horizontal' , command = update_preview).grid(row = 3 , column = 1 , padx = 5)
    
    tk.Label(root , text = '顏色預覽' , font = ('Arial' , 20 , 'bold')).grid(row = 4 , column = 0 , padx = 5)
    
    color_preview = tk.Label(root , bg = get_current_color() , width = 20 , height = 10)
    color_preview.grid(row = 4 , column = 1 , pady = 5)
    
    clear_button = tk.Button(control_frame , text = '清除畫布' , command = clear_canvas , bg = 'red' , fg = 'white').grid(row = 5 , column = 0 , columnspan = 2 , pady = 10)
    update_preview()
    
    # app = Preview(root)
    root.mainloop()