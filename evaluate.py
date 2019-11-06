import keras
from keras.models import Input, Model
from keras.layers import LSTM, SimpleRNN, Dense, GRU
from keras.utils import to_categorical
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy
import numpy as np
import time
import os
import cv2
from process_data import processing_data
from keras.callbacks import TensorBoard, ModelCheckpoint

# model path
model_path = "/home/wsn/Desktop/HAR/result/major_experiment/SimpleRNN_128/weights.197-0.9599.hdf5"

# load data
data_x = np.load("/home/wsn/Desktop/HAR/HGR_dataset/data_x_64.npy")
data_y = np.load("/home/wsn/Desktop/HAR/HGR_dataset/data_y_64.npy")

print(data_x.shape)
# data_x = cv2.blur(data_x, (128, 1))
print(data_y.shape)

# total_data_count = data_x.shape[0]
# indexs = np.arange(total_data_count)
# np.random.seed(10)
# np.random.shuffle(indexs)
# print(indexs)
# data_x = data_x[indexs]
# data_y = data_y[indexs]

# # divide dataset
# training_data_x = data_x[:int(len(data_x) * 0.8)]
# val_data_x = data_x[int(len(data_x) * 0.8):int(len(data_x) * 0.9)]
# test_data_x = data_x[int(len(data_x) * 0.9):]

# training_data_y = data_y[:int(len(data_y) * 0.8)]
# val_data_y = data_y[int(len(data_y) * 0.8):int(len(data_y) * 0.9)]
# test_data_y = data_y[int(len(data_y) * 0.9):]

# build rnn model
input_layer = Input([128, 8])
m = SimpleRNN(128)(input_layer)
# m = LSTM(128)(input_layer)
# m = GRU(128)(input_layer)
m = Dense(7, activation = "softmax")(m)
model = Model(input_layer, m)

# testing
optimizer = Adam(lr=1e-4)
model.compile(optimizer, categorical_crossentropy, metrics=["acc"])
# model.load_weights(model_path)

# result = model.predict(data_x)
# for i in range(len(result)):
#     if np.argmax(result[i]) != np.argmax(data_y[i]):
#         print(np.argmax(result[i]), np.argmax(data_y[i]))


# # start_time = time.time()
# # model.predict(test_data_x[0:1,:,:])
# # print("Time cost:", time.time() - start_time)
# print(model.evaluate(data_x, data_y))

print(model.summary())