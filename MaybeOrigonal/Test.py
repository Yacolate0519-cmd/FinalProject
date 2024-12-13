import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D , MaxPooling2D , Flatten , Dense

(x_train , y_train) , (x_test , y_test) = mnist.load_data()

x_train = x_train.antype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

x_train = np.expand_dims(x_train , axis = -1)
x_test = np.expend_dims(x_test , axis = -1)

y_train = to_categorical(y_train , num_classes = 10)
y_test = to_categorical(y_test , num_classes = 10)

model = Sequential([
    Conv2D(6, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # 第一個卷積層
    MaxPooling2D(pool_size=(2, 2)),                                # 第一個池化層
    Conv2D(16, (3, 3), activation='relu'),                        # 第二個卷積層
    MaxPooling2D(pool_size=(2, 2)),                                # 第二個池化層
    Flatten(),                                                    # 展平層
    Dense(120, activation='relu'),                                # 全連接層 1
    Dense(84, activation='relu'),                                 # 全連接層 2
    Dense(10, activation='softmax')                               # 輸出層
])

model.comile(optimize = 'adam',
             loss = 'categorical_crossentropy',
             metrics = ['accuracy'])

model.fit(x_train , y_train,
          epoch = 10,
          batch_size = 32,
          validation_data = (x_test , y_test))

loss , accuracy = model.evaluate(x_test , y_test)
print(f'Test Loss:{loss:.4f} , Test Accuracy : {accuracy:.4f}')
