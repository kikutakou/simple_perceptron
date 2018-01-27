import argparse
import numpy as np
import sys
import os
from collections import namedtuple
import pyplot_helper as plt


class Data(object):

    __slots__ = ["x1", "x2", "y1", "y2", "x_all", "y_all"]

    def __init__(self, file, y2label=0):
        
        # load data
        if file == "-":
            fin = sys.stdin
        elif os.path.exists(file):
            fin = open(file)
        else:
            exit("file {} not found".format(file))
        data_txt = [line.rstrip("\r\n").split("\t") for line in fin.readlines()]

        # parse (txt to float,int)
        data = [[[float(a) for a in ary[0:-1]], int(ary[-1])] for ary in data_txt]

        self.x1 = np.array([d[0] for d in data if d[1] > 0]).T
        self.x2 = np.array([d[0] for d in data if not d[1] > 0]).T

        self.y1 = np.array([d[1] for d in data if d[1]])
        self.y2 = np.array([d[1] for d in data if not d[1]])


        # concat
        self.x_all = np.concatenate([self.x1, self.x2], axis=1)
        self.y_all = np.concatenate([self.y1, self.y2])

if __name__ == '__main__':

    data = Data('sample.txt')
    print(data)
    plt.plot_main(data.x1, data.x2)
    plt.show()


