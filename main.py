import turtle as t
import time
from pathlib import Path

#show question and write answer player in a file
def game(question, nameAnime, root_dir):
    
    window = t.Screen()
    window.clear()
    window.title("quizz")
    window.bgcolor('gray')
    window.setup(width=1600, height = 400)
    window.tracer(0)
    pen = t.Turtle()
    pen.speed(0)
    pen.color("White")
    pen.penup()
    pen.hideturtle()

    compteur = 0
    for letter in question:
        compteur += 1
    
    question1 = ""
    question2 = ""
    if compteur > 50:
        compteur = 0
        for letter in question:
            if compteur < 51:
                compteur += 1
                question1 += letter
            else:
                compteur += 1
                question2 += letter
        pen.goto(0,0)
        pen.write("\n \n {} \n {}".format(question1, question2), align = 'center', font = ('Arial', 32, 'normal'))
    else:
        pen.write("{}".format(question), align = 'center', font = ('Arial', 32, 'normal'))
    
    time.sleep(3)
    answer_player = t.textinput("answer", "Your answer ?")
    source_file = root_dir / "answers_player.txt"
    with open(source_file, "a", encoding="utf-8") as answer_player_file:
        answer_player_file.write(answer_player + "\n")

def correction(nameAnime, root_dir):
    window = t.Screen()
    window.clear()
    window.title("quizz")
    window.bgcolor('gray')
    window.setup(width=1600, height = 400)
    window.tracer(0)

    pen = t.Turtle()
    pen.speed(0)
    pen.color("White")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,0)
    pen.write("correction".format(question), align = 'center', font = ('Arial', 32, 'normal'))
    time.sleep(5)

    his_source_file = root_dir / "answers_player.txt"
    newNameAnime = "answers_" + nameAnime
    answers_source_file = root_dir / newNameAnime

    his_answer = []
    correct_answers = []
        
    with open(his_source_file) as his_answer_file:
        for line in his_answer_file:
            his_answer.append(line)

    with open(answers_source_file) as correct_answer_file:
        for line in correct_answer_file:
            correct_answers.append(line)

    correct_answer = 0

    for i in range(len(correct_answers)):
        if his_answer[i] == correct_answers[i]:
            correct_answer += 1
        
    window.clear()
    window.bgcolor('gray')
    pen.speed(0)
    pen.color("White")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,0)
    pen.write("You have {} correct answers".format(correct_answer), align = 'center', font = ('Arial', 32, 'normal'))
    time.sleep(5) 


def scoreboard(username):
    with open("/home/brante/Documents/dev/projet_personnel/quizz/scoreboard.txt", 'r+', encoding="utf-8") as scoreboard:
        scoreboard.write(username + " , " + correct_answer)

#################################################################################################################################

if __name__ == "__main__":

    #clear the file of ancient player
    with open("/home/brante/Documents/dev/projet_personnel/quizz/answers_player.txt", 'a') as his_answer_file:
        his_answer_file.truncate(0)
    
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

    username = t.textinput("username", "Choose your username :")
    nameAnime = t.textinput("anime", "Choose your anime :")
    nameAnime.lower()
    nameAnime += ".txt"

    root_dir = Path("/home/brante/Documents/dev/projet_personnel/quizz")
    source_file = root_dir / nameAnime

    questions = []
    with open(source_file) as questions_file:
        for line in questions_file:
            questions.append(line)

    for question in questions:
        game(question, nameAnime, root_dir)
    
    correction(nameAnime, root_dir)
    scoreboard(username)