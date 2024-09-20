import speech_recognition as sr

def speech():
    mic = sr.Microphone() 
    recog = sr.Recognizer()
    
    with mic as audio_file: 
        print("Speak Please")
        recog.adjust_for_ambient_noise(audio_file)

        audio = recog.listen(audio_file)
        print("You said: " + recog.recognize_google(audio, language="Ru-ru"))

        return recog.recognize_google(audio, language="Ru-ru")
    
