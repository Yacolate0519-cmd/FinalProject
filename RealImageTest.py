from PIL import Image
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

# 加載模型
model = load_model('Test.keras')

# 圖片預處理函數
def preprocess_image(image_path):
    image = Image.open(image_path).convert('L')
    image = image.resize((28, 28))
    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    return img_array

# 測試多張圖片
image_paths = [f'{i}.png' for i in range(10)]  # 假設有 0.png 到 9.png 的圖片
predicted_labels = []

# 預測每張圖片的標籤
for image_path in image_paths:
    input_image = preprocess_image(image_path)
    predictions = model.predict(input_image)
    predicted_label = np.argmax(predictions)
    predicted_labels.append(predicted_label)

# 繪製所有圖片到一張大圖
def plot_all_images(image_paths, predicted_labels):
    num_images = len(image_paths)
    cols = 5  # 每行顯示的圖片數量
    rows = (num_images + cols - 1) // cols  # 計算需要的行數
    
    fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
    axes = axes.flatten()  # 展平成一維數組，方便索引
    
    for i, (image_path, predicted_label) in enumerate(zip(image_paths, predicted_labels)):
        img = Image.open(image_path).convert('L').resize((28, 28))
        axes[i].imshow(img, cmap='gray')
        axes[i].set_title(f'Label: {predicted_label}', fontsize=10)
        axes[i].axis('off')
    
    # 隱藏多餘的子圖
    for ax in axes[len(image_paths):]:
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()

# 顯示結果
plot_all_images(image_paths, predicted_labels)
