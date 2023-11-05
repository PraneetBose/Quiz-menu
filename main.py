import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz App")

        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['Paris', 'London', 'Berlin', 'Rome'],
                'correct': 0
            },
            {
                'question': 'Which planet is known as the "Red Planet"?',
                'options': ['Mars', 'Venus', 'Jupiter', 'Mercury'],
                'correct': 0
            }
            # Add more questions
        ]

        self.current_question = 0
        self.score = 0

        self.label = tk.Label(root, text="", font=('Arial', 16))
        self.label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)

        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(root, variable=self.radio_var, value=i)
            self.radio_buttons.append(radio)
            radio.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.label.config(text=question_data['question'])
            for i, radio in enumerate(self.radio_buttons):
                radio.config(text=question_data['options'][i])
            self.radio_var.set(-1)
        else:
            self.show_score()

    def check_answer(self):
        selected_option = self.radio_var.get()
        if selected_option == self.questions[self.current_question]['correct']:
            self.score += 1
        self.current_question += 1
        self.next_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour score: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
