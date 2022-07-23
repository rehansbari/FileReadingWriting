#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
NAMES = []
with open("./Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()

for name in name_list:
    new_name = name.replace('\n', '')
    NAMES.append(new_name)


starting_letter = open("./Input/Letters/starting_letter.txt", mode="r")
letter = starting_letter.read()
txt_to_replace = "[name]"

new_letter = letter.replace(txt_to_replace, NAMES[0])

for name in NAMES:
    with open(f".//Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
        new_letter = letter.replace(txt_to_replace, name)
        new_file.write(new_letter)

starting_letter.close()







