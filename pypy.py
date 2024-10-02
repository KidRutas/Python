# My original Code

# fruits = ["Apple", "Strawberry", "Watermelon"]
# adjectives = ["Red", "Delicious", "Sweet"]

# for y in range(3):
#     global lim
#     lim = []
#     lim = adjectives[y] + " " + fruits[y]
#     print(y)
#     print(lim)
# print(lim)


# My ChatGpt improved code
fruits = ["Apple", "Strawberry", "Watermelon", "Craneberry"]
adjectives = ["Red", "Delicious", "Sweet", "Blue"]

for y in range(3):
    lim = adjectives[y] + " " + fruits[y]  # Combine adjective and fruit
    # print(y)  # Print the index
    print(lim)  # Print the combined string

# Print the last value of lim
# print(lim)
