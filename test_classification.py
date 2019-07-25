import keras
from keras.models import Input, Model
from keras.layers import LSTM, SimpleRNN, Dense
from keras.utils import to_categorical
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy
import numpy as np
import time
import os
from process_data import processing_data
from keras.callbacks import TensorBoard

# load labels
data_dir = "../data_0717_miao/"
dir_list = os.listdir(data_dir)
dir_list = sorted(dir_list)
labels = []
for i in dir_list:
    if not i.startswith("."):
        labels.append(i)
print(labels)

# load data
data_x = None
data_y = None                                          
for label in labels:
    
    data_files = []
    data_file_list = os.listdir(os.path.join(data_dir, label))
    for i in data_file_list:
        if not i.startswith("."):
            data_files.append(i)


    for file_name in data_files:
        f = open(os.path.join(data_dir, label, file_name), "rb")
        temp_data = f.read()
        # print(file_name)
        # print(temp_data)
        temp_data = processing_data(temp_data).T
        temp_data = np.reshape(temp_data, [-1, 256,8])
        
        if data_x is None:
            data_x = temp_data
            data_y = np.ones([temp_data.shape[0], 1]) * int(label)
        else:
            data_x = np.concatenate([data_x, temp_data])
            data_y = np.concatenate([data_y, np.ones([temp_data.shape[0], 1]) * int(label)]) 

print(data_x.shape)
data_y = to_categorical(data_y, 7)
print(data_y.shape)

total_data_count = data_x.shape[0]
indexs = np.arange(total_data_count)
np.random.seed(10)
np.random.shuffle(indexs)
print(indexs)
data_x = data_x[indexs]
data_y = data_y[indexs]

# build rnn
input_layer = Input([256, 8])
# m = SimpleRNN(100)(input_layer)
m = LSTM(10)(input_layer)
m = Dense(7, activation = "softmax")(m)
model = Model(input_layer, m)

# training
optimizer = Adam(lr=3e-4)
model.compile(optimizer, categorical_crossentropy, metrics=["acc"])
tensorboard = TensorBoard()
model.fit(data_x, data_y, batch_size=128, epochs=200, validation_split=0.2, callbacks=[tensorboard])
