import math
# Functions with input

# def greet_with_name_and_location(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
# greet_with_name_and_location(location = "Mumbai", name = "Gouresh")


# def calculate_love_score(name1, name2):
#     lower_name1 = name1
#     lower_name2 = name2
#     t_count = lower_name1.count("t")
#     r_count = lower_name1.count("r")
#     u_count = lower_name1.count("u")
#     e_count = lower_name1.count("e")
#     Total_True = t_count + r_count + u_count + e_count
#
#     l_count = lower_name2.count("l")
#     o_count = lower_name2.count("o")
#     v_count = lower_name2.count("v")
#     e_count_love = lower_name2.count("e")
#     Total_love = l_count + o_count + v_count + e_count_love
#
#     print(f"T occurs {t_count} times")
#     print(f"R occurs {r_count} times")
#     print(f"U occurs {u_count} times")
#     print(f"E occurs {e_count} times")
#     print(f"Total = {Total_True}")
#
#     print(f"L occurs {l_count} time ")
#     print(f"L occurs {o_count} time ")
#     print(f"L occurs {v_count} time ")
#     print(f"L occurs {e_count_love} time ")
#     print(f"Total = {Total_love}")
#
#     Total_count = int(str(Total_True) + str(Total_love))
#     print(f"Love Score = {Total_count}")
#
# calculate_love_score(name1 = "Gouresh", name2 = "Shital")

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")