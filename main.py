import time, sys, os
import cash

def write(word):
  for ch in word:
      sys.stdout.write(ch)
      sys.stdout.flush()
      time.sleep(0.01)
  print()

def clear():
  os.system("clear")

write("Welcome to the 37♦ Casino!\n")
#while True:
#  write("")
write(f"You have ${cash.cash}!")
write("Here at the casino, we offer the following games (still in dev, may have bugs):")
write("[1] Blackjack\n[2] Russian Roulette")
while True:
  write("Which game would you like to play?")
  which_game = input(">")
  if which_game.strip() == "1":
    clear()
    write("Ok, lets play some blackjack!\n")
    exec(open("blackjack.py").read())
  elif which_game.strip() == "2":
    clear()
    write("Ok, lets play some Russian roulette!\n")
    exec(open("roulette.py").read())