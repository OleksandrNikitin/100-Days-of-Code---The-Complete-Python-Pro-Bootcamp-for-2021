PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt", mode="r") as template_file:
    template_letter = template_file.read()

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

for name in names:
    stripped_name = name.rstrip()
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(template_letter.replace(PLACEHOLDER, stripped_name))
