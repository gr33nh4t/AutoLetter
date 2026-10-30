
class Create_Letters:
    def __init__(self, addressees, sender, letter, place):
        """This Class Create Letters from a Tempelate that had been given, whis is the third parameter.
        - Pass The name of adressees as a txt file.
        - Seconedly, the name of sender as string.
        - Thirdly, the Letter as a txt file
        - Fourthly, the location for the letters as a path.\n
        Note: You have to let your letter(template) addressee's name place like this: {name}, and your signature place like this: {signature}"""

        self.addressees = addressees
        self.sender = sender
        self.letter = letter
        self.place = place

        self.invited_names = []
        # calling the method which Stored the name of addressess in list
        self.addressees_list(self.addressees)

    #Create a list from NAMES
    def addressees_list(self, addressees, number=0):
        """This method takes one parameter, addressees's file, and change it to list.
        If you want to have just the list Enter (1)"""

        with open(addressees, 'r') as names_file:
            if addressees is FileNotFoundError:
                print('The path is uncorrect')
            else:
                names_list_before_strip = names_file.readlines()
                for name in names_list_before_strip:
                    if name == '\n':
                        continue
                    self.invited_names.append(name.strip())


        # if user want to use the class at all or just this method
        if number == 1:
            print(self.invited_names)
        else:
            self.create_letters(self.invited_names, self.sender, self.letter, self.place)


    # Create lettters method
    def create_letters(self, invited_names, sender, letter, place):
        """This method Create a letter for each name"""

        #  a loop to create file to each name
        for name in invited_names:
            # Calling letter changer method
            letter_ready_write = self.letter_change(name, sender, letter)
            
            # creating  a file for names
            if place is FileNotFoundError: #A PROBLEM HERE
                print('The location for letters isn\'t vail')
            else:
                with open('{place}\letter_for_{name}.txt'.format(place = place , name = name), 'w') as invited_letter:
                    if letter is FileNotFoundError:
                        print('The letter\' location is not correct')
                    else:
                        invited_letter.write(letter_ready_write)
                    
    # Change The Template message with names
    def letter_change(self, name, sender, letter):
        with open(letter, 'r') as main_letter:
            main_letter = main_letter.read()
            changed_letter = main_letter.format(name = name, signature = sender)
        return changed_letter
        

Create_Letters("letters\First_template\Addressees.txt", "Rahaf", "letters\First_template\Template.txt", "letters\First_templatejgj\send_letters")