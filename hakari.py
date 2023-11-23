import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

num_of_symbols = {
    "Pig": 6,
    "Cherry": 15,
    "Blueberry": 23,
    "Coin": 35
}


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items:
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    collums = [[], [], []]


def deposit():
    while True:
        money = input("How much money would you like to deposit? $ ")
        if money.isdigit():
            money = int(money)
            if money > 0:
                break
            else:
                print("You must deposit more than 0 dollars")
        else:
            print("You must type in a number")
    return money


def lines():
    while True:
        lines_picked = input("How many lines do you want to bet on? (1-" + str(MAX_LINES) + ")? ")
        if lines_picked.isdigit():
            lines_picked = int(lines_picked)
            if 1 <= lines_picked <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("You must type in a number")
    return lines_picked


def bet_amount():
    while True:
        bets = input("How much would you like to bet on each line? $ ")
        if bets.isdigit():
            bets = int(bets)
            if MIN_BET < bets < MAX_BET:
                break
            else:
                print("Please type a valid amount (" + str(MIN_BET) + "-" + str(MAX_BET) + ")")
        else:
            print("Please type a digit")
        return bets


def main():
    balance = deposit()
    line = lines()
    while True:
        bet = bet_amount()
        total_bet = bet * line
        if total_bet > balance:
            print(f"You dont have enough, brokie. You only have ${balance}")
        else:
            break
    print(f"You are betting {bet} on {line} lines, making your total bet: $ {total_bet}")
    print(balance, line, bet)


main()
