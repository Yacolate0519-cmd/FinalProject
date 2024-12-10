from PIL import Image
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

# Load the model
model = load_model('Test.keras')

# Function to preprocess a single image
def preprocess_image(image_path):
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to 28x28
    img_array = np.array(image) / 255.0  # Normalize to [0, 1]
    img_array = img_array.reshape(1, 28, 28, 1)  # Reshape for the model
    return img_array

# Paths to input images
input_paths = ['mypic.png']

# Preprocess all images and predict
predictions = []
for image_path in input_paths:
    input_image = preprocess_image(image_path)
    pred = model.predict(input_image)
    predictions.append(np.argmax(pred))

# Display images and predictions
num_images = len(input_paths)
cols = 3
rows = (num_images + cols - 1) // cols  # Determine rows dynamically

fig, axes = plt.subplots(rows, cols, figsize=(15, 5))
axes = axes.flatten()

for i, image_path in enumerate(input_paths):
    img = Image.open(image_path).convert('L').resize((28, 28))
    axes[i].imshow(img, cmap='gray')
    axes[i].set_title(f"Image {i + 1}\nPredicted: {predictions[i]}")
    axes[i].axis('off')

# Turn off any extra axes
for ax in axes[num_images:]:
    ax.axis('off')

plt.tight_layout()
plt.show()
