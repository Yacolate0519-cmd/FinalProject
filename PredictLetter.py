from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

model = load_model('mymodel.keras')

def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')
    img = img.resize((28,28))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1,28,28,1)
    return img_array

image_path = 'A.png'

input_image = preprocess_image(image_path)
predictions = model.predict(input_image)
predicted_label = np.argmax(predictions)

alphabet = [chr(i) for i in range(65,91)]
predicted_letter = alphabet[predicted_label]

print(f'Predict model letter: {predicted_letter}')

plt.title(f'Predicted Letter: {predicted_letter}')
img = Image.open(image_path).convert('L')
plt.imshow(img , cmap = 'gray')
plt.show()
