from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data_list = [[0.9551,0.9728,0.9599,0.9287,0.9511],
            [0.9711,0.9770,0.9506,0.9607,0.9482],
            [0.9484,0.9738,0.9484,0.9582,0.9729],
            [0.9519,0.9339,0.9489,0.9530,0.9468],
            [0.9465,0.9050,0.9391,0.9546,0.9579],
            [0.9146,0.9054,0.9455,0.9455,0.9179],
            [0.9149,0.5193,0.8626,0.9491,0.9222],
            [0.9078,0.3496,0.8936,0.7213,0.9026],
            [0.4948,0.3600,0.1622,0.5823,0.8738],
            [0.4605, 0.2857,0.1594,0.4391,0.6816]]
data = np.array(data_list)

plt.rc("font", family="Times New Roman", size=14)
df = pd.DataFrame(data.T,columns=['90%','91%','92%','93%','94%','95%','96%','97%','98%','99%'])
settings = {"showfliers":False,
            }
f = df.boxplot(**settings)
plt.xlabel("Test to Total Ratio", size=16)
plt.ylabel("Accuracy", size=16)
# plt.title("Test to Total Ratio Experiment", size=16)
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300 
plt.savefig('/home/wsn/Desktop/HAR/result_figure/Figure_TTR.eps', bbox_inches='tight', restarized=True, format="eps")
plt.show()