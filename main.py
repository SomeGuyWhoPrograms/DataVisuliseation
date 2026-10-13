from analysis import ControlSPC
from constants import batchOne,batchTwo,combined,titles

def main() -> None:
    print("=================")
    print("Generating Control charts")
    print("=================")

    count = 0 
    while count <= len(titles):
        val = ControlSPC(combined, titles[count])  
        val.XMR(2) 
        val.IMR(2)
        count += 1 
        print(f"Plotting {titles[count]}") 
        
    print("=================")
    print("Process Compleate")
    print("=================")


if __name__ == "__main__":
    main()
