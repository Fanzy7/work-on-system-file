#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
 
print( os.path.basename('E:\Personal Work\1_Computer Scicence\2_Python\Rename_filename\Objects/fan.zip') )   # 返回文件名
print( os.path.dirname('/root/runoob.txt') )    # 返回目录路径
print( os.path.split('/root/runoob.txt') )      # 分割文件名与路径
print( os.path.join('root','test','runoob.txt') )  # 将目录和文件名合成一个路径