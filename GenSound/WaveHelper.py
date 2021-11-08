import wave,struct
import numpy as np


c1 = 261.626
d1 = 293.665
e1 = 329.628
f1 = 349.228
g1 = 391.995
a1 = 440


def normalize_wave(wave, range_max):
    """map wave to certain range

    Args:
        wave (np.ndarray): wave to be mapped
        range_max (int): max range
    """
    wave_max, wave_min = max(wave), min(wave)
    wave_abs_max = max(abs(wave_max), abs(wave_min))
    mapped_wave = wave / (wave_abs_max / (range_max - wave_abs_max))
    return mapped_wave


def sin_wave(A, f, fs, phi, t):
    Ts = 1/fs
    n = t/Ts
    n = np.arange(n)
    y = A*np.sin(2*np.pi*f*n*Ts + phi * (np.pi/180))
    return y
