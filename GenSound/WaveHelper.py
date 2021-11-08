import wave
import struct
import numpy as np
from enum import Enum

class Note(Enum):
    C3 = 8.176
    C3_s = 8.662
    D3 = 9.177
    D3_s = 9.723
    E3 = 10.301
    F3 = 10.913
    F3_s = 11.562
    G3 = 12.250
    G3_s = 12.978
    A3 = 13.750
    A3_s = 14.568
    B3 = 15.434
    C2 = 16.352
    C2_s = 17.324
    D2 = 18.354
    D2_s = 19.445
    E2 = 20.602
    F2 = 21.827
    F2_s = 23.125
    G2 = 24.500
    G2_s = 25.957
    A2 = 27.500
    A2_s = 29.135
    B2 = 30.868
    C1 = 32.703
    C1_s = 34.648
    D1 = 36.708
    D1_s = 38.891
    E1 = 41.203
    F1 = 43.654
    F1_s = 46.249
    G1 = 48.999
    G1_s = 51.913
    A1 = 55.000
    A1_s = 58.270
    B1 = 61.735
    C = 65.406
    C_s = 69.296
    D = 73.416
    D_s = 77.782
    E = 82.407
    F = 87.307
    F_s = 92.499
    G = 97.999
    G_s = 103.826
    A = 110.000
    A_s = 116.541
    B = 123.471
    c = 130.813
    c_s = 138.591
    d = 146.832
    d_s = 155.563
    e = 164.814
    f = 174.614
    f_s = 184.997
    g = 195.998
    g_s = 207.652
    a = 220.000
    a_s = 233.082
    b = 246.942
    c1 = 261.626
    c1_s = 277.183
    d1 = 293.665
    d1_s = 311.127
    e1 = 329.628
    f1 = 349.228
    f1_s = 369.994
    g1 = 391.995
    g1_s = 415.305
    a1 = 440.000
    a1_s = 466.164
    b1 = 493.883
    c2 = 523.251
    c2_s = 554.365
    d2 = 587.330
    d2_s = 622.254
    e2 = 659.255
    f2 = 698.456
    f2_s = 739.989
    g2 = 783.991
    g2_s = 830.609
    a2 = 880.000
    a2_s = 932.328
    b2 = 987.767
    c3 = 1046.502
    c3_s = 1108.731
    d3 = 1174.659
    d3_s = 1244.508
    e3 = 1318.510
    f3 = 1396.913
    f3_s = 1479.978
    g3 = 1567.982
    g3_s = 1661.219
    a3 = 1760.000
    a3_s = 1864.655
    b3 = 1975.533
    c4 = 2093.005
    c4_s = 2217.461
    d4 = 2349.318
    d4_s = 2489.016
    e4 = 2637.020
    f4 = 2793.826
    f4_s = 2959.955
    g4 = 3135.963
    g4_s = 3322.438
    a4 = 3520.000
    a4_s = 3729.310
    b4 = 3951.066
    c5 = 4186.009
    c5_s = 4434.922
    d5 = 4698.636
    d5_s = 4978.032
    e5 = 5274.041
    f5 = 5587.652
    f5_s = 5919.911
    g5 = 6271.927
    g5_s = 6644.875
    a5 = 7040.000
    a5_s = 7458.620
    b5 = 7902.133
    c6 = 8372.018
    c6_s = 8869.844
    d6 = 9397.273
    d6_s = 9956.063
    e6 = 10548.082
    f6 = 11175.303
    f6_s = 11839.822
    g6 = 12543.854
    g6_s = 13289.750
    a6 = 14080.000
    a6_s = 14917.240
    b6 = 15804.266


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


def chord(*notes, framerate=44100, time=1):
    wave = sum(sin_wave(100, note.value, framerate, 0, time) for note in notes)
    wave = normalize_wave(wave, 0x7fff).astype(np.int16)
    return wave