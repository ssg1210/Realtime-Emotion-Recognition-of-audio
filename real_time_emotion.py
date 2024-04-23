# Tasks - Completed
# 1. Take input from microphone for 4 sec 
# 2. Extract features from the above 4 seconds audio
# 3. Predict emotion for the above 4 sec
# 4. Repeat

import pyaudio
import struct
from matplotlib import pyplot as plt
import numpy as np
import math
import wave
from live_predict import LivePredictions

# plt.ion()             # Turn on interactive mode so plot gets updated

WIDTH     = 2         # bytes per sample
CHANNELS  = 1         # mono
RATE      = 48000      # Sampling rate (samples/second)
BLOCKSIZE = 1024      # length of block (samples)
DURATION  = 4        # Duration (seconds)

NumBlocks = int( DURATION * RATE / BLOCKSIZE )
CONTINUE=True

print('BLOCKSIZE =', BLOCKSIZE)
print('NumBlocks =', NumBlocks)
print('Running for ', DURATION, 'seconds...')


# Open audio device:
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format    = PA_FORMAT,
    channels  = CHANNELS,
    rate      = RATE,
    input     = True,
    output    = False)


print('* Start')
audio_file_cnt = 0
while CONTINUE:
    frames = []
    print("Starting 4sec..")
    for i in range(0, NumBlocks):
        input_bytes = stream.read(BLOCKSIZE, exception_on_overflow=False)     # Read audio input stream 
        frames.append(input_bytes)
    print("Ending 4sec..")
    output_file = "output_wav_{}.wav".format(audio_file_cnt)
    wf1 = wave.open(output_file, 'w')
    wf1.setnchannels(1)
    wf1.setframerate(RATE)
    wf1.setsampwidth(2)
    wf1.writeframes(b''.join(frames))
    wf1.close()
    audio_file_cnt+=1

    live_prediction = LivePredictions(file=output_file)
    final_prediction = live_prediction.make_predictions()
    print(final_prediction)

print('* End')
stream.stop_stream()
stream.close()
p.close()