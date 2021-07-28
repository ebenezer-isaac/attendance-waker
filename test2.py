import speech_recognition as sr
import asyncio




# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()
while(True):
    with sr.Microphone() as source:   # using microphone here, would like to use speaker instead
        print("Talk Something...")
        audio=r.listen(source)
        print("got the audio")
        try:
            text = r.recognize_google(audio)
            print(text)
        except Exception as e:
            print(e)
            print("Didn't understand the audio")