"""
    Re-apply today's concepts of audio capture, 
    digitization, and speech recognition by building 
    a self-contained Python tool that records your voice, 
    transcribes it with Google Speech-to-Text, and plots its waveform.
                                                                        """
import threading, pyaudio, numpy as np
import matplotlib.pyplot as plt, wave, speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()

# wait for enter to stop
def wait_for_enter():
    input("Press Enter to stop recording...\n")
    stop_event.set()

# record audio asap
def record_audio():
    stop_event.clear()
    print("Recording... speak now")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)

    threading.Thread(target=wait_for_enter).start()

    frames = []
    while not stop_event.is_set():
        frames.append(stream.read(1024))

    stream.stop_stream()
    stream.close()

    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()

    return b''.join(frames), 16000, width

# save wav file
def save_wav(audio_data, rate, width):
    with wave.open("speech.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(audio_data)

# plot waveform
def plot_waveform(audio_data):
    samples = np.frombuffer(audio_data, dtype=np.int16)
    plt.plot(samples)
    plt.title("Waveform")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.show()

# transcribe + save text
def transcribe_audio(audio_data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(audio_data, rate, width)

    try:
        text = recognizer.recognize_google(audio)
    except:
        text = "Could not understand audio"

    # save to txt
    with open("speech.txt", "w") as f:
        f.write(text)

    print("Transcription:", text)


# run
audio, rate, width = record_audio()

save_wav(audio, rate, width)
print("Saved as speech.wav")

plot_waveform(audio)

transcribe_audio(audio, rate, width)
print("Saved as speech.txt")