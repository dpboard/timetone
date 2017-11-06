import numpy as np
import pyaudio
from apscheduler.schedulers.blocking import BlockingScheduler
import time

scheduler = BlockingScheduler()
p = pyaudio.PyAudio()

sr = 48000
f = 1000

num_samples_a = int(sr * 0.5)
num_samples_b = num_samples_a * 5

x_a = np.arange(num_samples_a)

y_a = (np.sin(2 * np.pi * x_a * f / sr)).astype(np.float32)

x_b = np.arange(num_samples_b)

y_b = (np.sin(2 * np.pi * x_b * f / sr)).astype(np.float32)

s = p.open(format=pyaudio.paFloat32,
           channels=1,
           rate=sr,
           output=True)

scheduler.add_job(s.write, 'cron', [y_a], second='10-45,55-99')
scheduler.add_job(s.write, 'cron', [y_b], second=0)
scheduler.start()

