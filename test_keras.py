import keras
from keras.models import Input, Model
from keras.layers import LSTM, SimpleRNN, Dense
from keras.utils import to_categorical
import numpy as np
import time

train_x = np.random.uniform(size=[1000,128,8])
train_y = np.random.randint(0, 6, [1000, 1])
train_y = to_categorical(train_y)

test_x = np.random.uniform(size=[1,128,8])
test_y = np.random.randint(0, 6, [1, 1])
test_y = to_categorical(test_y, 6)

print(train_y.shape)
print(test_y.shape)

input_layer = Input([128, 8])
# m = SimpleRNN(100)(input_layer)
m = LSTM(1)(input_layer)
m = Dense(6, activation = "softmax")(m)
model = Model(input_layer, m)
model.compile("adam", "categorical_crossentropy", metrics=["acc"])

model.fit(train_x, train_y, epochs=10, validation_data=[test_x, test_y])

model.summary()

start_time = time.time()
model.predict(test_x)
print(time.time() - start_time)