# You'll build a Voice Analysis Lab that records 
# two samples of your voice, measures their properties 
# (duration, average amplitude, maximum amplitude), 
# compares them numerically, displays the comparison 
# results, and visualizes both waveforms side-by-side. 
# This is real scientific analysis code - 
# the same approach used in audio engineering, 
# quality assurance, and AI research.
import threading, sys, time, pyaudio, numpy as np 
import matplotlib.pyplot as plt, wave, speech_recognition as sr
from speech_recognition import AudioData
from colorama import Fore, Style

stop_event = threading.Event()

# Functions for audio recording and analysis
def wait_for_enter():
    input(f"{Fore.GREEN}Press Enter to stop recording...{Style.RESET_ALL}")
    stop_event.set()

def record_audio(label):
    stop_event.clear()
    print(f"{Fore.GREEN}{label}{Style.RESET_ALL}")
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

def transcribe_audio(audio_data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(audio_data, rate, width)
    text = recognizer.recognize_google(audio)
    return (f"{Fore.GREEN}Transcribed text: {text}{Style.RESET_ALL}")

def analyze_audio(audio_data, rate):
    samples = np.frombuffer(audio_data, dtype=np.int16)
    return {
        "duration": len(samples) / rate,
        "avg_volume": np.mean(np.abs(samples)),
        "max_volume": np.max(np.abs(samples)),
        "samples": samples
    }

def display_stats(stats, text, label):
    print(f"{Fore.GREEN}{label} Analysis:{Style.RESET_ALL}")
    print(f"  Duration: {stats['duration']:.2f} seconds")
    print(f"  Average Volume: {stats['avg_volume']:.2f}")
    print(f"  Maximum Volume: {stats['max_volume']:.2f}")
    print(f"  Transcribed Text: {text}")

def compare(stats1, stats2):
    if stats1['duration'] > stats2['duration']:
        print(f"{Fore.GREEN}First recording is longer.{Style.RESET_ALL}")
    if stats1['duration'] < stats2['duration']:
        print(f"{Fore.GREEN}Second recording is longer.{Style.RESET_ALL}")
    if stats1['avg_volume'] > stats2['avg_volume']:
        print(f"{Fore.GREEN}First recording is louder on average.{Style.RESET_ALL}")
    if stats1['avg_volume'] < stats2['avg_volume']:
        print(f"{Fore.GREEN}Second recording is louder on average.{Style.RESET_ALL}")
    if stats1['max_volume'] > stats2['max_volume']:
        print(f"{Fore.GREEN}First recording has a louder peak.{Style.RESET_ALL}")
    if stats1['max_volume'] < stats2['max_volume']:
        print(f"{Fore.GREEN}Second recording has a louder peak.{Style.RESET_ALL}")
    

# Constants for audio recording    
print("*"*50)
print(f"{Fore.GREEN}VOICE ANALYSIS LAB{Style.RESET_ALL}")
print("*"*50)
print(f"{Fore.GREEN}Record twice and compare your voice.{Style.RESET_ALL}")

audio1, rate, width = record_audio(f"{Fore.GREEN}Recording once, speak normally.{Style.RESET_ALL}")
stats1 = analyze_audio(audio1, rate)
text1 = transcribe_audio(audio1, rate, width)
display_stats(stats1, text1, "First Recording")

audio2, rate, width = record_audio(f"{Fore.GREEN}Recording again, speak louder.{Style.RESET_ALL}")
stats2 = analyze_audio(audio2, rate)
text2 = transcribe_audio(audio2, rate, width)
display_stats(stats2, text2, "Second Recording")

compare(stats1, stats2)
