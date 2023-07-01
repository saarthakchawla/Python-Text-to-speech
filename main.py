
import win32com.client as wc
speaker = wc.Dispatch("SAPI.SpVoice")

while True:
    x = input("Enter what to speak: ")
    if x=="q":
        speaker.Speak("Good Bye")
        break
    else:
        speaker.Speak(x)


