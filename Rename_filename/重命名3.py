#coding:utf-8
from datetime import datetime
import os
import os.path
import sys
movie_name = os.listdir('./重命名文件/对象')
for temp in movie_name:
    new_name = datetime.strptime(temp, '%Y-%m-%d').strftime('%Y%m%d')
 
    os.rename('./对象/'+temp,'对象/'+new_name)