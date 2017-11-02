import numpy as np
import matplotlib.pyplot as plt

frequency = 100
interval = 1000
num_cells = 1

spikes = []
for i in range(num_cells):
    isi = np.random.poisson(1000  / frequency, interval)
    spikes.append(np.cumsum(isi))

variation = np.std(isi)**2
print("Variation: " + str(variation))
print("Coefficient of variation: " + str(variation / (1000 / frequency)))

max_spike_interval = 1000
num_intervals = 10
n_spikes = [0 for i in range(num_intervals)]

for spike in spikes[0]:
    index = (spike // (max_spike_interval // num_intervals))
    if index < num_intervals:
        n_spikes[index] += 1

print("Fano: " + str(np.std(n_spikes) / 1))

plt.hist(n_spikes, bins=np.arange(30), align='left', ec='black')
#plt.hist(isi, bins=np.arange(30), align='left', ec='black')
#plt.show()
