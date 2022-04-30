#  余弦退火算法示例 #
# -------------- #

import torch
import torch.nn as nn
from torch.optim.lr_scheduler import CosineAnnealingLR, CosineAnnealingWarmRestarts
import itertools
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt


class Tmodel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3)

    def forward(self, x):
        pass

model = Tmodel()

optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
scheduler = CosineAnnealingWarmRestarts(optimizer, T_0=5, T_mult=2,eta_min=1e-5)

print("初始化的学习率：", optimizer.defaults['lr'])

lr_list = []  # 把使用过的lr都保存下来，之后画出它的变化

for epoch in range(1, 31):
    # train
    optimizer.zero_grad()
    optimizer.step()
    print("第%d个epoch的学习率：%f" % (epoch, optimizer.param_groups[0]['lr']))
    lr_list.append(optimizer.param_groups[0]['lr'])
    scheduler.step()

# 画出lr的变化
plt.plot(list(range(1, 31)), lr_list)
plt.xlabel("epoch")
plt.ylabel("lr")
plt.title("learning rate's curve changes as epoch goes on!")
plt.show()

print("已经完成")