import secrets


# Describe Problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_number = secrets.choice(range(0, 6))
print(dice_images[dice_number])

# Play Computer
year = int(input("What's your year of birth?"))
if 1980 < year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# Print is Your Friend
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
