import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import kagglehub
from PIL import ImageOps

# 下載數據集
path = kagglehub.dataset_download("sachinpatel21/az-handwritten-alphabets-in-csv-format")
csv_files = os.path.join(path, 'A_Z Handwritten Data.csv')

# 讀取CSV文件
data = pd.read_csv(csv_files)

# 檢查列名
print("Columns in data:", data.columns)

import pandas as pd

# 讀取CSV文件
data = pd.read_csv(csv_files)

# 確定標籤列名（假設是 0，請根據實際情況調整）
label_column = '0'

# 計算每個字母的數量分佈
letter_counts = data[label_column].value_counts()

# 顯示每個字母的樣本數量
print("Letter counts:")
print(letter_counts)

# 繪製字母數量的條形圖
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
letter_counts.sort_index().plot(kind='bar', color='skyblue')
plt.title("Distribution of Handwritten Alphabet Samples")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.xticks(ticks=range(26), labels=[chr(65 + i) for i in range(26)], rotation=45)
plt.show()



'''
# 假設第一列是標籤，並檢查列名，通常第一列可能是 '0' 或其他名稱，這取決於CSV文件的格式
# 如果標籤列是 '0'，改為使用 '0'，否則請根據顯示的列名選擇適當的列名。
label_column = '0'  # 假設標籤列是 '0'，若列名不同，請修改

# 篩選出字母 Y (label = 24) 的數據
y_data = data[data[label_column] == 24]

# 設定顯示的圖片數量
n = 5
fig, axes = plt.subplots(1, n, figsize=(15, 5))

for i in range(n):
    random_index = random.randint(0, len(y_data) - 1)
    random_sample = y_data.iloc[random_index]
    
    label = random_sample[label_column]
    pixels = random_sample[1:]
    
    # 重塑為28x28的圖像
    image = pixels.values.reshape(28, 28)
    image = 255 - image  # 反轉顏色以適應視覺習慣
    
    # 顯示圖片
    axes[i].imshow(image, cmap='gray')
    axes[i].set_title(f'Label: {chr(65 + label)}')
    axes[i].axis('off')

# 顯示結果
plt.tight_layout()
plt.show()
'''