import numpy as np


class TrainGenerator:
    @staticmethod
    def inhomogeneous(time, rate_fnc, time_step=1):
        result = list(range(len(time)))
        for i, t in enumerate(time):
            result[i] = 1 if np.random.uniform() < time_step * rate_fnc(t) else 0
        return result

    @staticmethod
    def homogeneous(time, rate, time_step=1):
        return [1 if np.random.uniform() < time_step * rate else 0 for i in range(len(time))]