import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play

def record_participant(name,duration):
    chunk = 1024
    audioformat = pyaudio.paInt16
    # dual channel = stereo
    channels = 2
    #sample rate
    sample_rate = 44100

    #initialize PyAudio object
    audio = pyaudio.PyAudio()
    
    stream = audio.open( format = audioformat,
                         channels = channels,
                         rate = sample_rate,
                         input = True,
                         output = True,
                         frames_per_buffer = chunk)
    frames = []

    print(f'Start Recording {name}.wav')
    
    for i in range(int(sample_rate/chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
        
    print(f'Stop Recording {name}.wav')
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf = wave.open(name+".wav","wb")
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(audioformat))
    wf.setframerate(sample_rate)
    #write the frame as bytes
    wf.writeframes(b"".join(frames))
    wf.close()
def listen_record(name):
    audio_file = AudioSegment.from_wav(name+".wav")
    play(audio_file)
    
    
