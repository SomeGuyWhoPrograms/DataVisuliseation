import matplotlib.pyplot as plt 
import matplotlib.animation as ani   
from pandas import DataFrame , Series
from typing import TypedDict  

""" 
class shape(TypedDict): 
    centerline:float
    ucl:float 
    lcl:float
    type:str  
    sname:str 
    data:DataFrame  
    ser:Series
""" 

class Plots:
    def __init__(self, obj) -> None:
        self.obj = obj
    
    def Test(self ,batch="") -> None: 
        plt.figure(figsize=(10, 8))
        plt.title(f"{self.obj.type} Control Diagram\n{self.obj.name} {batch}", size=25)
        plt.xlabel("Number of Observations", size=15) 
        plt.ylabel("Measured Values (mm)", size=15)  

        lim:int = len(self.obj.ser)
        while (lim % 5) != 0: 
            lim += 1  

        label: list[str] = ['0']
        for i in range(5,len(self.obj.ser),5): 
            label.append(f"{i}")
        label.append(f"{lim}")

        plt.xticks(range(-1,lim,5),
                labels=label
                )
        plt.xlim(-1, xmax=lim)
        plt.ylim(ymin=self.obj.lcl-0.25, ymax=self.obj.ucl+0.25)

        plt.text(lim+0.5, self.obj.centerline-0.005, f"{self.obj.type}", style='italic',fontsize=18)
        plt.text(lim+0.5, self.obj.ucl-0.005, 'UCL', style='italic',fontsize=18)
        plt.text(lim+0.5, self.obj.lcl-0.005, 'LCL', style='italic',fontsize=18)

        plt.plot(range(0, len(self.obj.ser)), self.obj.ser, marker=".", color="b")
        plt.plot([-1,lim], [self.obj.lcl,self.obj.lcl], ls="dashed", color="r", label="UCL") 
        plt.plot([-1,lim], [self.obj.centerline,self.obj.centerline], color="k", ls="dotted", label="Center line") 
        plt.plot([-1,lim], [self.obj.ucl,self.obj.ucl], ls="dashed", color="r",label="LCL") 

        plt.grid(lw=0.5)  
        plt.show()

    def Plot(self, batch="") -> None:
        plt.figure(figsize=(10, 8))
        plt.title(f"{self.obj.type} Control Diagram\n{self.obj.name} {batch}", size=25)
        plt.xlabel("Number of Observations", size=15) 
        plt.ylabel("Measured Values (mm)", size=15)  

        lim:int = len(self.obj.ser)
        while (lim % 5) != 0: 
            lim += 1  

        label: list[str] = ['0']
        for i in range(5,len(self.obj.ser),5): 
            label.append(f"{i}")
        label.append(f"{lim}")

        plt.xticks(range(-1,lim,5),
                labels=label
                )
        plt.xlim(-1, xmax=lim)
        plt.ylim(ymin=self.obj.lcl-0.25, ymax=self.obj.ucl+0.25)

        plt.text(lim+0.5, self.obj.centerline-0.005, f"{self.obj.type}", style='italic',fontsize=18)
        plt.text(lim+0.5, self.obj.ucl-0.005, 'UCL', style='italic',fontsize=18)
        plt.text(lim+0.5, self.obj.lcl-0.005, 'LCL', style='italic',fontsize=18)

        plt.plot(range(0, len(self.obj.ser)), self.obj.ser, marker=".", color="b")
        plt.plot([-1,lim], [self.obj.lcl,self.obj.lcl], ls="dashed", color="r", label="UCL") 
        plt.plot([-1,lim], [self.obj.centerline,self.obj.centerline], color="k", ls="dotted", label="Center line") 
        plt.plot([-1,lim], [self.obj.ucl,self.obj.ucl], ls="dashed", color="r",label="LCL") 

        plt.grid(lw=0.5)  
        plt.savefig(fname=f"Plots/{self.obj.type}/{self.obj.name}{batch}") 
        plt.close() 

    def Animate (self, batch="") -> None: 
        pass 