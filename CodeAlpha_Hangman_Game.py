"""
import random
words = ["python", "matrix", "robot", "cloud", "linux"]
limit=6
chosen_word=random.choice(words)
word_progress=list(len(chosen_word)*"_")
while limit>0:
        if "_" not in word_progress:
                     print("Congurlations you did it!")
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
"""
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 415,
    "NVDA": 875,
    "META": 510,
    "NFLX": 635
}
total=0
while input("Yeni sehm almaq isteyirsiniz? (Y/N): ").upper() == "Y":
          sehm = input("Enter a name: ").upper()
          if sehm not in stock_prices:
               print("This stock is not available.")
               continue
          else:
               times =int(input("How much do you want: "))
               Umumi=stock_prices.get(sehm) * times
               total += Umumi
               with open("stoklar.txt","a") as file:
                     file.write(f"Sehm: {sehm}, Times: {times}, Total: {Umumi}\n")
with open("stoklar.txt", "r") as file:            
     print(f"\nThank you for using our service! \nThis is your list: \n{file.read()} And your total is: {total}")