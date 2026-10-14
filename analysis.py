import pandas as pd 
from constants import idealhingeMesurments, lookup 
from plot import Plots  

class ControlSPC: 
    def __init__(self, df:pd.DataFrame, name) -> None:
        self.centerline:float = 0.0 
        self.ucl:float = 0.0 
        self.lcl:float = 0.0 
        self.type:str = "" 
        self.name:str = name
        self.data:pd.DataFrame = df 
        self.ser = self.data[self.name]

    def IMR (self, r:int, batch="")-> Plots: 
        self.type = "I-mR̄" 

        mran:list[float] = [] 
        for i in range(1, len(self.ser)): 
            mran.append(abs((self.ser[i-1]) - self.ser[i])) 

        self.ser = self.data[self.name]
        self.centerline = sum(self.ser) / len(self.ser) 
        self.ucl = self.centerline + (lookup(table="IndividualXR", columb="E2", n=r) * (sum(mran) / (len(mran) - 1)))
        self.lcl = self.centerline - (lookup(table="IndividualXR", columb="E2", n=r) * (sum(mran) / (len(mran) - 1)))
        return Plots(self)   #  batch 

    def XMR(self, r:int, batch="") -> Plots: 
        self.type = "X-mR̄"

        mran:list[float] = [] 
        for i in range(1, len(self.ser)): 
            mran.append(abs((self.ser[i-1]) - self.ser[i])) 

        self.ser = mran 
        self.centerline = sum(mran) / (len(mran) - 1)
        self.ucl:float = lookup(table="MediamXR", columb="D4", n=r)  * (sum(mran) / (len(mran) - 1))
        self.lcl:float = lookup(table="MediamXR", columb="D3", n=r)  * (sum(mran) / (len(mran) - 1))
        return Plots(self)  

    def Xbar(self): 
        # to properly define this you need the splitter function to accuratly fork for n number batches 
        pass 

    def Rbar(self): 
        pass 

"""
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
    """
