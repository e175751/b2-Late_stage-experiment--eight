import os
import pandas as pd
import numpy as np
import datetime

data_path = "/Users/e175751/Desktop/programing/課題2/experiment/第八回"

month = ["06","10","11","12"]

for i in month:
    for j in range(1,32,1):
        path = ["RainData/2009" + str(i) + str(j).zfill(2) + "/2009" + str(i) + str(j).zfill(2) + "_rain.csv"]
        for k in path:
            try:
                df = pd.read_csv(k)
                #print(file)
            except:
                continue

            try:
                    f = lambda x: x *60*0.0083333
                    df2 = df["Recording started."].map(f)
                    #print(file_Rx)
            except:
                continue

            df3 = df2.fillna(0)
            df3.to_csv("Rain_data.csv",mode="a",header=False)

print("終了です")


                
