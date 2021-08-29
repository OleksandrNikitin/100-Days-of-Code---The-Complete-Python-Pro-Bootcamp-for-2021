from replit import clear

from art import logo

# HINT: You can call clear() to clear the output in the console.

bid_dict = {}

while True:
    clear()
    print(logo)
    name = input("Input a name: ")
    bid = int(input("Input a bid: $"))
    bid_dict[name] = bid
    ask = input("Do you want to add another bid? Yes or No? ").lower()
    if ask != "yes":
        clear()
        break

max_bid = 0
winner_name = ""
for name in bid_dict:
    if bid_dict[name] > max_bid:
        max_bid = bid_dict[name]
        winner_name = name

print(f"The winner is {name} with a bid of ${max_bid}")
