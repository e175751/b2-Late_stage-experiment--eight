import pandas as pd
import matplotlib.pyplot as plt

plt.xscale("log")
df3 = pd.read_csv("Rx26_result.csv",header=None)
plt.grid(which="both")
plt.plot(df3[1],df3[0])
plt.savefig('Rx26_cd.png')
