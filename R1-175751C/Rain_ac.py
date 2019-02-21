import pandas as pd
data_ave = []
data_cu=[]

file = pd.read_csv("Rain_data.csv",header=None)
data = file[1]
cu=0
for i in range(150,-5,-5):
    data_ave.append(i)
    num=0
    for k in range(0,len(file)):
        if i-5< data[k] and data[k] <= i:
            num += 1
    num = num / len(file)
    cu += num*100
    data_cu.append(cu)
    
df = pd.DataFrame({
    "frequency" : data_ave,
    "Accumulation" : data_cu}
)
df.to_csv("Rain_result.csv",mode="w",header=False,index=False)
print("finish")
