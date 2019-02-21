import os
import pandas as pd
import numpy as np
import datetime

data_path = "/Users/e175751/Desktop/programing/課題2/experiment/第八回"
file_path = "/Users/e175751/Desktop/programing/課題2/experiment/第八回"

month = ["06","10","11","12"]

for i in month:
    #print(i)
    for j in range(1,32,1):
        #print(j)
        path = ["RxData/2009" + str(i) + "/2009" + str(i) + str(j).zfill(2) + "/192.168.100._csv.log"]
        #print(path)
        for k in path:
            #print(k)
            try:
                file = pd.read_csv(k,header=1)

            except :
                continue

            file_time = file[["time"]]
            file = file[[" 1803_RX_LEVEL"]]


            try:
                f = lambda x: (x + 256)/2 - 121 if x < 0 else x/2 - 121
                file_Rx = file[" 1803_RX_LEVEL"].map(f)

            except TypeError:
                continue

        #file_timeとfile_rxの配列を列ごとに繋げる
            file_join = pd.concat([file_time, file_Rx], axis=1)


        #時間(columns)のtimeという名前をつける
            file_join = file_join.set_index("time")


        #timeをdatetime型に変換する
            file_join.index = pd.to_datetime(file_join.index)


        #file_joinのtimeを10秒ごとに分割し,Rxの平均を取る
            res = file_join.resample("10S").mean()


        #reset_indexでtimeを指定し,時間を整える
            df = res.reset_index("time")
            #print(df6)

        #結果をfileに書き込む
            df.to_csv("data_Rx23.csv",mode="a",header=False)



print("終了しました")
