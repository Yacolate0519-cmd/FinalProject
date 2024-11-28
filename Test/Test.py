from keras.datasets import mnist
from keras.utils import np_utils
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)

# Load MNIST data
(X_Train, y_Train), (X_Test, y_Test) = mnist.load_data()

# Data preprocessing
X_Train4D = X_Train.reshape(X_Train.shape[0], 28, 28, 1).astype('float32')
X_Test4D = X_Test.reshape(X_Test.shape[0], 28, 28, 1).astype('float32')

X_Train4D_norm = X_Train4D / 255.0
X_Test4D_norm = X_Test4D / 255.0

y_TrainOneHot = np_utils.to_categorical(y_Train, 10)
y_TestOneHot = np_utils.to_categorical(y_Test, 10)

# Build model
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(5,5), padding='same', input_shape=(28,28,1), activation='relu', name='conv2d_1'))
model.add(MaxPool2D(pool_size=(2,2), name='max_pooling2d_1'))

model.add(Conv2D(filters=36, kernel_size=(5,5), padding='same', activation='relu', name='conv2d_2'))
model.add(MaxPool2D(pool_size=(2,2), name='max_pooling2d_2'))
model.add(Dropout(0.25, name='dropout_1'))
model.add(Flatten(name='flatten_1'))
model.add(Dense(128, activation='relu', name='dense_1'))
model.add(Dropout(0.5, name='dropout_2'))
model.add(Dense(10, activation='softmax', name='dense_2'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
train_history = model.fit(x=X_Train4D_norm,
                          y=y_TrainOneHot,
                          validation_split=0.2,
                          epochs=10,
                          batch_size=300,
                          verbose=1)

# Evaluate model
scores = model.evaluate(X_Test4D_norm, y_TestOneHot, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

model.save('result.keras')

# Visualization functions
def plot_image(image):
    plt.imshow(image.reshape(28,28), cmap='binary')
    plt.show()

def plot_images_labels_predict(images, labels, prediction, idx, num=10):
    if num > 25: num = 25
    for i in range(0, num):
        ax = plt.subplot(5,5, 1+i)
        ax.imshow(images[idx].reshape(28,28), cmap='binary')
        title = f'l={labels[idx]}'
        if len(prediction) > 0:
            title += f', p={prediction[idx]}'
        ax.set_title(title, fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
        idx += 1
    plt.show()

def show_train_history(train_history, train, validation):
    x = np.linspace(0,8,100)
    y = [0.99]*100
    plt.plot(x,y)
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.xlabel('Epoch')
    plt.ylabel(train)
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

# Show training history
show_train_history(train_history, 'accuracy', 'val_accuracy')
show_train_history(train_history, 'loss', 'val_loss')

# Make predictions
prediction = model.predict(X_Test4D_norm)

# Display some results
plot_images_labels_predict(X_Test, y_Test, prediction.argmax(axis=1), idx=0, num=10)
