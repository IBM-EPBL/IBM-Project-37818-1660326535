# -*- coding: utf-8 -*-
"""Test with Saved Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SvDVrBs4hdgJ05j6Sx1oa1CqAKuCSDcu
"""

from tensorflow.keras.models import load_model

model = load_model(r'C:\Users\ELCOT\Desktop\IBM\model Building(s2)\mnistCNN.h5')

from PIL import Image 
import numpy as np
for index in range(4):
  img = Image.open('C:/Users/ELCOT/Desktop/IBM/model Building(s2)/0.png')
  img = img.resize((28, 28))
  im2arr = np.array(img)
  im2arr = im2arr.reshape(1,28,28,1)
  y_pred = model.predict(im2arr)
  print(y_pred)