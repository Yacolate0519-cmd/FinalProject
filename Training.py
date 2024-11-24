import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
from tensorflow.python import keras
from keras import layers
from random import sample


print(tf.config.list_physical_devices("GPU"))


fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (valid_images, valid_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0
valid_images = valid_images / 255.0


i = random.randint(0, 10000)
data_idx = i


number_of_classes = train_labels.max() + 1
print(f"Number of classes: {number_of_classes}")


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), 
    tf.keras.layers.Dense(128, activation='relu'),  
    tf.keras.layers.Dropout(0.2), 
    tf.keras.layers.Dense(number_of_classes)
])


model.summary()


model.compile(optimizer='adam', 
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
              metrics=['accuracy'])

#早停回調
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

#增加模型精準度
history = model.fit(train_images, train_labels, epochs=50, verbose=True, validation_data=(valid_images, valid_labels), callbacks=[early_stopping])  # 增加epochs


predictions = model.predict(train_images[0:10])


print('Correct answer:', train_labels[data_idx])


plt.subplot(2,2,1)
plt.title('Clothing')
plt.imshow(train_images[data_idx], cmap='gray')
plt.colorbar()
plt.grid(False)


plt.subplot(2,2,2)
x_values = range(number_of_classes)
plt.bar(x_values, model.predict(train_images[data_idx:data_idx + 1]).flatten())
plt.xticks(range(10))
plt.title("Analyse data")


plt.subplot(2,2,3)
plt.plot(history.history['loss'], label='training loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()


plt.subplot(2,2,4)
plt.plot(history.history['accuracy'], label='training accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.suptitle("Yacolate's AI image trainging")
plt.show()