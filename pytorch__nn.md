# 有关于pytorch中神经网络的一些说明
model.parameters()与model.state_dict()是Pytorch中用于查看网络参数的方法。  
一般来说，前者多见于优化器的初始化，如：  
`optimizer = torch.optim.SGD(cnn.parameters(), lr=0.1)`  
后者多见于模型的保存，如：  
`torch.save(model.state_dict(),'best_model.pth')`  


