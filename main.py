import os
import numpy as np
import matplotlib.pyplot as plt
from sort import bubble_sort
from load_data import load_data




def main():
   
    dat = load_data('activity.csv')
    sorted_power_W = bubble_sort(dat['PowerOriginal'])
    time = list(range(len(sorted_power_W)))
    time_1 = np.array(time) / 60


    plt.plot(time_1, sorted_power_W)
    plt.xlabel('t/min')
    plt.ylabel('Power (W)')
    plt.title('Sorted Power Data')
    

    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/sorted_power.png", dpi = 300)

    plt.show()
    
if __name__ == "__main__":
    main()


