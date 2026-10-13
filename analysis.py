import pandas as pd 
import matplotlib.pyplot as plt  
from constants import idealhingeMesurments, lookup   

class ControlSPC: 
    def __init__(self, df:pd.DataFrame, name) -> None:
        self.centerline:float = 0.0 
        self.ucl:float = 0.0 
        self.lcl:float = 0.0 
        self.type:str = "" 
        self.name:str = name
        self.data:pd.DataFrame = df 
        self.ser = self.data[self.name]

    def plotter(self, batch:str) -> None: 
        plt.figure(figsize=(10, 8))
        plt.title(f"{self.type} Control Diagram\n{self.name} {batch}", size=25)
        plt.xlabel("Number of Observations", size=15) 
        plt.ylabel("Measured Values (mm)", size=15)  
    
        lim:int = len(self.ser)
        while (lim % 5) != 0: 
            lim += 1  
        
        label: list[str] = ['0']
        for i in range(5,len(self.ser),5): 
            label.append(f"{i}")
        label.append(f"{lim}")
    
        plt.xticks(range(-1,lim,5),
                labels=label
                )
        plt.xlim(-1, xmax=lim)
        plt.ylim(ymin=self.lcl-0.25, ymax=self.ucl+0.25)
    
        plt.text(lim+0.5, self.centerline-0.005, f"{self.type}", style='italic',fontsize=18)
        plt.text(lim+0.5, self.ucl-0.005, 'UCL', style='italic',fontsize=18)
        plt.text(lim+0.5, self.lcl-0.005, 'LCL', style='italic',fontsize=18)
    
        plt.plot(range(0, len(self.ser)), self.ser, marker=".", color="b")
        plt.plot([-1,lim], [self.lcl,self.lcl], ls="dashed", color="r", label="UCL") 
        plt.plot([-1,lim], [self.centerline,self.centerline], color="k", ls="dotted", label="Center line") 
        plt.plot([-1,lim], [self.ucl,self.ucl], ls="dashed", color="r",label="LCL") 
    
        plt.grid(lw=0.5)  
        #plt.show()
        plt.savefig(fname=f"Plots/{self.type}/{self.name}{batch}") 
        plt.close()

    def IMR (self, r:int, batch="")-> None: 
        self.type = "I-mR̄" 

        mran:list[float] = [] 
        for i in range(1, len(self.ser)): 
            mran.append(abs((self.ser[i-1]) - self.ser[i])) 

        self.ser = self.data[self.name]
        self.centerline = sum(self.ser) / len(self.ser) 
        self.ucl = self.centerline + (lookup(table="IndividualXR", columb="E2", n=r) * (sum(mran) / (len(mran) - 1)))
        self.lcl = self.centerline - (lookup(table="IndividualXR", columb="E2", n=r) * (sum(mran) / (len(mran) - 1)))
        return self.plotter(batch)

    def XMR(self, r:int, batch="") -> None: 
        self.type = "X-mR̄"

        mran:list[float] = [] 
        for i in range(1, len(self.ser)): 
            mran.append(abs((self.ser[i-1]) - self.ser[i])) 

        self.ser = mran 
        self.centerline = sum(mran) / (len(mran) - 1)
        self.ucl:float = lookup(table="MediamXR", columb="D4", n=r)  * (sum(mran) / (len(mran) - 1))
        self.lcl:float = lookup(table="MediamXR", columb="D3", n=r)  * (sum(mran) / (len(mran) - 1))

        return self.plotter(batch)  

    def Xbar(self): 
        # to properly define this you need the splitter function to 
        pass 

    def Rbar(self): 
        pass 
