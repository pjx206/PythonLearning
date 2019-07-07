import sys, os
import time, random
import numpy as np
import wave, argparse, pygame
from collections import deque
from matplotlib import pyplot as plt


def generateNote(freq):
    nSample = 44100
    sampleRate = 44100
    N = int(sampleRate/ freq)

    buf = deque([random.random() - 0.5 for i in range(N)])
    samples = np.array([0] * nSample, 'float32')
    for i in range(nSamples):
        samples[i] = buf[0]
        avg = 0.5 * (buf[0] + buf[1])
        buf.append(avg * 0.995)
        buf.popleft()
    samples = np.array(samples * 32767, 'int16')
    return samples.tostring()

def writeWave(fname, data):
    file = wave.open(fname, 'wb')
    nChannels = 1
    sampleWidth = 2
    frameRate = 44100
    nFrames = 44100
    file.setparams((nChannels, sampleWidth, frameRatem nFrames, 'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close


class NotePlayer:
    def __init__(self):
        pygame.mixer.pre_init(4410, -16, 1, 2048)
        pygame.init()
        self.notes = {}
    
    def add(self, fileName):
        self.notes[filename] = pygame.mixer.Sound(fileName)
    
    def play(self, fileName):
        try:
            self.notes[fileName].play()
        except:
            print(fileName + ' not found')
    
    def playRandom(self):
        """play a random note"""
        index = random.randint(0, len(self.note) - 1)
        note = list(self.notes.values())[index]
        note.play()

def  main():
    pass