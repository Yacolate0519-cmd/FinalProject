from numpy import load
import pandas as pd
import kagglehub
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

import os

# Download latest version
path = kagglehub.dataset_download("sachinpatel21/az-handwritten-alphabets-in-csv-format")

dataset_path = "sachinpatel21/az-handwritten-alphabets-in-csv-format"

print('Files in dataset directory:')
print(os.listdir(path))

csv_files = os.path.join(path, 'A_Z Handwritten Data.csv')
data = pd.read_csv(csv_files)

labels = data['0']
pixels = data.iloc[: , 1 :]

images = pixels.to_numpy().reshape(-1,28,28,1)

# print("Images shape: ", images.shape)
# print('Labels shape: ', labels.shape)

images = images / 255.0

x_train , x_test , y_train , y_test = train_test_split(images , labels , test_size = 0.2 , random_state = 42)

# print("training data shape: ", x_train.shape,y_train.shape)
# print('testing data shape: ',x_test.shape,y_test.shape)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(26, activation='softmax')  # 26 個字母分類
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
print(model.summary())