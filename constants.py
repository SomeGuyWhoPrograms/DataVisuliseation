import pandas as pd 

def buildfile(file:str) -> pd.DataFrame: 
    data = pd.read_csv(file) 
    data = data.dropna()  
    data = data.drop(columns="ID")
    return data  

def split(df=buildfile("Hingemes.csv"))-> tuple[pd.DataFrame,pd.DataFrame]: 
    batchone:pd.DataFrame = df.drop(labels=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]).reset_index(drop=True) 
    batchtwo:pd.DataFrame = df.drop(labels=[20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]).reset_index(drop=True)
    return batchone , batchtwo # if you want sepperate plots you have to change the lables 


batchOne:pd.DataFrame = split()[0] 
batchTwo:pd.DataFrame = split()[1] 
combined: pd.DataFrame = buildfile("Hingemes.csv")  

titles = {
    0:"Length Without Knuckles",
    1:"Length With Knuckles",
    2:"Left Knuckle Length",
    3:"Left Knuckle Pin Gap",
    4:"Left Knuckle Pin Gap (swelling)",
    5:"Left Knuckle Thickness From Centre",
    6:"Left Knuckle Thickness From (swelling)",
    7:"Right Knuckle Length",
    8:"Right Knuckle Pin Gap",
    9:"Right Knuckle Pin Gap (swelling)",
    10:"Right Knuckle Thickness From Centre",
    11:"Right Knuckle Thickness From (swelling)",
    12:"Left Teardrop Length",
    13:"Left Teardrop Depth",
    14:"Right Teardrop Length",
    15:"Right Teardrop Depth",
    16:"Distance Between knuckles",
    17:"Width Without Knuckle",
    18:"Width With Knuckle"
    }

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


