# 卷积神经网络中的一些相关说明
### 1.四维张量[B, C, H, W]  
其中𝑏表示输入的数量，𝑐表示特征图的通道数,h、w分布表示特征图的高宽  
部分深度学习框架也会使用[ h, w,c ]格式的特征图张量，例如PyTorch。    
图片数据是特征图的一种，对于含有RGB 3 个通道的彩色图片，每张图片包含了h 行w 列像素点，  
每个点需要3 个数值表示RGB 通道的颜色强度，因此一张图片可以表示为[h, w, 3]  
### 2.关于卷积层输出size的计算
O=输出图像的尺寸(output)  
I=输入图像的尺寸(input)  
K=卷积层的核尺寸(kernel_size)  
N=核数量  
S=移动步长(stride)  
P =填充数(padding)  
O=(I-K+2P)/S+1  
### 3.关于池化层输出size的计算
O=输出图像的尺寸。
I=输入图像的尺寸。
S=移动步长
PS=池化层尺寸  
O=(I-PS)/S+1  
不同于卷积层，池化层的输出通道数不变(卷积层的输出通道数，也就是神经元的数量为N)  
[详细说明见文章](https://zhuanlan.zhihu.com/p/414328961#:~:text=K%3D%E5%8D%B7%E7%A7%AF%E5%B1%82%E7%9A%84%E6%A0%B8%E5%B0%BA%E5%AF%B8%20N%3D%E6%A0%B8%E6%95%B0%E9%87%8F%20S%3D%E7%A7%BB%E5%8A%A8%E6%AD%A5%E9%95%BF%20P%20%3D%E5%A1%AB%E5%85%85%E6%95%B0,%E8%BE%93%E5%87%BA%E5%9B%BE%E5%83%8F%E5%B0%BA%E5%AF%B8%E7%9A%84%E8%AE%A1%E7%AE%97%E5%85%AC%E5%BC%8F%E5%A6%82%E4%B8%8B%EF%BC%9A%20%E8%BE%93%E5%87%BA%E5%9B%BE%E5%83%8F%E7%9A%84%E9%80%9A%E9%81%93%E6%95%B0%E7%AD%89%E4%BA%8E%E6%A0%B8%E6%95%B0%E9%87%8FN%E3%80%82%20%E7%A4%BA%E4%BE%8B%EF%BC%9AAlexNet%E4%B8%AD%E8%BE%93%E5%85%A5%E5%9B%BE%E5%83%8F%E7%9A%84%E5%B0%BA%E5%AF%B8%E4%B8%BA227%2A227%2A3.%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8D%B7%E7%A7%AF%E5%B1%82%E6%9C%8996%E4%B8%AA%E5%B0%BA%E5%AF%B8%E4%B8%BA11%2A11%2A3%E7%9A%84%E6%A0%B8%E3%80%82%20%E6%AD%A5%E9%95%BF%E4%B8%BA4%EF%BC%8C%E5%A1%AB%E5%85%85%E4%B8%BA0.%20%E8%BE%93%E5%87%BA%E7%9A%84%E5%9B%BE%E5%83%8F%E4%B8%BA55%2A55%2A96%EF%BC%88%E6%AF%8F%E4%B8%AA%E6%A0%B8%E5%AF%B9%E5%BA%941%E4%B8%AA%E9%80%9A%E9%81%93%EF%BC%89%E3%80%82)  
### 4.关于每层的参数数量计算
在CNN中,每层有两种类型的参数:weights 和biases.总参数数量为所有weights和biases的总和.  
定义如下:  
WC=卷积层的weights数量  
BC=卷积层的biases数量  
PC=所有参数的数量  
K=核尺寸  
N=核数量  
C =输入图像通道数  
  
WC=K*K*C*N  
BC=N  
PC=WC-BC  
