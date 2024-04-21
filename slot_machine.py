MAX_LINES = 3 #constant value
MAX_BET = 10
MIN_BET = 1
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
        #getting deposit amount as a input from the user
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

def main ():

    balance = deposit()
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance :
            print(f"You do not have enough to bet that amount, your current balance is ${balance}" )
        else:
            break    
    print(f"You are betting {bet} on {lines} lines. Therefore total bet is equal to ${total_bet}.")

main()
