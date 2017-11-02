import numpy as np
import matplotlib.pyplot as plt

frequency = 100
interval = 10000
num_cells = 1

spikes = []
for i in range(num_cells):
    isi = np.random.poisson(1000 / frequency, interval)
    spikes.append(np.cumsum(isi))

spikes = spikes[0]
variation = np.std(isi)**2
print("Variation: " + str(variation))
print("Coefficient of variation: " + str(variation / (1000 / frequency)))

for size in [1, 5, 10, 20, 50, 100]:
    max_spike_interval = 10000
    interval_size = size
    interval_count = spikes[-1] // interval_size
    n_spikes = [0 for i in range(interval_count)]

    for spike in spikes:
        index = (spike // interval_size)
        if index < interval_count:
            n_spikes[index] += 1

    print("Fano " + str(interval_size) + ": " + str(np.std(n_spikes)**2 / (interval_size / 100)))

#plt.hist(n_spikes, bins=np.arange(30), align='left', ec='black')
plt.hist(isi, bins=np.arange(30), align='left', ec='black')
plt.xlabel("Interspike interval [ms]")
plt.ylabel("Number of occurencies")
plt.show()