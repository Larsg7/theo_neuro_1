import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from train_generator import TrainGenerator


def gen_child_train(parent_train, p, jitter_spread=0, jitter_center=0.0):
    result = np.zeros(len(parent_train))
    for index, e in enumerate(parent_train):
        if np.random.uniform() < p and e != 0:
            jitter = np.random.normal(jitter_center, jitter_spread)
            index = int(index + jitter)
            result[max(0, min(index, len(result) - 1))] = e
            print(index, jitter)
    return result

##### a) #####

max_time = 1
time_step = 0.01
rate = 60
p = 0.1
time = np.arange(-max_time, max_time, time_step)

parent_train = TrainGenerator.homogeneous(time, rate, time_step)
child_train = gen_child_train(parent_train, p)

# rate_child = p * rate_parent
print("Rate of child with p={}, r_0={}: {:0.1f}".format(p, rate, sum(child_train) / max_time / 2))

plt.plot(time, parent_train)
plt.plot(time, child_train)
plt.show()

##### b) #####

child_train = gen_child_train(parent_train, p, 0)

plt.plot(time, signal.correlate(parent_train, child_train, "same"))
plt.show()

##### c) #####

omega = np.pi * 50
rate1 = lambda t: 60 * np.sin(omega * t) ** 2
parent_train = TrainGenerator.inhomogeneous(time, rate1, time_step)
child_train = gen_child_train(parent_train, 1, 0, - 0.2 / time_step)

plt.plot(time, signal.correlate(parent_train, child_train, "same"))
plt.show()
