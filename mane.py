def calculate_change(paid,price):
    change=paid-price
    return change

snack=500
print("SNACK VENDING MACHINE")
print(f"This snack cost Ush.{snack}") 
print("Accepted coins : 1,5,10,25\n")

total_inserted=0
coins_inserted=0

while True:
    coin=int(input("Insert a coin(1,5,10,25):"))
    coins=[1,5,10,25]
    if coin not in coins:
        print("Invalid coin Try agin")
        continue
    total_inserted+=1
    coins_inserted+=1


    print(f"Total coins inserted: {total_inserted}")
    if total_inserted>=snack:
        print("Enough Money Inserted")
        break

    change_due=calculate_change(total_inserted,snack)

    print("Dispensing Snack")

    if change_due==0:
        pass
    else:
        print(f"Here is your change:Ush.{change_due}")