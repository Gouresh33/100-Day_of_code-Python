with open("../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")
#
# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text.")