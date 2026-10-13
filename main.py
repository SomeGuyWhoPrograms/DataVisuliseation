from analysis import controlRB, controlXB, dstats, OverlayedXB , controlImr
from constants import batchOne,batchTwo,combined,titles

import math 

def main() -> None:
    print("=================")
    print("Generating Control charts")
    print("=================")

    count = 0 
    while count != len(titles):
        #OverlayedXB(batchOne, batchTwo,f"{titles[count]}")
        controlImr(batchTwo,f"{titles[count]}")
        controlXB(batchTwo, f"{titles[count]}") 
        controlRB(batchTwo, f"{titles[count]}")
        count += 1 
        
    print("=================")
    print("Process Compleate")
    print("=================")


if __name__ == "__main__":
    main()
