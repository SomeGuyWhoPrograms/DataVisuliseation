import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
from constants import idealhingeMesurments

def dstats(df:pd.DataFrame, name) -> None: 
    des = df.agg(['mean','median','average','std','sem','var','min','max','size']) 
    des = des.rename(index={'sem':'standard error','average':'mode','var':'veriance'}) 
    des.to_csv(f"{name}.csv")

def controlXB(df:pd.DataFrame, name:str ,batch="") -> None:
    ser:pd.Series = df[name]
    ucl:float = ser.mean() + 3*ser.std()
    lcl:float = ser.mean() - 3*ser.std()

    plt.figure(figsize=(10, 8))# layout="constrained")
    plt.title(f"X̄ Bar Control Diagram\n{name}{batch}", size=25)
    plt.xlabel("Number of Observations", size=15)   # "Observations"
    plt.ylabel("Measured Values (mm)", size=15)  
    #plt.ylim(bottom=(ser.min()-0.5), top=(ser.max()+0.5)) 
    plt.xticks(range(0,39,2),
            labels=['1','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30','32','34','36','38']
            )
    plt.xlim(-0.5, xmax=len(ser)-0.55)

    plt.text(len(ser), ser.mean()-0.005, 'X̄', style='italic',fontsize=18)
    plt.text(len(ser), ucl-0.005, 'UCL', style='italic',fontsize=18)
    plt.text(len(ser), lcl-0.005, 'LCL', style='italic',fontsize=18)

    plt.plot(range(0, len(ser)), ser, marker=".", color="b")
    plt.plot([-0.5,40], [lcl,lcl], ls="dashed", color="r", label="UCL") # +3stdv 
    plt.plot([-0.5,40], [ser.mean(),ser.mean()], color="k", ls="dotted", label="Center line")  # mean 
    plt.plot([-0.5,40], [ucl,ucl], ls="dashed", color="r",label="LCL") # -3stdv
    #plt.plot([20,20], [ser.min()-0.5,ser.max()+0.5])

    plt.grid()  
    plt.show()
    #plt.savefig(fname=f"Plots/Xbar/{name}") 
    plt.close()

def controlRB(df:pd.DataFrame, name:str, batch="") -> None:

    ser: pd.Series = df[name]
    plt.figure(figsize=(10, 8))# layout="constrained")
    plt.title(f"R̄ Bar Control Chart\n{name}{batch}", size=25)
    plt.xlabel("Number of Observations", size=15)   # "Observations"
    plt.ylabel("Range of values", size=15)  
    
    plt.xticks(range(0,45,5),
        labels=['1','5','10','15','20','25','30','35','40']
        )

    Ran = [] 
    for i in range(0, len(ser)): 
        Ran.append((idealhingeMesurments[name] - ser[i]))

    ucl:float = np.mean(Ran) + 3*np.std(Ran)
    lcl:float = np.mean(Ran) - 3*np.std(Ran)

    plt.text(len(Ran), np.mean(Ran)-0.005, 'R̄', style='italic',fontsize=18)
    plt.text(len(Ran), ucl-0.005, 'UCL', style='italic',fontsize=18)
    plt.text(len(Ran), lcl-0.005, 'LCL', style='italic',fontsize=18)
    #plt.ylim(bottom=(min(Ran)-0.05), top=(max(Ran)+0.05))
    plt.xticks(range(0,39,2),
        labels=['1','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30','32','34','36','38']
        )
    plt.xlim(left=-0.5, xmax=len(Ran)-0.55)

    plt.plot(range(0, len(Ran)), Ran, marker=".", color="b")
    plt.plot([-0.5,40], [lcl,lcl], ls="dashed", color="r", label="UCL") # +3stdv 
    plt.plot([-0.5,40], [np.mean(Ran),np.mean(Ran)], color="k", ls="dotted", label="Center line")  # mean 
    plt.plot([-0.5,40], [ucl,ucl], ls="dashed", color="r",label="LCL") # -3stdv
    #plt.plot([20,20], [min(Ran)-0.05,max(Ran)+0.05])

    plt.grid()  
    #plt.show()
    plt.savefig(fname=f"Plots/Rbar/{name}")
    plt.close() 

def OverlayedXB(B1:pd.DataFrame, B2:pd.DataFrame,name)->None: 
    B1s:pd.Series = B1[name]
    B2s:pd.Series = B2[name]
    ucl:float = (B1s.mean() + 3*B1s.std()) + (B2s.mean() + 3*B2s.std()) /2 
    lcl:float = (B1s.mean() - 3*B1s.std()) + (B2s.mean() - 3*B2s.std()) /2 # thees are inffered so idk if i can properly plot them 
    meanCom = (B1s.mean() + B2s.mean()) / 2 

    plt.figure(figsize=(10, 8))# layout="constrained")
    plt.title(f"Combined Baches Against Tolerance\n{name}", size=25)
    plt.xlabel("Number of Observations", size=15)   # "Observations"
    plt.ylabel("Measured Values (mm)", size=15)  

    plt.text(max(len(B1s),len(B2s)), ((B1s.mean()+B2s.mean())/2),"X̄",style='italic',fontsize=18)
    plt.xticks(range(0,39,2),
            labels=['1','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30','32','34','36','38']
            )
    plt.xlim(-0.5, xmax=max(len(B1s),len(B2s))-0.55)
    plt.plot(range(0, len(B1s)), B1s, marker=".", color="b")
    plt.plot(range(0, len(B2s)), B2s, marker=".", color="r")
    plt.grid()  
    plt.show()
    #plt.savefig(fname=f"Plots/Overlayed/{name}")
    #plt.close()