import pandas as pd
import matplotlib.pyplot as plt

plt.xscale("log")
df2 = pd.read_csv("Rx18_result.csv",header=None)
plt.grid(which="both")
plt.plot(df2[1],df2[0])
plt.savefig('Rx18_cd.png')
