from voice_engine import VoiceEngine
from safe_eval import evaluate

def main():
    engine = VoiceEngine()
    print("🎙️ Voice Calculator — say a math expression or type 'quit' to exit.")
    while True:
        choice = input("Enter 'v' to speak or type an expression: ").strip()
        if choice.lower() in ['quit', 'q']:
            break

        if choice.lower() == 'v':
            try:
                print("Listening... (speak now)")
                text = engine.listen_once()
                print("Heard:", text)
            except Exception as e:
                print("Error listening:", e)
                engine.say("I didn't catch that. Please try again.")
                continue
        else:
            text = choice

        try:
            result = evaluate(text)
            out = f"Result: {result}"
            print(out)
            engine.say(f"The result is {result}")
        except Exception as e:
            print("Could not evaluate expression:", e)
            engine.say("I could not evaluate that expression.")

if __name__ == '__main__':
    main()

