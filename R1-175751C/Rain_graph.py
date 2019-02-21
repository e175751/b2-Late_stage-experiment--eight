import pandas as pd
import matplotlib.pyplot as plt

plt.xscale("log")
df = pd.read_csv("Rain_result.csv",header=None)
plt.grid(which="both")
plt.plot(df[1],df[0])
plt.savefig('Rain_cd.png')
