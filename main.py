from analysis import controlRB, controlXB, dstats
from constants import batchOne,batchTwo,combined,titles


def main() -> None:
    #print(batchTwo)
    #print(batchTwo)
    dstats(combined,"Combined") 
    count = 0 
    while count != len(titles):
        #controlXB(batchTwo, f"{titles[count]}"," (Batch Two)") 
        #controlRB(batchOne, f"{titles[count]}"," (Batch One)")
        count += 1 


if __name__ == "__main__":
    main()
