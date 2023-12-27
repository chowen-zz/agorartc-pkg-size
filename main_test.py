#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 6:14 下午
# @Created By  : zhouwen
# @Software: PyCharm
import os
import sys
base_path = os.path.dirname(__file__)
sys.path.append(os.path.abspath(base_path))
sys.path.append(os.path.dirname(os.path.abspath(base_path)))
print(f'base_path:{os.path.abspath(base_path)}')

if __name__ == "__main__":
    podFile = open('ios/Podfile', 'r+')
    podFileText = podFile.read()
    print(f'podFileTest:{podFileText}')