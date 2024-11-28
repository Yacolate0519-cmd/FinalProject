from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    image = Image.open(image_path).convert('L')
    image = image.resize((28, 28))
    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    return img_array

# 多張圖片路徑
image_paths = ['1.png','2.png','6.png','0.png','9.png']  # 替換為你的實際圖片路徑

# 設置子圖的行列數
num_images = len(image_paths)
cols = 3  # 每行顯示的圖片數
rows = (num_images + cols - 1) // cols  # 自動計算行數

# 創建圖形
fig, axes = plt.subplots(rows, cols, figsize=(15, 5))
axes = axes.flatten()  # 展平成一維列表，方便迭代

# 遍歷圖片並繪製
for i, image_path in enumerate(image_paths):
    img = Image.open(image_path).convert('L').resize((28, 28))  # 預處理圖片
    axes[i].imshow(img, cmap='gray')  # 顯示圖片
    axes[i].set_title(f"Image {i+1}")  # 添加標題
    axes[i].axis('off')  # 關閉座標軸

# 隱藏多餘的子圖框架
for ax in axes[num_images:]:
    ax.axis('off')

# 顯示圖片
plt.tight_layout()
plt.show()