import random
from game_data import data
from art import logo, vs

def format_data(account):
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]

    return f"{account_name}, {account_des}, {account_country}"

def cheak_follower(user_guess, a_follower_account, b_follower_account):
    if a_follower_account > b_follower_account:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
should_con = True
account_b = random.choice(data)

while should_con:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 30)
    print(logo)
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct = cheak_follower(guess, a_follower_account, b_follower_account)

    if is_correct:
        score += 1

        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_con = False