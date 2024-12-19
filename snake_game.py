import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        # 遊戲視窗設定
        self.root = root
        self.root.title("貪吃蛇遊戲")
        self.width = 500
        self.height = 500
        self.board_size = 20  # 每個格子的大小
        self.speed = 100  # 蛇移動的速度 (數值越小越快)
        self.score = 0

        # 畫布
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        # 遊戲變數
        self.direction = "Right"  # 初始方向
        self.snake = []
        self.food = None

        # 初始化蛇和食物
        self.init_snake()
        self.create_food()

        # 分數顯示
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14), bg="black", fg="white")
        self.score_label.place(x=10, y=10)

        # 綁定鍵盤事件
        self.root.bind("<KeyPress>", self.change_direction)

        # 初始化 Restart 按鈕並隱藏
        self.restart_button = tk.Button(
            self.root, 
            text="Restart", 
            font=("Arial", 14), 
            command=self.restart_game, 
            bg="white"
        )
        self.restart_button.place(x=self.width / 2 - 40, y=self.height / 2 + 20)
        self.restart_button.place_forget()  # 隱藏按鈕

        # 開始遊戲
        self.move_snake()

    def init_snake(self):
        """ 初始化蛇的身體 """
        self.snake = [
            self.canvas.create_rectangle(100, 100, 100 + self.board_size, 100 + self.board_size, fill="green")
        ]
        self.snake.append(
            self.canvas.create_rectangle(80, 100, 80 + self.board_size, 100 + self.board_size, fill="green")
        )
        self.snake.append(
            self.canvas.create_rectangle(60, 100, 60 + self.board_size, 100 + self.board_size, fill="green")
        )

    def create_food(self):
        """ 在隨機位置產生食物 """
        x = random.randint(0, (self.width // self.board_size) - 1) * self.board_size
        y = random.randint(0, (self.height // self.board_size) - 1) * self.board_size
        if self.food:
            self.canvas.delete(self.food)
        self.food = self.canvas.create_oval(x, y, x + self.board_size, y + self.board_size, fill="red")

    def change_direction(self, event):
        """ 改變蛇的方向 """
        new_direction = event.keysym
        if new_direction == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif new_direction == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif new_direction == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif new_direction == "Right" and self.direction != "Left":
            self.direction = "Right"

    def move_snake(self):
        """ 移動蛇的邏輯 """
        head_coords = self.canvas.coords(self.snake[0])
        x1, y1, x2, y2 = head_coords

        # 根據方向計算新蛇頭的位置
        if self.direction == "Right":
            new_head_coords = (x1 + self.board_size, y1, x2 + self.board_size, y2)
        elif self.direction == "Left":
            new_head_coords = (x1 - self.board_size, y1, x2 - self.board_size, y2)
        elif self.direction == "Up":
            new_head_coords = (x1, y1 - self.board_size, x2, y2 - self.board_size)
        elif self.direction == "Down":
            new_head_coords = (x1, y1 + self.board_size, x2, y2 + self.board_size)

        # 檢查是否碰到邊界或自己
        def check_collision(self, head_coords):
            x1, y1, x2, y2 = head_coords
            # 檢查邊界
            if x1 < 0 or y1 < 0 or x2 > self.width or y2 > self.height:
                return True
            # 檢查蛇頭是否撞到自己（即蛇頭是否與蛇的身體重疊）
            for part in self.snake[1:]:  # 排除蛇頭自身
                if self.canvas.coords(part) == head_coords:
                    return True
            return False


        # 創建新蛇頭並加入蛇的身體
        new_head = self.canvas.create_rectangle(*new_head_coords, fill="green")
        self.snake.insert(0, new_head)

        # 檢查是否吃到食物
        if self.check_food(new_head_coords):
            self.create_food()
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
        else:
            # 刪除蛇尾
            tail = self.snake.pop()
            self.canvas.delete(tail)

        # 設定下一次移動
        self.root.after(self.speed, self.move_snake)

    def check_collision(self, head_coords):
        """ 檢查蛇是否撞到邊界或自己 """
        x1, y1, x2, y2 = head_coords
        # 檢查邊界
        if x1 < 0 or y1 < 0 or x2 > self.width or y2 > self.height:
            return True
        # 檢查蛇頭是否撞到自己
        for part in self.snake[1:]:
            if self.canvas.coords(part) == head_coords:
                return True
        return False

    def check_food(self, head_coords):
        """ 檢查蛇是否吃到食物 """
        food_coords = self.canvas.bbox(self.food)
        head_x1 , head_y1 , head_x2 , head_y2 = head_coords
        food_x1 , food_y1 , food_x2 , food_y2 = food_coords

        return (head_x1 < food_x2 and head_x2 > food_x1 and head_y1 < food_y2 and head_y2 > food_y1)

    def game_over(self):
        """ 遊戲結束時顯示訊息 """
        self.canvas.create_text(
            self.width / 2, self.height / 2 - 20,
            text=f"Game Over\nYour Score: {self.score}",
            fill="white", font=("Arial", 20, "bold")
        )

        # 顯示 Restart 按鈕
        self.restart_button.place(x=self.width / 2 - 40, y=self.height / 2 + 20)

    def restart_game(self):
        """ 重置遊戲狀態並重新開始 """
        self.canvas.delete("all")
        self.score = 0
        self.direction = "Right"
        self.snake = []
        self.food = None

        self.score_label.config(text=f"Score: {self.score}")
        self.init_snake()
        self.create_food()
        self.move_snake()
        # 隱藏 Restart 按鈕
        self.restart_button.place_forget()

# 遊戲啟動
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
