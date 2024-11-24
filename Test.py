import tensorflow as tf

# 检查是否有可用的 GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"Num GPUs Available: {len(gpus)}")
else:
    print("No GPUs detected.")
