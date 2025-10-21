"""Tkinter GUI calculator with voice input button."""
import tkinter as tk
from tkinter import messagebox
from safe_eval import evaluate
from voice_engine import VoiceEngine

class GUICalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Voice Calculator')
        self.geometry('360x480')
        self.resizable(False, False)
        self.engine = VoiceEngine()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.entry_var, font=('Arial', 20), justify='right')
        entry.pack(fill='x', padx=10, pady=10)
        entry.bind('<Return>', lambda e: self.evaluate_expression())

        btns = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','%','+']
        ]
        for row in btns:
            frame = tk.Frame(self)
            frame.pack(fill='x', padx=10)
            for b in row:
                tk.Button(frame, text=b, font=('Arial',18), command=lambda ch=b: self.on_button(ch)).pack(side='left', expand=True, fill='both')

        control_frame = tk.Frame(self)
        control_frame.pack(fill='x', padx=10, pady=10)
        tk.Button(control_frame, text='=', font=('Arial',18), command=self.evaluate_expression).pack(side='left', expand=True, fill='both')
        tk.Button(control_frame, text='C', font=('Arial',18), command=self.clear).pack(side='left', expand=True, fill='both')

        tk.Button(self, text='🎤 Speak', font=('Arial',16), command=self.speak_then_evaluate).pack(fill='x', padx=10)

    def on_button(self, ch):
        self.entry_var.set(self.entry_var.get() + ch)

    def clear(self):
        self.entry_var.set('')

    def evaluate_expression(self):
        expr = self.entry_var.get().strip()
        if not expr:
            return
        try:
            res = evaluate(expr)
            self.entry_var.set(str(res))
            self.engine.say(f"The result is {res}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not evaluate expression: {e}")
            self.engine.say("I could not evaluate that expression")

    def speak_then_evaluate(self):
        try:
            self.engine.say('Listening now')
            text = self.engine.listen_once()
            self.entry_var.set(text)
            self.evaluate_expression()
        except Exception as e:
            messagebox.showwarning('Listen error', str(e))
            self.engine.say('I did not understand. Please try again')

if __name__ == '__main__':
    app = GUICalculator()
    app.mainloop()
