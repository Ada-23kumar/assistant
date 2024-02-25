import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        voice = listener.listen(source, timeout=5)  # Set a timeout to avoid indefinite listening
        print("Recognizing...")

        command = listener.recognize_google(voice)
        print(f"You said: {command}")

except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
