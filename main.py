import turtle as t
import time
from pathlib import Path

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

    with open(source_file) as mon_fichier:
        for line in mon_fichier:
            questions = []
            questions += line
            