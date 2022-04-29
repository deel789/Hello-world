import torch
import torchvision


import os
import numpy as np
from PIL import Image

'''
x = torch.randn(128,20)
m = torch.nn.Linear(20,30)
output = m(x)
print('m.weight.shape:\n', m.weight.shape)
print('m.bias.shape:\n', m.bias.shape)
print('output.shape:\n', output.shape)
'''


def rand(a=0, b=1):
    return np.random.rand() * (b - a) + a



min_offset_x = rand(0.25, 0.75)
min_offset_y = rand(0.25, 0.75)
nws = [int(1280 * rand(0.4, 1)), int(1280 * rand(0.4, 1)), int(1280 * rand(0.4, 1)), int(1280 * rand(0.4, 1))]
nhs = [int(720 * rand(0.4, 1)), int(720 * rand(0.4, 1)), int(720 * rand(0.4, 1)), int(720 * rand(0.4, 1))]
w,h = 1280,720
place_x = [int(w*min_offset_x)-nws[0], int(w*min_offset_x)-nws[1], int(w*min_offset_x), int(w*min_offset_x)]
place_y = [int(h*min_offset_y)-nhs[0], int(h*min_offset_y)-nhs[1], int(h*min_offset_y), int(h*min_offset_y)]
nw = place_x[0]
nh = place_y[0]

if __name__ == "__main__":
    path = os.getcwd()
    path_img = os.path.join(path, 'data/images')
    img_list = os.listdir(path_img)
    img1 = Image.open(os.path.join(path_img, img_list[0]))
    img2 = Image.open(os.path.join(path_img, img_list[2]))
    img1.paste(img2, (nw, nh))
    img1.show()
    new_image = Image.new('RGB', (1280, 720), (128, 128, 128))
