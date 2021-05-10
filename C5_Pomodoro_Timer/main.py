from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    tick.config(text="")
    label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    
    if reps % 2 != 0:
        count_down(work_time)
        label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_time)
        label.config(text="Break", fg=RED)
    else:
        count_down(short_break_time)
        label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global completions
    global reps
    count_min = floor(count / 60)
    count_seconds = count % 60
    
    
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        completions = ""
        for _ in range(floor(reps/2)):
            completions += "✔"
        tick.config(text=completions)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=75, pady=60, bg=YELLOW)



label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35), fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", width=6, bg=PINK, font=(FONT_NAME, 10, "bold"), 
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=6, bg=PINK, font=(FONT_NAME, 10, "bold"), 
                      command=reset_timer)
reset_button.grid(column=2, row=2)

tick = Label(bg=YELLOW, font=(FONT_NAME, 15, 'bold'), fg=GREEN)
tick.grid(column=1, row=3)







window.mainloop()
