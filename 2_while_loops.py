#notes on while loops
# while loop = execute some code WHILE some conditions remain true

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name:")
# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")


# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like ( q to quit): ")

# print("bye")
# food_list = []
# print("I like " + food + " too!")
# food_list.append(food)
# food

# num= input("Enter a # between 1 - 10: ")

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     mum= int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")


# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

index = 0
while index < len(colors):
    if colors [index] == "yellow":
        break
    print(colors[index])
    index+= 1 # increment the index to avoid the infinite loop