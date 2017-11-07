import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from train_generator import TrainGenerator

##### a) #####

omega = np.pi
rate1 = lambda t: 60 * np.sin(omega * t) ** 2
rate2 = lambda t: 60 * np.cos(omega * t) ** 2

max_time = 1
time_step = 0.01
time = np.arange(-max_time, max_time, time_step)

train1 = TrainGenerator.inhomogeneous(time, rate1, time_step)
train2 = TrainGenerator.inhomogeneous(time, rate2, time_step)

correlation = signal.correlate(train1, train2, "same")

plt.plot(time, correlation)
# Does the same thing, only slower...
# plt.plot(time, cross_correlation(time, train1, train2, time_step))
#plt.show()

# when omega >> r_0 the frequency of the correlation function increases until its just 0

##### b) #####

rate3 = lambda t: 60 * np.cos(omega * (t - 0.3)) ** 2

plt.plot(time, signal.correlate(train1, TrainGenerator.inhomogeneous(time, rate3, time_step), "same"))
plt.show()


