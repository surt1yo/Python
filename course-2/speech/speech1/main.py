# You'll build a Voice Analysis Lab that records 
# two samples of your voice, measures their 
# properties (duration, average amplitude, 
# maximum amplitude), compares them numerically,
# displays the comparison results, and visualizes 
# both waveforms side-by-side. This is real 
# scientific analysis code - the same approach 
# used in audio engineering, quality assurance, and AI research.
# pyaudio → microphone input
# numpy → audio sample processing
# matplotlib → waveform graph
# wave → save .wav file
# speech_recognition → speech-to-text
# threading → record + wait for Enter simultaneously
import threading 
import sys 
import time 
import pyaudio 
import numpy as np 
import matplotlib.pyplot as plt 
import wave 
import speech_recognition as sr 
from speech_recognition import AudioData

stop_event = threading.Event()

# Functions for audio recording and analysis
def wait_for_enter():
    input("Press Enter to stop recording...")
    stop_event.set()

def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    threading.Thread(target=wait_for_enter).start()
    frames=[]
    while not stop_event.is_set():
        frames.append(stream.read(1024))  
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames), 16000, width

def save_audio(audio_data, rate, width, filename):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(audio_data)
    print(f"Audio saved to {filename}")

def transcribe_audio(audio_data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(audio_data, rate, width)
    text = recognizer.recognize_google(audio)
    print(f"Transcribed text: {text}")
    
def plot_waveform(audio_data, rate):
    samples = np.frombuffer(audio_data, dtype=np.int16)
    duration = len(samples) / rate
    time_axis = np.linspace(0, duration, num=len(samples))
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, samples)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

# Constants for audio recording
print("*"*50)
print("Hello AI, Can you hear me?")
print("*"*50)
print("Speak into the microphone to record.")
audio_data,rate,width=record_audio()
save_audio(audio_data, rate, width, "recording.wav")
transcribe_audio(audio_data, rate, width)
plot_waveform(audio_data, rate)