from PIL import Image
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt


model = load_model('Test.keras')

def preprocess_image(image_path):
    image = Image.open(image_path).convert('L')
    image = image.resize((28,28))
    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = img_array.reshape(1,28,28,1)
    return img_array

input_path = '5.png'
input_image = preprocess_image(input_path)
predictions = model.predict(input_image)
predict_label = np.argmax(predictions)

def plot_test_image(input_path,predicted_label):
    img = Image.open(input_path).convert('L').resize((28,28))
    plt.imshow(img,cmap='gray')
    plt.title(f'Predicted label:{predicted_label}')
    plt.axis('off')
    plt.show()
    
plot_test_image(input_path,predict_label)