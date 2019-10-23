# -*- coding:utf8 -*-

import os
from datetime import datetime
import os.path
import sys
class BatchRename():
    def __init__(self):
        self.path ='C:\\Users\\Fan Zhiyuan\\OneDrive\\科研\\组会\\周总结\\'
    def rename(self):
        filelist = os.listdir(self.path)
        for item in filelist:
            if item.endswith('.doc'):
                old_name = os.path.join(os.path.abspath(self.path), item)
                d = datetime.strptime(item, '%Y-%m-%d 范志远.doc').strftime('%Y%m%d.doc')
                new_name = os.path.join(os.path.abspath(self.path), '范志远 ' + d)
                os.rename(old_name, new_name)
                print ("converting %s to %s ..." % (old_name, new_name))
            elif item.endswith('.docx'):
                old_name = os.path.join(os.path.abspath(self.path), item)
                d = datetime.strptime(item, '%Y-%m-%d 范志远.docx').strftime('%Y%m%d.docx')
                new_name = os.path.join(os.path.abspath(self.path), '范志远 ' + d)
                os.rename(old_name, new_name)
                print ("converting %s to %s ..." % (old_name, new_name))
            else:
                continue


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()