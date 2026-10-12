import pandas as pd 

def buildfile(file:str) -> pd.DataFrame: 
    data = pd.read_csv(file) 
    data = data.dropna()  
    data = data.drop(columns="ID")
    return data  

def split(df=buildfile("Hingemes.csv"))-> tuple[pd.DataFrame,pd.DataFrame]: 
    # You can split it at any point in the data i defult to 19 because thats where I split from this can work for more devides if you want it 
    def get_devide(split:int,start=0)->list[int]:
        todrop = [] 
        for i in range(start,split+1): 
            todrop.append(i)
        return todrop

    batchone:pd.DataFrame = df.drop(labels=get_devide(18)).reset_index(drop=True) 
    start:int = len(batchone.columns)  
    batchtwo:pd.DataFrame = df.drop(labels=get_devide(len(df)-1,start)).reset_index(drop=True)
    return batchone , batchtwo  

batchOne:pd.DataFrame = split()[0] 
batchTwo:pd.DataFrame = split()[1] 
combined:pd.DataFrame = buildfile("Hingemes.csv")  

titles = combined.columns

idealhingeMesurments:dict[str,float] = {
    "Length Without Knuckles":101.6,
    "Length With Knuckles":101.6,
    "Left Knuckle Length":round(((101.6 - 52.80) / 2),2),
    "Left Knuckle Pin Gap":6.90,
    "Left Knuckle Pin Gap (swelling)":7.05,   #This is infered form the drawing may be the wrong thing 
    "Left Knuckle Thickness From Centre":3.0,
    "Left Knuckle Thickness From (swelling)":3.0,
    "Right Knuckle Length":round(((101.6 - 52.80) / 2),2),
    "Right Knuckle Pin Gap":6.90,
    "Right Knuckle Pin Gap (swelling)":7.05,   #This is infered form the drawing may be the wrong thing 
    "Right Knuckle Thickness From Centre":3.0,
    "Right Knuckle Thickness From (swelling)":3.0,
    "Left Teardrop Length":0.0,   # From what part of the hinge did you take thees mesurments?? 
    "Left Teardrop Depth":0.0,   # The drawing dosent have mesurments simular to thees for me to guess what they are 
    "Right Teardrop Length":0.0,   
    "Right Teardrop Depth":0.0, 
    "Distance Between knuckles":53.0,
    "Width Without Knuckle":36.0,
    "Width With Knuckle":(44.45 +(13/2))   # This is inferd from the length of one end of the hindge to the hole centre + radius 
}


