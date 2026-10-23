# First Plotting of SMAP and MSL Data
# Author: Carson Mead
# Date: 10/22/26

# Including libraries
import numpy as np
import matplotlib as plt

# Loading clean data
clean = np.load("./JPL Data/data/data/train/A-2.npy")

print("Clean Training Data Shape:", clean)

# Plot the first channel parameter to see what "clean" spacecraft telemetry looks like
plt.pyplot.figure(figsize=(10, 4))
plt.pyplot.plot(np.arange(len(clean))*10,clean[:, 0], color='blue', label='Clean Telemetry (Nominal)')
plt.pyplot.title("NASA SMAP Channel A-2 (Clean Training Set)")
plt.pyplot.xlabel("Time (min)")
plt.pyplot.ylabel("Normalized Signal Value")
plt.pyplot.legend()
plt.pyplot.grid(True)
plt.pyplot.show()