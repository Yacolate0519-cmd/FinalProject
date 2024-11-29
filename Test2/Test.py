import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
import matplotlib.pyplot as plt
# 將資料做一個歸一化的動作
def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32) / 255.
    x = tf.reshape(x,[28,28,1])
    y = tf.cast(y, dtype=tf.int32)
    return x, y

batchs = 32

# 載入mnist 資料集 60000張訓練資料 , 10000張測試資料, 每張大小為 28x28
(train_Data, train_Label), (test_Data, test_Label) = mnist.load_data()
# 將訓練集資料打散
db = tf.data.Dataset.from_tensor_slices((train_Data, train_Label))
db = db.map(preprocess).shuffle(10000).batch(batchs)

db_test = tf.data.Dataset.from_tensor_slices((test_Data, test_Label))
db_test = db_test.map(preprocess).batch(batchs)

LeNet5Model = Sequential([
    # 第一個卷積層，6個 5x5 卷積核,激勵函數為 relu
    Conv2D(6,kernel_size=5,strides=1,padding='same',activation='relu'),
    # 池化層大小 2x2, 步長 2
    MaxPooling2D(pool_size=2,strides=2),
    # 第二個卷積層，16個 5x5 卷積核, 步長為 1
    Conv2D(16,kernel_size=5,strides=1,padding='same',activation='relu'),
    # 池化層大小 2x2, 步長 2
    MaxPooling2D(pool_size=2,strides=2),
    # 打平層，方便全連接層處理
    Flatten(),
    # 全連接層，120 個節點, 激勵函數為 relu
    Dense(120, activation='relu'),
    # 全連接層，84 個節點, 激勵函數為 relu
    Dense(84, activation='relu'),
    # 全連接層(輸出)，10 個節點, 最後以機率方式呈現
    Dense(10,activation='softmax')
])

# 指定輸入數據維度
LeNet5Model.build(input_shape=(None, 28, 28, 1))
# 顯示參數量
print(LeNet5Model.summary())


# 設定優化器
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
# 配置模型  # label 為數字編碼
LeNet5Model.compile(optimizer=optimizer,
                    loss='sparse_categorical_crossentropy',  # 指定損失函數
                    metrics=['accuracy'])
# 訓練模型
hist = LeNet5Model.fit(db,epochs=5, validation_data=db_test)

val_acc = hist.history['val_accuracy']
acc = hist.history['accuracy']
val_loss = hist.history['val_loss']
loss = hist.history['loss']

plt.plot(np.arange(len(val_loss)),val_loss,label='val_loss')
plt.plot(np.arange(len(loss)),loss,label='loss')
plt.ylim(0.1,0.8)
plt.xlabel('EPOCHS')
plt.ylabel('LOSS')
plt.legend()
plt.grid()
plt.show()

plt.plot(np.arange(len(val_acc)),val_acc,label='val_acc')
plt.plot(np.arange(len(acc)),acc,label='acc')
plt.ylim(0.1,1.0)
plt.xlabel('EPOCHS')
plt.ylabel('ACC')
plt.legend()
plt.grid()
plt.show()