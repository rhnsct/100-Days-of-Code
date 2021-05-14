from tkinter import *
from quiz_brain import QuizBrain
from data import parameters


THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text=f"Score: 0", font=("Arial", 10, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0,)
        
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 
                                                   125, 
                                                   text="Text Here", 
                                                   font=("Arial", 15, "italic"),
                                                   width=280,
                                                   fill="#040024"
                                                   )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(bd=0, image=true_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(column=0, row=2)
        
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(bd=0, image=false_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(column=1, row=2) 
        
        self.get_next_question()
        
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question)
        else:
            self.canvas.itemconfig(self.canvas_text, 
                                   text=f"You have reached the end of the quiz.\nFinal score: {self.quiz.score}/{parameters['amount']}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
        
    def is_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score: {self.quiz.score}")


    def is_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        

    def give_feedback(self, is_right):
        if is_right: 
            
            self.canvas.config(bg="#B2EAB3")
            
        else:
            self.canvas.config(bg="#EA7F7F")
            
        
        self.window.after(800, self.get_next_question)
    
