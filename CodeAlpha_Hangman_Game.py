import random
words = ["python", "matrix", "robot", "cloud", "linux"]
limit=6
chosen_word=random.choice(words)
word_progress=list(len(chosen_word)*"_")
while limit>0:
        if "_" not in word_progress:
                     print("Congratulations you did it!")
                     exit()
        player_input = input("Enter a letter: ")
        if player_input in chosen_word:             
              for i, letter in enumerate(chosen_word):
                   if letter == player_input:
                        word_progress[i] = player_input
                        print("You guessed it right, go on")
              print(word_progress)
        else:
             limit -= 1
             print(f"Try again \n{limit} Guess left") 
print(f"You lost! The word was: {chosen_word}")   
