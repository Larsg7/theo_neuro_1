import math
import numpy as np
import matplotlib.pyplot as plt

dt = 0.5
t_max = 500
synaptic_events = [50, 150, 190, 300, 320, 400, 410]


class Neuron:
    def __init__(self):
        self.v_reset = -80
        self.v_th = -54
        self.e_L = -70
        self.tau_m = 10
        self.e_s = 0
        self.r_m_g_s = 0.5
        self.p_max = 0.5
        self.tau_s = 10
        self.e = math.exp(1)
        self.t_m_i_e = 0

        self.v = -80
        self.z = 0
        self.p_s = 0

        self.v_t = []
        self.z_t = []
        self.spikes = []
        self.on_spike: callable = None

    def __calculate_dv(self):
        return (self.e_L - self.v - self.r_m_g_s * self.p_s * (self.v - self.e_s)) / self.tau_m * dt + self.r_m_g_s

    def __calculate_dz(self):
        return -self.z / self.tau_s * dt

    def __calculate_dp_s(self):
        return (self.e * self.p_max * self.z - self.p_s) * dt

    def register_spike(self):
        self.z = 1

    def update(self, t):
        self.v_t.append(self.v)
        self.z_t.append(self.z)
        self.z += self.__calculate_dz()
        self.p_s += self.__calculate_dp_s()
        self.v += self.__calculate_dv()
        if self.v > self.v_th:
            if self.on_spike:
                self.on_spike()
            self.spikes.append(t)
            self.v = self.v_reset

##### Exercise 1 #####


neuron = Neuron()
t = 0

# while t <= t_max:
#     if t in synaptic_events:
#         neuron.register_spike()
#     neuron.update(t)
#     t += dt

# plt.plot(np.arange(0, len(neuron.v_t) * dt, dt), neuron.v_t)

# plt.figure()
# plt.plot(np.arange(0, len(neuron.v_t) * dt, dt), neuron.z_t)
# plt.show()

##### Exercise 2 #####

t_max = 1
dt = 0.1

neuron0 = Neuron()
neuron1 = Neuron()

neuron0.r_m_g_s = neuron1.r_m_g_s = 0.15
neuron0.tau_m = neuron1.tau_m = 20
neuron0.r_m_g_s = neuron1.r_m_g_s = 18
neuron0.e_s = neuron1.e_s = -80
neuron0.on_spike = neuron1.register_spike
neuron1.on_spike = neuron0.register_spike

neuron0.v = -80
neuron1.v = -45

t = 0
time = np.arange(0, t_max + dt, dt)

while t <= t_max:
    neuron0.update(t)
    neuron1.update(t)
    t += dt

plt.plot(time, neuron0.v_t)
plt.plot(time, neuron1.v_t)
print(neuron0.spikes)
plt.show()
