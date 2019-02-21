import pandas as pd
file = pd.read_csv("data_Rx26.csv",header=None)
data_num = []
data_cu=[]
data_ave=[]
data = file[2]

cu=0
for i in range(-10,-50,-3):
    data_ave.append(i)
    num=0
    for k in range(0,len(file)):
        if i-3 < data[k] and data[k] <= i:
            num+=1
    num = num / len(file)
    cu += num*100
    data_cu.append(cu)
    
df = pd.DataFrame({
    "frequency" : data_ave,
    "Accumulation" : data_cu}
)
df.to_csv("Rx26_result.csv",mode="w",header=False,index=False)
print("finish")
