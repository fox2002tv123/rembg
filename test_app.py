'''
Author: bob
Date: 2022-04-13 16:39:10
LastEditors: bob
LastEditTime: 2022-04-13 16:59:19
FilePath: \rembg\test_app.py
Description: 测试程序

Copyright (c) 2022 by bob, All Rights Reserved. 
'''
from rembg import remove # 导入程序
from PIL import Image

input_path = 'input.jpg' # 输入图片路径
output_path = 'output.png' # 输出图片路径

input = Image.open(input_path) # 打开图片
output = remove(input) # 去背景
output.save(output_path) # 保存图片