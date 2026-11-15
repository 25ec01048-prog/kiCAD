import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

vtc = [5, 9]


for i in vtc:
    df = pd.read_csv("vtc_"+ str(i)+"v.txt", delimiter="\t")
    
    vm= np.mean(df[((i/2 - (i/2 *0.2)) < df["V(vout)"]) &( df["V(vout)"] < i/2 + i/2 *0.01)])

    y = plt.plot(df["Vin"], df["V(vout)"], label = "$V_{DD}$ ="+str(i)+" (V), $V_m$ = "+ str(round(vm,2))+ " (V)")
    

    plt.axhline(i/2, color = y[0].get_color(), linestyle ="--")
    plt.axvline(vm, color = y[0].get_color(), linestyle ="--")

plt.legend()
plt.xlabel("$V_{in}$")
plt.ylabel("$V_{out}$")
plt.title("Voltage transfer curve")
plt.savefig("figures/l2-vtc.png",  dpi=300, bbox_inches="tight")
plt.show()
