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
from sklearn.metrics import confusion_matrix
import seaborn as sns; 
import itertools
from matplotlib import pyplot as plt

def plot_confusion_matrix(cm, classes,
                          title,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
　　 cm:混淆矩阵值
　　 classes:分类标签
　　 """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.xlabel('True Label')
    plt.ylabel('Predicted Label')



# model path
model_path = "/home/wsn/Desktop/HAR/result/major_experiment/GRU_128/weights.194-0.9941.hdf5"

# load data
data_x = np.load("/home/wsn/Desktop/HAR/HGR_dataset/user_data/ni_x_128.npy")
data_y = np.load("/home/wsn/Desktop/HAR/HGR_dataset/user_data/ni_y_128.npy")

print(data_x.shape)
# data_x = cv2.blur(data_x, (128, 1))
print(data_y.shape)

# build rnn model
input_layer = Input([128, 8])
m = GRU(128)(input_layer)
m = Dense(7, activation = "softmax")(m)
model = Model(input_layer, m)

# testing
optimizer = Adam(lr=1e-4)
model.compile(optimizer, categorical_crossentropy, metrics=["acc"])
model.load_weights(model_path)

print(model.evaluate(data_x, data_y))

result = model.predict(data_x)
print(result.shape)
print(data_y.shape)
result = np.argmax(result, axis=1)
data_y = np.argmax(data_y, axis=1)
print(result.shape)
print(data_y.shape)


mat = confusion_matrix(result, data_y)
mat = np.round(mat/640, 4)
print(mat)
plt.rc("font", family="Times New Roman", size=12)
plt.rcParams['savefig.dpi'] = 200 #图片像素
plt.rcParams['figure.dpi'] = 200
plot_confusion_matrix(mat, classes=['0','1','2','3','4','5','6'], title="User 3 (Accuracy = 0.8257)")
plt.savefig('/home/wsn/Desktop/HAR/result_figure/Figure_user_ni.eps', bbox_inches='tight', restarized=True, format="eps")
plt.show()