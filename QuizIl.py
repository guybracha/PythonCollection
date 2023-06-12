print("Hello and Welcome to Quiz IL")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

question_one = input("has david ben-gurion was the first PM of israel?")
if question_one == "yes":
    print("you're correct")
    score = score + 1
else:
    print("wrong")
    quit()

question_two = input("how many times does maccabi tel aviv won as euroleague champion?")
if question_two == "6":
    print("great, you're correct")
    score = score + 2
else:
    print("wrong")
    print(score)
    quit()

question_three = input("was ephraim kishon the first israeli person who ever been nominated for the foreign oscars?")
if question_three == "yes":
    print("and the oscars goes to you")
    score = score + 3
else:
    print("you lose")
    print(score)
    quit()

question_four = input("which person has been called 'the jewish state's prophet'? herzl or someone else?")
if question_four == "herzl":
    print("congratulaions")
    score = score + 4
else:
    print("sorry")
    print(score)
    quit()

print("congratulaions, you've won the quiz. mazal tov")
print(score)
