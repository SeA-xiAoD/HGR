import numpy as np
from matplotlib import pyplot as plt
import time
import cv2
import os
from keras.utils import to_categorical


def processing_data(raw_data):
    """Convert raw data to 8 dimentions
    input: raw data
    return: numpy array
    """
    data = np.frombuffer(raw_data, np.uint8)
    data = np.reshape(data, [data.shape[0]//1029, -1])
    data = data[:, 5:]
    data = np.reshape(data, [1, -1])
    data = 256 * data[0, 0::2] + data[0, 1::2]
    data = 10 * (data / 65535)
    data = np.reshape(data, [-1, 8]).T
    return data


if __name__ == "__main__":

    # 2: 70;  4: 70;  6: 90;
    filename = "/home/wsn/Desktop/HAR/HGR_dataset/data_sea/2/"
    number = input()
    filename = filename + number + ".txt"
    f = open(filename, "rb")
    data = f.read()
    data = processing_data(data)
    avg = np.average(data, axis=1)
    print(avg.shape)

    plt.rc("font", family="Times New Roman", size=16)
    plt.bar(["ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8"], avg)
    plt.xlabel("Channel", size=16)
    plt.ylabel("Voltage (V)", size=16)
    plt.ylim(0, 2.5)
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.dpi'] = 300
    plt.savefig('/home/wsn/Desktop/HAR/result_figure/Figure_shadow_2.eps', bbox_inches='tight')
    plt.show()
    