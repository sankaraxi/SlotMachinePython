import random

#constant values
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_values = {  #these values are used for calculating winning amount
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values): #function to obtain winnings and winning line
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)

    return winnings , winning_lines

def get_slot_machine_spin(rows,cols,symbols): #function to to assign symbols for each rows
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #making a copy of an existing list
        for _ in range(rows):
            value = random.choice(current_symbols) #here the values are choosed randomly from the dictionary
            current_symbols.remove(value) #once the value is choosen, the value is removed from the list
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns): # function to display the transposed format of the columns
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): # Enumerate over the columns to iterate with both index and value
            if i != len(columns) - 1:
                print(column[row] , end = " | ")
            else:
                print(column[row] , end ="")
        print()


def deposit():
    while True:
        #getting deposit amount as a input from the user
        amount = input("Enter the amount that you would like to deposit : $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit amount should be greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount

def get_number_of_lines():
    while True:
        #getting number of lines to bet on from the user
        lines = input("Enter the number of lines to bet on (1 - "+str(MAX_LINES)+")  : ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")

    return lines

def get_bet():
    while True:
        #getting bet amount as a input from the user
        amount = input("Enter the amount that you would like to bet on each line : $")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET} - ${MAX_BET}") #string formatting
        else:
            print("Please enter a valid number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance :
            print(f"You do not have enough to bet that amount, your current balance is ${balance}" )
        else:
            break    
    print(f"You are betting {bet} on {lines} lines. Therefore total bet is equal to ${total_bet}.")

    slots = get_slot_machine_spin(ROWS,COLS,symbols_count)
    print_slot_machine(slots)
    winnings,winning_lines= check_winnings(slots,lines,bet,symbols_values)
    print(f"You won ${winnings}.")
    print(f"You won on the lines: ", *winning_lines) #unpacks the list and displays as 2 3 4 5
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}") #string formatting
        answerr = input("Press Enter to play (q to quit).")
        if answerr == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")

main()
