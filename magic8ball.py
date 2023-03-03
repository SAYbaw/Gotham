#Magic 8 Ball
import random

playAgain = "y"

name = input("Welcome to the Magic 8 Ball.  Type your name and press enter:")

print("Hello", name)

print("Let me tell you your fortune... IF YOU DARE!")

while playAgain == "y":

    input("Ask me a question out loud and press enter")

    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes – definitely",
               "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes",
               "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
               "Very doubtful."]

    print(answers[random.randint(0,19)], name)

    print(f"Ask another question {name}?")

    playAgain = input("press [y] for yes or [n] for no:")

print("Good Luck " + name)
