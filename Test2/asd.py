import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    resized_image = image.resize((28, 28))  # Resize to 28x28
    img_array = np.array(resized_image) / 255.0  # Normalize to [0, 1]
    img_array = img_array.reshape(1, 28, 28, 1)  # Reshape for the model
    return image, resized_image, img_array

def display_images(original_image, resized_image):
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(original_image, cmap='gray')
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    axes[1].imshow(resized_image, cmap='gray')
    axes[1].set_title("Resized (28x28)")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()

# 使用文件路径测试
image_path = '0.png'  # 替换为你的图片路径
original_image, resized_image, img_array = preprocess_image(image_path)
display_images(original_image, resized_image)
