import numpy as np
from matplotlib import pyplot as plt
import time

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

    filename = "../data_0707/0/"
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


    # f = open("/home/wsn/Desktop/HAR/HGR/test_switch.txt", "rb")
    # data = f.read()
    # data1 = processing_data(data)
    # f = open("/home/wsn/Desktop/HAR/HGR/test_switch0702.txt", "rb")
    # data = f.read()
    # data2 = processing_data(data)
    # x = np.arange(1, data1.shape[1] +1)
    # plt.ion()
    # plt.title("test")
    # for j in range(100):
    #     for i in range(8):
    #         plt.xlabel("samples")
    #         plt.ylabel("Voltage /V")
    #         plt.ylim([0, 5.0])
    #         plt.subplot(4, 2, i+1)
    #         plt.plot(x, data1[i])
    #         plt.title("ch" + str(i + 1))
    #         plt.tight_layout(1)
    #     plt.pause(0.1)
    #     plt.clf()
    #     for i in range(8):
    #         plt.xlabel("samples")
    #         plt.ylabel("Voltage /V")
    #         plt.ylim([0, 5.0])
    #         plt.subplot(4, 2, i+1)
    #         plt.plot(x, data2[i])
    #         plt.title("ch" + str(i + 1))
    #         plt.tight_layout(1)
    #     plt.pause(0.1)
    #     plt.clf()