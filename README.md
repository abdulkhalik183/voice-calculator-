# voice-calculator-
    This project is a voice-based calculator that uses speech recognition and text to speech to perform 
arithmatic and scientific algorithms.
The app:
    > Captures voice input Captures voice input using your system microphone.
    > Converts it to text with the SpeechRecognition library.
    > Evaluates the expression securely (without eval()).
    >Speaks the result using pyttsx3.

  #Features-
    > Voice input using speech_recognition
    > Text-to-speech output with pyttsx3
    > Safe evaluation using AST (no eval)
    > GUI (Tkinter) + CLI support
    > Supports math functions like sin, cos, sqrt, log, etc.
    > Error handling and voice feedback
    > Unit tests for safety and correctness

  #Requirements
    Python 3.8+
    speechrecognition
    pyttsx3
    pyaudio

  #project structure
    voice_calculator
          |
     requirements.txt
          |
     safe_eval.py
          |
     voice_engine.py
          |
     cli_calculator.py
          |
     gui_calculator.py
          |
     tests
         >tests_safe_eval.py

    #installation
       Create and activate a virtual environment:
          python -m venv venv
          # Windows
             venv\Scripts\activate

    #installation requirements
        pip install -r requirements.txt


    #usage
      > cli mode
         python cli_calulator.py
      > Gui mode
         python gui_calculator.py
  -> Type expressions or click buttons.
  -> click the mic button to use input voice.
  -> The result will be spoken aloud.
   # output
![screenshot]()


