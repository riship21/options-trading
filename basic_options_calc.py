import decimal

buying_power = decimal.Decimal(input("Enter your buying power: "))
amount = decimal.Decimal(input("Enter the money you put in: "))

if amount > buying_power:
    print("You don't have enough buying power")
    exit()


entry_point = decimal.Decimal(input("Enter the premium price you entered: "))
contracts_bought = int((amount / entry_point) / 100)
print(f"You bought {contracts_bought} contracts")
print()

exit_point = decimal.Decimal(input("Enter the price you sold: "))


buying_power_left = buying_power - amount
profit = decimal.Decimal((exit_point - entry_point) * contracts_bought * 100)
percent_profit = round(((profit / amount) * 100), 2)

print(f"You have ${buying_power_left} left in your buying power")
print()
print(
    f"Your profit is ${profit} and your percent profit is {percent_profit}% \n")
print("no more spy 0dte for me")
print()
