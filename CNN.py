# 同济大学
# 人工智能 2151406刘卓明
# 开发时间 2023/5/21 23:36
import torch.optim
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# CNN的类
"""
卷积神经网络
这里是继承了nn.Module
"""


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()    # 引入类属性
        # nn.Sequential是一个序列容器
        """
         1. Conv2d代表二位卷积，卷积核大小为3，stride是步长，padding表示图像填充，比如原始图像是
         32*32,填充后是34*34，其输入参数的前两个代表输入张量的channel数和输出张量的channel数
         2.BatchNorm2d是做数据的归一化处理，把数据从比较偏的分布拉回比较标准的分布
         3.relu是激活函数
         4.MaxPool2d池化作用，是最大池化，还有平均池化
         5.liner用来设计全连接层，形状通常为[batch_size, size]，第二个size代表了神经元的个数
        """
        self.layers1 = nn.Sequential(

            # Conv2d代表二位卷积，卷积核大小为3，stride是步长，padding表示图像填充，比如原始图像是
            #  32*32,填充后是34*34

            nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1),# 32+2*1-3+1=32
            nn.BatchNorm2d(16),   # 进行数据的归一化处理，num_features：一般输入参数为batch_size*num_features*height*width，即为其中特征的数量
            nn.ReLU(inplace=True) # 激活函数
        )
        self.layers2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),# 32+2*1-3+1=32
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.layers3 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1), # 14+2*1-3+1=14
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2) # 14/2=7.输出为7*7？
        )
        self.layers4 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),

        )
        self.fc = nn.Sequential(
            nn.Linear(7 * 7 * 128, 1024),
            nn.ReLU(inplace=True),
            nn.Linear(1024, 100),
            nn.ReLU(inplace=True),
            nn.Linear(100, 26)
        )
# 前馈网络过程

    def forward(self, x):
        x = self.layers1(x)
        x = self.layers2(x)
        x = self.layers3(x)
        x = self.layers4(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x