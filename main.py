import turtle as t
import time
from pathlib import Path

#show question and write answer player in a file
def game(question, nameAnime, root_dir):
    window = t.Screen()
    window.title("quizz")
    window.bgcolor('gray')
    window.setup(width=1600, height = 1400)
    window.tracer(0)

    pen = t.Turtle()
    pen.speed(0)
    pen.color("White")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,0)
    pen.write("{}".format(question), align = 'center', font = ('Arial', 32, 'normal'))
    time.sleep(20)
    answer_player = t.textinput("answer", "Your answer ?")
    source_file = root_dir / "answers_player.txt"
    with open(source_file, "a", encoding="utf-8") as answer_player_file:
        answer_player_file.write(answer_player + "\n")


if __name__ == "__main__":
    #creating the platform
    window = t.Screen()
    window.title("quizz")
    window.bgcolor('gray')
    window.setup(width=800, height = 600)
    window.tracer(0)

    pen = t.Turtle()
    pen.speed(0)
    pen.color("White")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,0)
    pen.write("Anime Quizz", align = 'center', font = ('Arial', 32, 'normal'))

    time.sleep(2)
    window.clear()

    nameAnime = t.textinput("anime", "Choose your anime :")
    nameAnime.lower()
    nameAnime += ".txt"
    # print(nameAnime)

    root_dir = Path("/home/brante/Documents/dev/projet_personnel/quizz")
    source_file = root_dir / nameAnime
    # print(source_file.name)

    questions = []
    with open(source_file) as questions_file:
        for line in questions_file:
            questions.append(line)

    for question in questions:
        game(question, nameAnime, root_dir)
    