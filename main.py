import numpy as np
import os
import re
import xlrd
import xlwt
import AI_ImportingNetworkData


ai = AI_ImportingNetworkData.Read(r'F:\360MoveData\Users\DELL\Desktop\数据.xlsx')
print(ai.bus_data)
ai.read_line()
print(ai.line_data)
ai.split_data()
print(ai.static_point)
print(ai.dynamic_point)