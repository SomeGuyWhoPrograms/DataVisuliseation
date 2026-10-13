import pandas as pd 

def buildfile(file:str) -> pd.DataFrame: 
    data = pd.read_csv(file) 
    try:
        data = data.drop(columns="ID") 
    except: 
        return data 
    return data  

def split(df=buildfile("ConstCsvs/Hingemes.csv"))-> tuple[pd.DataFrame,pd.DataFrame]: 
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

def lookup(table:str, columb:str, n:int) -> float : 
    #IndividualsXR , MediamXRconstants , XRSconstants 
    ControlConst: dict[str, pd.DataFrame] = { 
        "XRSconst":buildfile("ConstCsvs/XRSconstants.csv"), 
        "IndividualXR":buildfile("ConstCsvs/IndividualsXR.csv"),
        "MediamXR":buildfile("ConstCsvs/MediamXRconstants.csv") 
    }   
    match table: 
        case "XRSconst": 
            df = ControlConst["XRSconst"] 
        case "IndividualXR": 
            df = ControlConst["IndividualXR"]
        case "MediamXR": 
            df = ControlConst["MediamXR"] 
        case _: 
            raise Exception("Table must be one of MediamXR, IndividualXR, XRSconst") 

    df = df.reset_index(drop=True) 
    df = df.set_index("n")

    try:
        ser = df[columb][n]  
    except: 
        raise Exception(f"Invalid Table value the table contains {df.columns}")

    if isinstance(ser, float) == False: 
        raise Exception("Invalid Table value")  
    
    return ser 

batchOne:pd.DataFrame = split()[0] 
batchTwo:pd.DataFrame = split()[1] 
combined:pd.DataFrame = buildfile("ConstCsvs/Hingemes.csv")  
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
    "Left Teardrop Length":10.0,   
    "Left Teardrop Depth":1.5,   
    "Right Teardrop Length":10.0,   
    "Right Teardrop Depth":1.5, # This is inffered 
    "Distance Between knuckles":53.0,
    "Width Without Knuckle":36.0,
    "Width With Knuckle":(44.45 +(13/2))   # This is inferd from the length of one end of the hindge to the hole centre + radius 
}





