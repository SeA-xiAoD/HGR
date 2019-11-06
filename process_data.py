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


def read_data_from_dir_list(data_dir_list, sampling_rate=256, save_file_path=None):
    # load data
    data_x = None
    data_y = None                                          
    for data_dir in data_dir_list:
        dir_list = os.listdir(data_dir)
        dir_list = sorted(dir_list)
        labels = []
        for i in dir_list:
            if not i.startswith("."):
                labels.append(i)
        print(labels)

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
                temp_data = np.reshape(temp_data, [-1, sampling_rate, 8])
                
                if data_x is None:
                    data_x = temp_data
                    data_y = np.ones([temp_data.shape[0], 1]) * int(label)
                else:
                    data_x = np.concatenate([data_x, temp_data])
                    data_y = np.concatenate([data_y, np.ones([temp_data.shape[0], 1]) * int(label)]) 
    
    data_y = to_categorical(data_y, 7)
    if save_file_path is not None:
        np.save(save_file_path + "_x_" + str(sampling_rate), data_x)
        np.save(save_file_path + "_y_" + str(sampling_rate), data_y)
    return data_x, data_y


if __name__ == "__main__":

    filename = "/home/wsn/Desktop/HAR/HGR_dataset/data_song/2/"
    number = input()
    filename = filename + number + ".txt"
    f = open(filename, "rb")
    data = f.read()
    data = processing_data(data)
    x = np.arange(1, data.shape[1] +1)
    for i in range(8):
        plt.xlabel("samples")
        plt.ylabel("Voltage /V")
        plt.subplot(4, 2, i+1)
        plt.ylim([0, 3.0])
        plt.plot(x, data[i])
        plt.title("ch" + str(i + 1))
        plt.tight_layout(1)
    plt.pause(0.0000000001)
    plt.show()

    # # generate data
    # dir_list = ["/home/wsn/Desktop/HAR/HGR_dataset/user_data/hao"]

    # read_data_from_dir_list(dir_list, 128, "/home/wsn/Desktop/HAR/HGR_dataset/user_data/hao")