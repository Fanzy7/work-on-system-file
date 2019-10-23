#!/usr/bin/env python
from datetime import datetime
import os
import os.path
import sys
def main(target):
 dir_path = os.path.abspath(target)
 for i in os.listdir(target):
    old_name = os.path.join(dir_path, i)
    d = datetime.strptime(i, '%Y-%m-%d').strftime('%Y%m%d')
    new_name = os.path.join(dir_path, d)
    os.rename(old_name, new_name)
if __name__ == '__main__':
 main('E:\Personal Work\1_Computer Scicence\2_Python\Rename_filename\Objects/2018-5-25 范志远.docx')