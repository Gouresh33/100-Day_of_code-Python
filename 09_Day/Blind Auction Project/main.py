# TODO-1: Ask the user for input
from art import logo
print(logo)
# TODO-2: Save data into dictionary {name: price}
def find_highest_bitter(bitting_direa):
    winner = ""
    highest_bit = 0
    for bitter in bitting_direa:
        bit_amount = bitting_direa[bitter]
        if bit_amount > highest_bit:
            highest_bit = bit_amount
            winner = bitter

    print(f"The winner is {winner} with a bid of ${highest_bit}")
bit_name = {}
# TODO-3: Whether if new bids need to be added
should_con = True
while should_con:
    name = input("What is your name?: ")
    bit = float(input("What is your bid?: $"))
    bit_name[name] = bit
    yes_or_no = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_con == "no":
        should_con = False
        find_highest_bitter(bit_name)
    elif should_con == "yes":
        print("\n" * 20)
# TODO-4: Compare bids in dictionary
