import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guesses = []

data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()


def write_name_on_map(answer):
    mapping = turtle.Turtle()
    mapping.hideturtle()
    mapping.pu()
    x = int(data[data.state == answer].x)
    y = int(data[data.state == answer].y)
    mapping.goto(x, y)
    mapping.write(answer, align="center", font=("Arial", 8, "normal"))


while len(guesses) < 50:
    answer_state = screen.textinput(title="Guess States",
                                    prompt=f"{len(guesses)}/50 States Correct\nGuess a State name: ").title()
    if answer_state == "Exit":
        missed_guesses = {"Missed States": []}
        for name in state_names:
            if name not in guesses:
                missed_guesses["Missed States"].append(name)
        df = pandas.DataFrame(missed_guesses)
        df.to_csv("Missed_States.csv")

        break
    if answer_state in state_names and answer_state not in guesses:
        guesses.append(answer_state)
        write_name_on_map(answer_state)


screen.exitonclick()
