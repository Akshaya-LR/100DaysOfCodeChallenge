from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#F7DBF0"
COLOR = "#423F3E"

class QuizApp:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz ZApp!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score : 0", fg="#171010", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=210, bg=COLOR)
        self.question_text = self.canvas.create_text(
            150, 105, width=210, text="Some question", fill=COLOR, font=('Calibre', 15))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true = PhotoImage(file="images/right.png")
        self.true_button = Button(text="Right", image=true, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=0, row=2)

        false = PhotoImage(file="images/wrong.png")
        self.false_button = Button(text="Wrong", image=false, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=COLOR)
            # print(self.quiz.score)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.", fill=COLOR)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(2000, self.reveal_score)

    def reveal_score(self):
        # print(self.quiz.score)
        self.canvas.itemconfig(self.question_text, text=f"Your final score is: "
                                                        f"{self.quiz.score}/{self.quiz.question_number}", fill=COLOR)

    def true_answer(self):
        self.show_answer(self.quiz.check_answer("True"))

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.show_answer(is_right)

    def show_answer(self, is_right):
        if is_right:
            self.canvas.config(bg="#7FC8A9")
            self.canvas.itemconfig(self.question_text, text="WOOHOO!!\nYOU GOT IT RIGHT", fill="white")
        else:
            self.canvas.config(bg="#FF9A8C")
            self.canvas.itemconfig(self.question_text, text="OOPS..\nYOU GOT IT WRONG", fill="white")
        self.window.after(1000, self.get_next_question)

