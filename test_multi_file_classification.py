import keras
from keras.models import Input, Model
from keras.layers import LSTM, SimpleRNN, Dense, GRU, RNN
from keras.utils import to_categorical
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy
import numpy as np
import time
import os
import cv2
from process_data import processing_data
from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau


data_x = np.load("../HGR_dataset/data_x_128.npy")
data_y = np.load("../HGR_dataset/data_y_128.npy")

print(data_x.shape)
# data_x = cv2.blur(data_x, (128, 1))
print(data_y.shape)

total_data_count = data_x.shape[0]
indexs = np.arange(total_data_count)
np.random.seed(10)
np.random.shuffle(indexs)
print(indexs)
data_x = data_x[indexs]
data_y = data_y[indexs]

# divide dataset
training_data_x = data_x[:int(len(data_x) * 0.8)]
val_data_x = data_x[int(len(data_x) * 0.8):int(len(data_x) * 0.9)]
test_data_x = data_x[int(len(data_x) * 0.9):]

training_data_y = data_y[:int(len(data_y) * 0.8)]
val_data_y = data_y[int(len(data_y) * 0.8):int(len(data_y) * 0.9)]
test_data_y = data_y[int(len(data_y) * 0.9):]

# build rnn model
input_layer = Input([128, 8])
# m = SimpleRNN(128)(input_layer)
m = LSTM(128)(input_layer)
# m = GRU(128)(input_layer)
m = Dense(7, activation = "softmax")(m)
model = Model(input_layer, m)

# training
optimizer = Adam(lr=1e-4)
model.compile(optimizer, categorical_crossentropy, metrics=["acc"])
tensorboard = TensorBoard()
lr_reduce = ReduceLROnPlateau("val_acc", verbose=1, factor=0.2, patience=5, min_lr=1e-6)
model_check_point = ModelCheckpoint("./snapshot/weights.{epoch:02d}-{val_acc:.4f}.hdf5", monitor="val_acc", verbose=1, save_best_only=True)
model.fit(training_data_x, training_data_y, batch_size=512, epochs=200, validation_data=[val_data_x, val_data_y], callbacks=[tensorboard, model_check_point, lr_reduce])
