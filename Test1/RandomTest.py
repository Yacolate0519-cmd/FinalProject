import tensorflow as tf
from keras import layers , models
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D , MaxPooling2D , Flatten , Dense , Dropout
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import random
import numpy as np

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = x_train.reshape(-1,28,28,1).astype('float32') / 255
x_test= x_test.reshape(-1,28,28,1).astype('float32') / 255
y_train = tf.keras.utils.to_categorical(y_train , 10)
y_test = tf.keras.utils.to_categorical(y_test , 10)

x_train = 1 - x_train
x_test = 1 - x_test
# y_train = 1 - y_train
# y_test = 1 - y_test


# # 从训练集中随机抽取一笔数据
# random_index = random.randint(0, x_train.shape[0] - 1)  # 随机索引
# random_image = x_train[random_index]  # 获取随机图像
# random_label = np.argmax(y_train[random_index])  # 获取图像对应的标签

# # 打印图像和标签
# plt.imshow(random_image.reshape(28, 28), cmap='gray')  # 显示图像
# plt.title(f"Label: {random_label}")  # 显示标签
# plt.axis('off')
# plt.show()

# # 取索引，抽取图片和标签
# random_index = random.randint(0, x_train.shape[0] - 1)
# random_image = x_train[random_index]
# random_label = np.argmax(y_train[random_index])

# # 打印图像对应的标签
# print(f"Index: {random_index}, Label: {random_label}")

for i in range(20):
    print(f"Image {i}: Label: {np.argmax(y_train[i])}")
    plt.subplot(5,4,1+i)
    plt.imshow(x_train[i].reshape(28, 28), cmap='gray')
    plt.title(f"Label: {np.argmax(y_train[i])}")
    plt.axis('off')

plt.show()

# import matplotlib.pyplot as plt
# from keras.datasets import mnist

# # 加载 MNIST 数据集
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# # 随机查看前 10 张图片
# for i in range(10):
#     plt.subplot(2, 5, i + 1)  # 创建一个 2x5 的子图
#     plt.imshow(x_train[i], cmap='gray')  # 显示图像
#     plt.title(f"Label: {y_train[i]}")  # 显示标签
#     plt.axis('off')  # 不显示坐标轴

# plt.tight_layout()
# plt.show()
