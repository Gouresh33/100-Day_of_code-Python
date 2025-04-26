# def greet():
#     print("Hi I am Gouresh")
#     print("I like programming in python and listening to music")
#     print("I am also a gamer")
#
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
# greet_with_name("Gouresh")

def life_in_weeks(age):
    age_as_int = int(age)
    age_as_int = (age_as_int - 90) * 52
    print(f"You have {age_as_int} Weeks left if you life for 90 years")

life_in_weeks(25)