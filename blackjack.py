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


def cut(cards):
  random.shuffle(cards)
  cards1 = cards[:26]
  cards2 = cards[26:]
  new_cards = cards2 + cards1
  return new_cards


def is_black_jack(num_hand):
  if sum(num_hand) == 21:
    return True
  else:
    return False


cards = [
  "A♠", "A♣", "A♦", "A♥", "2♠", "2♣", "2♦", "2♥", "3♠", "3♣", "3♦", "3♥", "4♠",
  "4♣", "4♦", "4♥", "5♠", "5♣", "5♦", "5♥", "6♠", "6♣", "6♦", "6♥", "7♠", "7♣",
  "7♦", "7♥", "8♠", "8♣", "8♦", "8♥", "9♠", "9♣", "9♦", "9♥", "10♠", "10♣",
  "10♦", "10♥", "J♠", "J♣", "J♦", "J♥", "Q♠", "Q♣", "Q♦", "Q♥", "K♠", "K♣",
  "K♦", "K♥"
]
cards = cut(cards)
num_cards = []
for each in cards:
  if each in [
      "10♠", "10♣", "10♦", "10♥", "J♠", "J♣", "J♦", "J♥", "Q♠", "Q♣", "Q♦",
      "Q♥", "K♠", "K♣", "K♦", "K♥"
  ]:
    num_cards.append(10)
  elif each in ["2♠", "2♣", "2♦", "2♥"]:
    num_cards.append(2)
  elif each in ["3♠", "3♣", "3♦", "3♥"]:
    num_cards.append(3)
  elif each in ["4♠", "4♣", "4♦", "4♥"]:
    num_cards.append(4)
  elif each in ["5♠", "5♣", "5♦", "5♥"]:
    num_cards.append(5)
  elif each in ["6♠", "6♣", "6♦", "6♥"]:
    num_cards.append(6)
  elif each in ["7♠", "7♣", "7♦", "7♥"]:
    num_cards.append(7)
  elif each in ["8♠", "8♣", "8♦", "8♥"]:
    num_cards.append(8)
  elif each in ["9♠", "9♣", "9♦", "9♥"]:
    num_cards.append(9)
  elif each in ["A♠", "A♣", "A♦", "A♥"]:
    num_cards.append(11)


def deal(hand, num_hand, num):
  global cards, num_cards
  for each in range(num):
    hand.append(cards.pop(0))
    num_hand.append(num_cards.pop(0))
  return hand


def back(hand, num_hand):
  global cards, num_cards
  cards.extend(hand)
  num_cards.extend(num_hand)
  return cards, num_cards


def jack():
  ur_hand = []
  ur_num_hand = []
  deal(ur_hand, ur_num_hand, 2)
  opp_hand = []
  opp_num_hand = []
  deal(opp_hand, opp_num_hand, 2)
  write(f"This is how much cash you have: ${cash.cash}")
  while True:
    write("What is your wager this round?")
    wager = input()
    try:
      wager = float(round(float(wager), 1))
      if wager <= 0:
        write("Not a positive value/cannot be zero!")
        continue
      elif wager > cash.cash:
        write("You cannot wager more than what you have!")
      else:
        break
    except ValueError:
      write("Not a number!")
      continue
  write("This is your hand:")
  print(', '.join(ur_hand))
  if ur_num_hand == [11, 11]:
    write("One ace is now worth 1!")
    ur_num_hand[ur_num_hand.index(11)] = 1
  elif opp_num_hand == [11, 11]:
    opp_num_hand[opp_num_hand.index(11)] = 1
  if is_black_jack(ur_num_hand) and is_black_jack(opp_num_hand):
    write("You both got a blackjack! You get your bet back.\n\n")
    back(ur_hand, ur_num_hand)
    back(opp_hand, opp_num_hand)
    write("Play again? [y/n]")
    yessir = input()
    if yessir.lower() == "n":
      clear()
      exec(open("main.py").read())
    else:
      jack()
  elif is_black_jack(opp_num_hand):
    write(f"Dang, the dealer got a blackjack! You lose ${wager}.\n\n")
    cash.cash -= wager
    back(ur_hand, ur_num_hand)
    back(opp_hand, opp_num_hand)
    write("Play again? [y/n]")
    yessir = input()
    if yessir.lower() == "n":
      clear()
      exec(open("main.py").read())
    else:
      jack()
  elif is_black_jack(ur_num_hand):
    write(
      f"Wow, you got a blackjack! Congrats, you win ${round(1.5*wager,1)}!\n\n"
    )
    cash.cash += float(round(1.5 * wager, 1))
    back(ur_hand, ur_num_hand)
    back(opp_hand, opp_num_hand)
    write("Play again? [y/n]")
    yessir = input()
    if yessir.lower() == "n":
      clear()
      exec(open("main.py").read())
    else:
      jack()
  while True:
    while True:
      write("Would you like to add to your wager? Please enter how much (0 for none):")
      new = input()
      try:
        new = float(round(float(new), 1))
        if new < 0:
          write("Not a positive value!")
          continue
        elif wager+new > cash.cash:
          write("You cannot wager more than what you have!")
        else:
          wager += new
          break
      except ValueError:
        write("Not a number!")
        continue
    while True:
      write("[1] Hit [2] Stand:")
      hit_stand = input()
      if hit_stand.strip() == "1" or hit_stand.strip() == "2":
        break
    if hit_stand.strip() == "1":
      deal(ur_hand, ur_num_hand, 1)
      write("\nThis is your new hand:")
      print(', '.join(ur_hand))
      if sum(ur_num_hand) > 21:
        if 11 in ur_num_hand:
          write("One ace is now worth 1!")
          try:
            fart = ur_num_hand.index(11)
            ur_num_hand[fart] = 1
          except ValueError:
            continue
          continue
        else:
          write("You busted! Let's see what the dealer got.\n")
          break
    elif hit_stand.strip() == "2":
      write("Your total stands at " + str(sum(ur_num_hand)))
      write("Let's see what the dealer got!\n")
      break
    else:
      continue
  write("...")
  while True:
    if (num_cards[0] + sum(opp_num_hand)) > 21:
      if 11 in opp_num_hand:
        try:
          fart = opp_num_hand.index(11)
          opp_num_hand[fart] = 1
        except ValueError:
          pass
        continue
      else:
        break
    else:
      deal(opp_hand, opp_num_hand, 1)
  write("This is the dealer's hand:")
  print(', '.join(opp_hand))
  write("Their total stands at " + str(sum(opp_num_hand)))
  if sum(ur_num_hand) <= 21 and sum(opp_num_hand) <= 21:
    if sum(opp_num_hand) > sum(ur_num_hand):
      write(f"The dealer won! Better luck next time! You lost ${wager}\n\n")
      cash.cash -= wager
    elif sum(opp_num_hand) < sum(ur_num_hand):
      write(f"You won this round! Congrats! You won ${wager}.\n\n")
      cash.cash += wager
    elif sum(opp_num_hand) == sum(ur_num_hand):
      write(f"You and the dealer tied! However, the dealer wins (rules) and you lose ${wager}\n\n")
      cash.cash -= wager
  elif sum(opp_num_hand) > 21 and sum(ur_num_hand) <= 21:
    write(f"The dealer busted! You won ${wager}!\n\n")
    cash.cash += wager
  elif sum(opp_num_hand) <= 21 and sum(ur_num_hand) > 21:
    write(f"You busted! You lost ${wager}.\n\n")
    cash.cash -= wager
  else:
    write(f"You both busted! However, the dealer wins (rules) and you lose ${wager}\n\n")
    cash.cash -= wager
  try:
    fart = ur_num_hand.index(11)
    ur_num_hand[fart] = 1
  except ValueError:
    pass
  try:
    fart = opp_num_hand.index(11)
    opp_num_hand[fart] = 1
  except ValueError:
    pass
  back(ur_hand, ur_num_hand)
  back(opp_hand, opp_num_hand)
  write("Play again? [y/n]")
  yessir = input()
  if yessir.lower() == "n":
    clear()
    exec(open("main.py").read())
  else:
    jack()
jack()
