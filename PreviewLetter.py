import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import kagglehub
from PIL import ImageOps

path = kagglehub.dataset_download("sachinpatel21/az-handwritten-alphabets-in-csv-format")
csv_files = os.path.join(path, 'A_Z Handwritten Data.csv')

data = pd.read_csv(csv_files)
n = 5
fig , axes = plt.subplots(1 , n , figsize = (15 , 5))
for i in range(n):
    random_index = random.randint(0 , len(data) - 1)
    random_sample = data.iloc[random_index]
    
    label = random_sample[0]
    pixels = random_sample[1:]
    
    image = pixels.values.reshape(28,28)
    image = 255 - image
    
    axes[i].imshow(image , cmap = 'gray')
    axes[i].set_title(f'Label: {chr(65 + label)}')
    axes[i].axis('off')
    
plt.tight_layout()
plt.show()