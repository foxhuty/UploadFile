# -*- coding: utf-8 -*-
# @Time: 2022/8/27 17:03
# @Author: foxhuty
# @File: test_date.py
# @Software: PyCharm
# @Based on: python 3.10.6

import os
import datetime
import random


# f='12587.jpg'
# f_suffix=f.rsplit('.')[1]
# print(f_suffix)
# base_dir=os.path.abspath(os.path.dirname(__file__))
# print(base_dir)
#
# filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
# print(filename)
#
# random_num = random.randint(0, 100)
# print(random_num)
base_dir = os.path.abspath(os.path.dirname(__file__))
print(base_dir)
file_img = base_dir + "/static/files/"
file_list=os.listdir(file_img)
print(file_list)
