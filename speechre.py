import pyaudio
import wave
import speech_recognition as sr
#import subprocess
import pyttsx3
from commands import commander




#def echo(text):
  #  subprocess.call('cscript "C:\Program Files\Jampal\ptts.vbs" ',shell=True)
  #  subprocess.call(text,shell=True)
def echo(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

running=True
cmd=commander()
def play_audio(filename):
    chunk=1024
    wf=wave.open(filename,'rb')
    pa=pyaudio.PyAudio()

    stream=pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True

    )

    data_stream=wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream=wf.readframes(chunk)

    stream.close()
    pa.terminate()

r=sr.Recognizer()
command=""
def initSpeech():
    global command
    print("Listening......")

    play_audio("./audio/sms-alert-5-daniel_simon.wav")


    with sr.Microphone() as source:
        print("say something....")
        audio=r.record(source, duration=5)

    play_audio("./audio/sms-alert-5-daniel_simon.wav")


    try:
        global running
        command=r.recognize_google(audio)
        print("your command:  ")
        print(command)
        echo("You said" + command)
        cmd.discover(command)
        if command=="quit" or command=="exit":
            running=False


    except:
        print("Not understood. Please try again")


while running == True:
    initSpeech()
