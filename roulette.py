import time, sys, os, random
import cash


def write(word):
  for ch in word:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.01)
  print()


def clear():
  os.system("clear")


def earns(rounds):
  if rounds == 1:
    return 1.1
  elif rounds < 3:
    return 1.15
  elif rounds:
    return 1.25

def calcwin(wager, xearn, rounds):
  return round(wager * xearn + rounds, 1)

while True:
  rounds = 1
  mag = [0, 0, 0, 0, 0, 0]
  i = random.randint(0, 5)
  mag[i] = 1
  died = False
  earnx = earns(rounds)
  write(
    "\nA bullet has been placed in a gun. You are now pointing it at your head."
  )
  while True:
    write(f"You have ${cash.cash}. What is your wager?")
    wager = input()
    try:
      wager = float(round(float(wager), 1))
      if wager > cash.cash:
        write("You cannot wager more than what you have!")
      elif wager <= 0:
        write("You cannot wager negative/zero!")
      else:
        break
    except ValueError:
      write("Not a number!")
  while died != True and rounds != 6:
    win = calcwin(wager, earnx, rounds)
    write(
      f"Would you like to pull the trigger and win ${win}? [y/n]"
    )
    pull = input()
    if pull.strip().lower() == "y":
      write(f"You pull the trigger and bet ${wager}... BANG!")
      if mag.pop(0) == 0:
        write(f"You survived and won ${win}\n")
        cash.cash += (win - wager)
        wager = win
        rounds += 1
        earnx = earns(rounds)
        continue
      else:
        if rounds == 0:
          write(f"You died and lost ${wager}\n")
          cash.cash -= wager
          died = True
        else:
          write(f"You died and lost ${wager}\n")
          cash.cash -= wager
          died = True
    elif pull.strip().lower() == "n":
      write("You decide to forfeit...\n")
      break
  if died and rounds > 1:
    write(
      f"You survived {rounds-1} rounds, but you died on the {rounds} round!")
  elif died and rounds == 1:
    write(f"You survived {rounds-1} rounds! :(")
  elif rounds == 6:
    write("You survived all 5 rounds! Wow!")
  else:
    write(f"You survived {rounds-1} rounds!")
  write("Play again? [y/n]")
  play = input()
  if play.lower() == "n":
    clear()
    exec(open("main.py").read())
    break
  else:
    continue
