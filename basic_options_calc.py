import decimal

buying_power = decimal.Decimal(input("Enter your buying power: "))

entry_point = decimal.Decimal(
    input("Enter the premium price you want to buy: "))

print()

max_contracts = int(round((buying_power / (entry_point * 100)), 2))
print(
    f"You can at most buy {max_contracts} contracts with your buying power: ${buying_power}")

decision = input("Do you want to trade? \n please enter: (y/yes, n/no): ")

if decision.lower() == "y" or decision.lower() == "Yes":
    contracts = int(input("How many contracts do you want to buy?: "))
    if contracts > max_contracts:
        print("You do not have enough buying power to buy that many contracts")
        contracts = int(input("How many more contracts do you want to buy?: "))
    print(f"You bought {contracts} contracts")
    amount_invested = decimal.Decimal(contracts * entry_point * 100)
    print(f"You invested ${amount_invested}")
    print()
    amount_left = buying_power - amount_invested
    print(f"You have ${amount_left} left in your buying power")
    print()
    exit_point = decimal.Decimal(input("Enter the price you sold: "))
    profit = decimal.Decimal((exit_point - entry_point) * contracts * 100)
    percent_profit = round(((profit / amount_invested) * 100), 2)
    print(
        f"Your profit is ${profit} and your percent profit is {percent_profit}% \n")
    buying_power = buying_power + profit
    print(f"Your buying power is now ${buying_power}")
    print()
    print("Thank you for using this calculator!")
    print()
    exit()

else:
    print()
    print("No day trades left for today :( GUH")
    print()
    exit()
