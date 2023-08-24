import decimal
from colorama import init, Fore,  Style

print()
print(Fore.BLUE + "Welcome to the options trading calculator!\n" + Style.RESET_ALL) 
#print( "Welcome to the options trading calculator!" + "\n")
print("=============================================================" + "\n")

buying_power = decimal.Decimal(input("Enter your buying power: "))

entry_point = decimal.Decimal(input("Enter the premium price you want to buy: "))

print()

print("=============================================================" + "\n")

# calculate max contracts and ask user if they want to trade

max_contracts = int(round((buying_power / (entry_point * 100)), 2))
print(
    f"You can at most buy {max_contracts} contracts with your buying power: ${buying_power}"
)

decision = input("Do you want to trade? \n please enter: (y/yes, n/no): ")

print()
print("=============================================================" + "\n")

################################################################################################
# if user wants to trade, ask how many contracts they want to buy and calculate profit

if decision.lower() == "y" or decision.lower() == "Yes":
    contracts = int(input("How many contracts do you want to buy?: "))

    if contracts > max_contracts:
        print("You do not have enough buying power to buy that many contracts" + "\n")
        contracts = int(input("How many more contracts do you want to buy?: "))
    
    print(f"You bought {contracts} contracts" + "\n")
    amount_invested = decimal.Decimal(contracts * entry_point * 100)
    print(f"You invested ${amount_invested}" + "\n")
    amount_left = buying_power - amount_invested
    print(f"You have ${amount_left} left in your buying power" "\n")
    exit_point = decimal.Decimal(input("Enter the price you sold: "))
    profit = decimal.Decimal((exit_point - entry_point) * contracts * 100)
    percent_profit = round(((profit / amount_invested) * 100), 2)
    print(f"Your profit is ${profit} and your percent profit is {percent_profit}% \n")
    buying_power = buying_power + profit
    print(f"Your buying power is now ${buying_power}" + "\n")
    print("=============================================================" + "\n")
    print("Thank you for using this calculator!" + "\n")
    print("=============================================================" + "\n")
    exit()

################################################################################################
else:
    print("No day trades left for today :( GUH" + "\n")
    print("=============================================================" + "\n")
    print("Exiting trading portal....." + "\n")

    exit()
