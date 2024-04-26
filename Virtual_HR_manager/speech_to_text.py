import pyaudio
import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Capture microphone input
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)
    
    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)  # Use Google Speech Recognition API
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Call the function to convert speech to text
transcription = speech_to_text()
if transcription:
    print("You said:", transcription)
