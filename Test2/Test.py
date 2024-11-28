import tensorflow as tf
from keras import layers , models
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D , MaxPooling2D , Flatten , Dense , Dropout
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range = 10,
    width_shift_range = 0.1,
    height_shift_range = 0.1,
    zoom_range = 0.1,
    shear_range = 0.1
)

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = x_train.reshape(-1,28,28,1).astype('float32') / 255
x_test= x_test.reshape(-1,28,28,1).astype('float32') / 255
y_train = tf.keras.utils.to_categorical(y_train , 10)
y_test = tf.keras.utils.to_categorical(y_test , 10)


x_train = 1 - x_train
x_test = 1 - x_test

datagen.fit(x_train)

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
# model = models.Sequential([
#     layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
#     layers.Conv2D(64, (3, 3), activation='relu'),
#     layers.MaxPooling2D(pool_size=(2, 2)),
#     layers.Conv2D(128, (3, 3), activation='relu'),
#     layers.Conv2D(128, (3, 3), activation='relu'),
#     layers.MaxPooling2D(pool_size=(2, 2)),
#     layers.Flatten(),
#     layers.Dense(256, activation='relu'),
#     layers.Dropout(0.5),
#     layers.Dense(10, activation='softmax')
# ])

#修改二
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.BatchNormalization(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Dropout(0.25),
    
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Dropout(0.5),
    
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

optimizer = Adam(learning_rate = 0.001)
model.compile(loss = 'categorical_crossentropy' , optimizer = 'adam' , metrics = ['accuracy'])

early_stopping = EarlyStopping(monitor = 'val_loss' , patience = 5 , verbose = 1)
history = model.fit(x_train , y_train , batch_size =64 , epochs = 30 , validation_data = (x_test , y_test) , callbacks = [early_stopping])

test_loss , test_accuracy = model.evaluate(x_test , y_test)
print(f'測試集損失:{test_loss:.4f},測試集準確率:{test_accuracy:.4f}')

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Train' , 'Test'] , loc = 'upper left')
plt.show()

model.save("Test.keras")
