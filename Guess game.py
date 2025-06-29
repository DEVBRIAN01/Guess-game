
import tkinter as tk
import random

class GuessGame:
    def __init__(self,root):
        self.root = root
        self.root.title("Guess the Number")
        self.number = random.randint(1, 100)
        self.attempts = 0

        tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14)).pack(pady=10)
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)
        self.feedback = tk.Label(root, text="", font=("Arial", 12))
        self.feedback.pack(pady=5)
        tk.Button(root, text="Guess", command=self.check_guess).pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.number:
                self.feedback.config(text="Too low!", fg="blue")
            elif guess > self.number:
                self.feedback.config(text="Too high!", fg="blue")
            else:
                self.feedback.config(text=f"Correct! Attempts: {self.attempts}", fg="green")
        except ValueError:
            self.feedback.config(text="Enter a valid number.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessGame(root)
    root.mainloop()
