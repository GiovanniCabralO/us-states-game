import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

correct_answers = []

while len(correct_answers) < 50:
  
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state is None:
        break

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in correct_answers]
        pandas.DataFrame(missing_states, columns=["state"]).to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in states_list and answer_state not in correct_answers:
        state_data = data[data.state == answer_state].iloc[0]
        x_cor, y_cor = state_data.x, state_data.y


        names_on_map = turtle.Turtle()
        names_on_map.penup()
        names_on_map.hideturtle()
        names_on_map.goto(x=x_cor, y=y_cor)
        names_on_map.write(answer_state)

        correct_answers.append(answer_state)



if len(correct_answers) == 50:
    congrats = turtle.Turtle()
    congrats.hideturtle()
    congrats.penup()
    congrats.goto(0, 0)
    congrats.write(
        "🎉 Congratulations! You found all 50 states! 🎉",
        align="center",
        font=("Arial", 16, "bold")
    )
