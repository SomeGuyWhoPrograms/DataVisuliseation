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

    lim:int = len(ser)
    while (lim % 5) != 0: 
        lim += 1  
    
    label: list[str] = ['0']
    for i in range(5,len(ser),5): 
        label.append(f"{i}")
    label.append(f"{lim}")

    plt.xticks(range(-1,lim,5),
            labels=label
            )
    plt.xlim(-1, xmax=lim)
    plt.ylim(ymin=lcl-0.5, ymax=ucl+0.5)

    plt.text(lim+1, ser.mean()-0.005, 'X̄', style='italic',fontsize=18)
    plt.text(lim+1, ucl-0.005, 'UCL', style='italic',fontsize=18)
    plt.text(lim+1, lcl-0.005, 'LCL', style='italic',fontsize=18)

    plt.plot(range(0, len(ser)), ser, marker=".", color="b")
    plt.plot([-1,lim], [lcl,lcl], ls="dashed", color="r", label="UCL") # +3stdv 
    plt.plot([-1,lim], [ser.mean(),ser.mean()], color="k", ls="dotted", label="Center line")  # mean 
    plt.plot([-1,lim], [ucl,ucl], ls="dashed", color="r",label="LCL") # -3stdv

    plt.grid(lw=0.5)  
    #plt.show()
    plt.savefig(fname=f"Plots/Xbar/{name}") 
    plt.close()

def controlRB(df:pd.DataFrame, name:str, batch="") -> None:

    ser: pd.Series = df[name]
    plt.figure(figsize=(10, 8))# layout="constrained")
    plt.title(f"R̄ Bar Control Chart\n{name}{batch}", size=25)
    plt.xlabel("Number of Observations", size=15)   # "Observations"
    plt.ylabel("Range of values", size=15)  

    mran:list[float] = [] 
    for i in range(1, len(ser)): 
        mran.append(abs((ser[i-1]) - ser[i]))

    lim:int = len(mran)
    while (lim % 5) != 0: 
        lim += 1 
    
    ucl:float = np.mean(mran) + 3*np.std(mran)
    lcl:float = np.mean(mran) - 3*np.std(mran)

    plt.text(lim+1, np.mean(mran)-0.005, 'R̄', style='italic',fontsize=18)
    plt.text(lim+1, ucl-0.005, 'UCL', style='italic',fontsize=18)
    plt.text(lim+1, lcl-0.005, 'LCL', style='italic',fontsize=18)

    label: list[str] = ['0']
    for i in range(5,lim,5): # need to set len of lim
        label.append(f"{i}")
    label.append(f'{lim}')  

    plt.xticks(range(-1,lim,5),
        labels=label
        )
    plt.xlim(left=-1, xmax=lim)
    plt.ylim(ymin=lcl-0.5, ymax=ucl+0.5)

    plt.plot(range(0, len(mran)), mran, marker=".", color="b")
    plt.plot([-1,lim], [lcl,lcl], ls="dashed", color="r", label="UCL") # +3stdv 
    plt.plot([-1,lim], [np.mean(mran),np.mean(mran)], color="k", ls="dotted", label="Center line")  # mean 
    plt.plot([-1,lim], [ucl,ucl], ls="dashed", color="r") # -3stdv

    plt.grid(lw=0.5)  
    #plt.show()
    plt.savefig(fname=f"Plots/Rbar/{name}")
    plt.close() 

def OverlayedXB(B1:pd.DataFrame, B2:pd.DataFrame,name)->None: 
    B1s:pd.Series = B1[name]
    B2s:pd.Series = B2[name]
    ucl:float = idealhingeMesurments[name] + 0.3
    lcl:float = idealhingeMesurments[name] - 0.3
    meantol:float = idealhingeMesurments[name]

    plt.figure(figsize=(10, 8))# layout="constrained")
    plt.title(f"Combined Baches Against Tolerance\n{name}", size=25)
    plt.xlabel("Number of Observations", size=15)   # "Observations"
    plt.ylabel("Measured Values (mm)", size=15) 

    lim:int = max(len(B1s),len(B2s))
    while (lim % 5) != 0: 
        lim += 1  

    label:list[str] = ['0'] 
    for i in range(5 ,lim,5): 
        label.append(f"{i}")
    label.append(f"{lim}")

    plt.xticks(range(-1,lim,5),
            labels=label  
            )
    plt.xlim(-1, xmax=lim)
    plt.ylim(ymin=lcl-0.5, ymax=ucl+0.5)

    plt.text(lim+1, meantol-0.005,"X̄",style='italic',fontsize=18) 
    plt.text(lim+1, ucl-0.005, 'SL', style='italic',fontsize=18)
    plt.text(lim+1, lcl-0.005, 'SL', style='italic',fontsize=18)

    plt.scatter(range(0, len(B1s)), B1s, marker=".", color="b",s=80)
    plt.scatter(range(0, len(B2s)), B2s, marker=".", color="g",s=80)
    plt.plot([-1,lim], [lcl,lcl], ls="dashed", color="r")
    plt.plot([-1,lim], [ucl,ucl], ls="dashed", color="r")
    plt.plot([-1,lim], [meantol,meantol], ls="dashed", color="r")

    
    plt.grid(lw=0.5)  
    #plt.show()
    plt.savefig(fname=f"Plots/Overlayed/{name}")
    plt.close()  

def controlImr(df:pd.DataFrame, name:str, batch="") -> None:
    ser: pd.Series = df[name]
    plt.figure(figsize=(10, 8))# layout="constrained")
    plt.title(f"I-MR Control Chart\n{name}{batch}", size=25)
    plt.xlabel("Number of Observations", size=15)   # "Observations"
    plt.ylabel("Range of values", size=15)  

    mran:list[float] = [] 
    for i in range(1, len(ser)): 
        mran.append(abs((ser[i-1]) - ser[i]))

    mr:float = np.average(mran) 
    x:float = np.average(ser) 
    ucl:float = x + 3*(mr/1.128)
    lcl:float = x - 3*(mr/1.128)

    lim:int = len(mran)
    while (lim % 5) != 0: 
        lim += 1 

    label:list[str] = ['0'] 
    for i in range(5 ,lim,5): 
        label.append(f"{i}")
    label.append(f"{lim}")

    plt.xticks(range(-1,lim,5),
            labels=label  
            )
    plt.xlim(-1, xmax=lim)
    plt.ylim(ymin=lcl-0.5, ymax=ucl+0.5)

    plt.text(lim+1, x-0.005," __\nMR",style='italic',fontsize=18) 
    plt.text(lim+1, ucl-0.005, 'UCL', style='italic',fontsize=18)
    plt.text(lim+1, lcl-0.005, 'LCL', style='italic',fontsize=18)


    plt.plot([-1,lim], [lcl,lcl], ls="dashed", color="r")
    plt.plot([-1,lim], [ucl,ucl], ls="dashed", color="r")
    plt.plot([-1,lim], [x,x], ls="dashed", color="r")
    plt.plot(range(0, len(ser)), ser, marker=".", color="b")

    plt.grid(lw=0.5)  
    #plt.show()
    plt.savefig(fname=f"Plots/I-MR/{name}")
