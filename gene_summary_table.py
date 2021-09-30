# -*- coding: UTF8 -*-

import pandas as pd
import os
# import time
if __name__=='__main__':
    col_list = ['题号', '难度', '是否完成', '记录原因']


    # data_frame1 = pd.read_excel('.\\array_string\\record.xlsx')
    # data_frame2 = pd.read_excel('.\\hashtable\\record.xlsx')
    # res = pd.concat([data_frame1, data_frame2], axis=0, ignore_index=True)
    # print(res)

    # summary_frame = pd.ExcelWriter('.\\summary_record.xlsx')
    # row = 1
    # for i in range(2):
    #     data_frame.to_excel(summary_frame, startrow=row, header=False, index=False)
    #     row += data_frame.shape[0]
    # summary_frame.save()

    record_list = []
    dir_list = os.listdir(os.getcwd())
    for direc in dir_list:
        if direc != '.git' and os.path.isdir(direc):
            data_frame = pd.read_excel(os.path.join(direc,'record.xlsx'))
            record_list.append(data_frame)

    res = pd.concat(record_list, axis=0, ignore_index=True)
    print(res)
    # time.sleep(3)
    df = pd.DataFrame(res, columns=col_list)
    df.to_excel('summary_record.xlsx')