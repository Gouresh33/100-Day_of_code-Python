try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid input plz enter a numeric value like 15.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
