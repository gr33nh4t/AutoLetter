#  a function to change the main letter for each name
def letter_change(name):
    with open('Input\letters\starting_letters.txt', 'r') as main_letter:
        main_letter = str(main_letter.read())
        letter = main_letter.format(name = name, signature = 'Rahaf The Coder')
    return letter


#All names
invited_names = []



# Stored invited_names.txt in list
with open('Names\invited_names.txt', 'r') as names_file:
    names_list_before_strip = names_file.readlines()
    for name in names_list_before_strip:
        if name == '\n':
            continue
        invited_names.append(name.strip())



#  a loop to create file to each name
for name in invited_names:
    letter = letter_change(name)
    with open(f'Output\Ready_to_send\letter_for_{name}.txt', 'w') as invited_letter:
        invited_letter.write(letter)