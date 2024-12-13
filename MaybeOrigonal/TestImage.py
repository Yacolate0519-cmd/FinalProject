import os 
import numpy as np
from tensorflow.keras.preprocessing.image import load_img , img_to_array
from tensorflow.keras.models import load_model

model = load_model('Test.keras')

test_image_dir ='Test_images/'

def preprocess_images(image_dir , target_size = (28,28)):
    images = []
    image_names = []
    for filename in os.listdir(image_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(image_dir, filename)
            img = load_img(filepath , color_mode = 'grayscale' , target_size = target_size).convert('L')
            img_array = img_to_array(img) / 255.0
            
            #Change Color
            # img_array = 255 - img_array
            
            img_array = np.expand_dims(img_array , axis = -1)
            images.append(img_array)
            image_names.append(filename)
    return np.array(images) , image_names

test_images , test_image_names = preprocess_images(test_image_dir)

predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions , axis = 1)

for name , label in zip(test_image_names , predicted_labels):
    print(f'圖片：{name}預測結果：{label}')