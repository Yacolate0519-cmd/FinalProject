import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# 1. 載入 MNIST 數據集
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. 數據預處理
# 將數據轉換為 3 通道 (ResNet 需要 RGB)，並將數值縮放到 [0, 1]
x_train = tf.image.grayscale_to_rgb(tf.expand_dims(x_train, axis=-1))
x_test = tf.image.grayscale_to_rgb(tf.expand_dims(x_test, axis=-1))

x_train = tf.image.resize(x_train, [224, 224]) / 255.0  # 調整為 224x224
x_test = tf.image.resize(x_test, [224, 224]) / 255.0

# 將標籤轉換為 one-hot 格式
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 3. 載入預訓練的 ResNet50 模型
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# 冻結預訓練模型的權重
base_model.trainable = False

# 4. 添加自定義分類層
model = models.Sequential([
    base_model,
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')  # MNIST 是 10 個類別
])

# 5. 編譯模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 6. 訓練模型
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5, batch_size=32)

# 7. 評估模型
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Test accuracy: {accuracy:.2f}')
model.save('Test.keras')