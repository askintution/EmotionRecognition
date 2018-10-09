#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 9:25
# @Author  : NYY
# @Site    : www.niuyuanyuanna.git.io
# @File    : calculate_mean_and_std.py
import os
import cv2
import numpy as np

from dataset.load_raf_dataset import load_normal_list
from config.configs import config


if __name__ == '__main__':
    train_dir_path = config.dataset.raf.label_list_path
    train_txt_path = os.path.join(train_dir_path, 'train_image_label.txt')
    train_image_list, train_label = load_normal_list(train_txt_path)
    sum_r = 0
    sum_g = 0
    sum_b = 0
    var_r = 0
    var_g = 0
    var_b = 0
    count = len(train_image_list)
    for image_name in train_image_list:
        img = cv2.imread(image_name)
        img = cv2.resize(img, config.pre_params.resize)
        sum_b += img[:, :, 0].mean()
        sum_g += img[:, :, 1].mean()
        sum_r += img[:, :, 2].mean()
    sum_r = sum_r / count
    sum_g = sum_g / count
    sum_b = sum_b / count
    img_mean = [sum_r, sum_g, sum_b]
    print(img_mean)

    for image_name in train_image_list:
        img = cv2.imread(image_name)
        img = cv2.resize(img, config.pre_params.resize)
        var_b += np.square(img[:, :, 0].mean() - sum_b)
        var_g += np.square(img[:, :, 1].mean() - sum_g)
        var_r += np.square(img[:, :, 2].mean() - sum_r)
    std_r = np.sqrt(var_r / (count - 1))
    std_g = np.sqrt(var_g / (count - 1))
    std_b = np.sqrt(var_b / (count - 1))

    img_std = [std_r, std_g, std_b]
    print(img_std)



