#!/usr/bin/env python
# -*- coding: utf8 -*-

import pandas as pd
import numpy as np
import re
import pickle
from numpy import linalg as la
import xlrd
import sys
import openpyxl
import heapq

def computeSim(inA, inB):  # 相似度计算 余弦相似度
    sim = np.dot(inA, inB.reshape(-1, 1)) / (la.norm(inA) * la.norm(inB))
    return sim[0]

# 打开excel文件,获取工作簿对象
wb = openpyxl.load_workbook('user.xlsx')
ws = wb.active  # 当前活跃的表单

major_info = {"IT类": 1, "通信类": 2, "自动化类": 3, "机械类": 4, "安全工程类": 5, "土木建工": 6, "化工类": 7,"环境生态类": 8,"医学": 9,"测绘类": 10,"农学类": 11,"理学类": 12,"经管类": 13,"法学": 14,"文学类": 15,"艺术类": 16,"哲学": 17,"教育学": 18,"体育学": 19}
total = 0
newuser = ['00001', '男', '30', 'IT类', '计算机科学与技术', 'IT类', '软件工程师']

sim = []
for i in range(302):
    sim.append(0)

for row in ws.iter_rows():
    for cell in row:
        tmp = major_info.get(cell, default=None)
        for index in newuser:
            for each in sim:
                if (tmp is not None):
                    total += computeSim(index, tmp)