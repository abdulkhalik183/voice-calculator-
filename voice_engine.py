import speech_recognition as sr
import pyttsx3

class VoiceEngine:
    def __init__(self, tts_rate: int = 150):
        # Recognizer
        self.recognizer = sr.Recognizer()
        # TTS engine
        self.tts = pyttsx3.init()
        self.tts.setProperty('rate', tts_rate)

    def listen_once(self, timeout: float = 5, phrase_time_limit: float = 7) -> str:
        """Listen from the default microphone once and return recognized text."""
        with sr.Microphone() as source:
            print("🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.4)
            audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"✅Recognized: {text}")
            return text
        except sr.UnknownValueError:
            raise Exception("Could not understand audio")
        except sr.RequestError as e:
            raise Exception(f"Speech recognition request failed: {e}")

    def say(self, text: str):
        """Speak the given text aloud using TTS."""
        print(f"🗣️ Saying: {text}")
        self.tts.say(text)
        self.tts.runAndWait()

