import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# sample frequency
freq = 44100

# recording duration
duration = 5

# Start recorder with the given values
recording = sd.rec(int(duration * freq), samplerate= freq, channels=2)

# record audio for the given number of seconds
sd.wait()

# this will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)

# convert the NumPy array to audio file

wv.write("recording1.wav", recording, freq, sampwidth=2)
