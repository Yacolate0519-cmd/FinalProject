import tensorflow as tf
from keras import layers , models
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D , MaxPooling2D , Flatten , Dense , Dropout
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = x_train.reshape(-1,28,28,1).astype('float32') / 255
x_test= x_test.reshape(-1,28,28,1).astype('float32') / 255
y_train = tf.keras.utils.to_categorical(y_train , 10)
y_test = tf.keras.utils.to_categorical(y_test , 10)

x_train = 1 - x_train
x_test = 1 - x_test

#原始模型
# model = models.Sequential([
#     layers.Conv2D(32,(3,3) , activation = 'relu' , input_shape = (28,28,1)),
#     layers.MaxPooling2D(pool_size = (2 , 2)),
#     layers.Conv2D(64,(3,3) , activation = 'relu'),
#     layers.MaxPooling2D(pool_size = (2 , 2)),
#     layers.Flatten(),
#     layers.Dense(128,activation = 'relu'),
#     layers.Dropout(0.5),
#     layers.Dense(10,activation = "softmax")
# ])

#修改一
model = models.Sequential([
    layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])


model.compile(loss = 'categorical_crossentropy' , optimizer = 'adam' , metrics = ['accuracy'])

early_stopping = EarlyStopping(monitor = 'val_loss' , patience = 5 , verbose = 1)
history = model.fit(x_train , y_train , batch_size =64 , epochs = 30 , validation_split = 0.2 , callbacks = [early_stopping])

test_loss , test_accuracy = model.evaluate(x_test , y_test)
val_loss = history.history['val_loss'][-1]
print(f'最後一個驗證集的損失:{val_loss}')

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Train' , 'Test'] , loc = 'upper left')
plt.show()

model.save("Test.keras")
