##############################################################################  
#  Computer Project #8
#    
#  Algorithm
#     Call main function
#       List options to call functions
#       Call function to read contacts from file
#             Call function to open file
#       Call function to write collection of contacts to file
#       Call function to add new contact
#           Call function to validate phone number
#           Call function to validate email
#       Call function to remove existing contact
#       Call function to edit contact's phone number
#           Call function to validate phone number
#       Call function to edit contact's email
#           Call function to validate email
#       Call function to display contacts by prefix
#
##############################################################################


        
def open_file():
    """
    Opens the file
    
    Returns: an open file    
    """
    #This opens the file, if it exists
    while True:
        try:
            file_name=str(input("name the file: "))  #file name
            file_proc = open(file_name,) #The file being processed
            return file_proc
            break
        except FileNotFoundError:
            print("File does not exist")
            break
                       
def validate_phone(ph_num):
    """
    Validates the phone number
    
    ph_num: the number to be validated
    
    Returns: True or False    
    """
    #this goes through the seqence of number to determine correct formatting
    if ph_num[:3].isnumeric():
        if ph_num[3] == '-':
            if ph_num[4:7].isnumeric():
                if ph_num[7] == '-':
                    if ph_num[8:].isnumeric():
                        return True
    else:
        return False

def validate_email(email):
    """
    Validates the email address
    
    email:The email to be validated

    Returns: True or False
    """
    if '@' in email:
        return True
        
def read_contacts(dictionary):
    """
    Reads the a document and makes a dictionary of the contacts
    
    dictionary: The existing dictionary
    
    Returns: The new dictionary   
    """    
    
    dictionary ={}  #sets the dictionary to empty
    #Tries to open the file, if successful, creates the dictionary entries
    try:
        file = open_file()
        for line in file:
            line = line.strip()      #strips white space
            contact_info = line.split(';')   #makes a list out of the info
            dictionary[contact_info[0]] = contact_info[1:3] #updates dict
    except TypeError:
        print("File not found")
   
    return dictionary
    
def write_contacts(dictionary):
    """
    Writes the dictionary to a new text file
    
    dictionary: The existing dictionary
    
    Returns: nothing
    """
    
    #Opens the new file and writes the dictionary into a properly formatted txt
    file = open(str(input("name the file: ")), 'w')
    for i in dictionary.items():
        name = i[0]        #name of contact
        number = i[1][0]   #number of contact
        email = i[1][1]    #email of contact
        contact = [name,number,email]  #list of contact info
        line = ';'.join(contact) #makes a properly formatted line
        file.write(line)
        file.write('\n')
    file.close()     
        
def new_contact(dictionary):
    """
    Adds a new contact to the dictionary
    
    dictionary: existing dictionary
    
    Returns: dictionary with added contact 
    """
    
    #checks the name and goes forward if the name is valid
    name = str(input("Name: "))
    name = name.strip()
    empty_name = ""
    if name ==  empty_name:
        print("Bad name")
    if name in dictionary:
        print('Contact already in collection')
    else:
        phone = str(input("Phone: "))  #new contact's number
        phone = phone.strip()          #no white space
        
        #validates phone
        if validate_phone(phone):
            email = str(input("Email: "))  #new contact's email
            email = email.strip()          #no white space
            
            #validates email
            if validate_email(email):
                dictionary[name] = [phone,email]
            else:
                print("Bad email")
        else:
            print("Bad phone")
    return dictionary

def remove_contact(dictionary):
    """
    Removes contact

    dictionary: existing dictionary

    returns: dictionary with removed contact      
    """
    
    #checks name if valid, it deletes it from the dictionary
    name = str(input("Name: "))
    name = name.strip()
    if name in dictionary:
        del dictionary[name]   
    else:
        print("Name not in collection")
    return dictionary
        

def update_phone(dictionary):
    """
    updates the phone number of a contact
    
    dictionary: the existing dictionary
    
    returns: dictionary with updated contact
    """  
    
    #checks name if valid, it updates the dictionary entry
    name = str(input("Name: "))
    name = name.strip()
    if name in dictionary:
        phone = str(input("Phone:"))  #new phone number
        phone = phone.strip()
        if validate_phone(phone):
            dictionary[name][0] = phone
        else:
            print("Bad phone")
    else:
        print("Bad name")
    return dictionary

def update_email(dictionary):
    """
    updates the email number of a contact
    
    dictionary: the existing dictionary
    
    returns: dictionary with updated contact
    """   
    
    #checks name if valid, it updates the dictionary entry
    name = str(input("Name: "))
    name = name.strip()
    if name in dictionary:
        email = str(input("Email:")) #new email
        email = email.strip()
        if validate_email(email):
            dictionary[name][1] = email
        else:
            print("Bad email")
    else:
        print("Bad name")
    return dictionary

def contact_subset(dictionary):
    """
    displays a subset of the contact list
    
    dictionary: the existing dictionary
    
    returns: nothing
    
    """
    
    subset = []  #the subset of the contact list  
    full_list = '' #blank entry
    prefix =str(input("Name: ")) #prefix to display
    prefix = prefix.strip()
    
    #if it is a blank entry, the entire list is printed
    if prefix == full_list:
        for i in dictionary.items():        
            subset.append(i)
    #this finds the indicated subset of contacts
    else:
        for i in dictionary.items():        
            if prefix in i[0][:(len(prefix))]:
                subset.append(i)
    header = ["Name", "Number",  "E-mail"]  #printed header
    print('{:<16} {:<12} {:>16}'.format(*header))
    subset = sorted(subset)  #sorted list of contacts
    #Prints the sorted subset of contacts
    for i in subset:
        name = i[0]         #name
        number = i[1][0]    #number
        email = i[1][1]     #email
        contact = [name,number,email]   #contact list
        print('{:<16} {:<12} {:>24}'.format(*contact))
    


def main():
    """
    invokes all of the other functions to run the program
    
    returns:none
    """
    
    #prints the menu of selections
    MENU = """
        A)  Read collection of contacts from file
        B)  Write collection of contacts to file
        C)  Add new contact
        D)  Remove existing contact
        E)  Update existing contact's phone number
        F)  Update existing contact's email address
        G)  Display contacts by prefix
        X)  Exit from the program"""
    print(MENU)
    
    #input for choosing an option
    choice = input("Choice: ")
    contact_book ={}
    up_choice = choice.upper()
    
    #The option menu choices to invoke the different functions
    while True:
        if up_choice == 'A':
            contact_book = read_contacts(contact_book)
        if up_choice == 'B':
            write_contacts(contact_book)
        if up_choice == 'C':
            contact_book = new_contact(contact_book)
        if up_choice == 'D':
            contact_book = remove_contact(contact_book)
        if up_choice == 'E':
            contact_book = update_phone(contact_book)
        if up_choice == 'F':
            contact_book = update_email(contact_book)
        if up_choice == 'G':
            contact_subset(contact_book)
        if up_choice == 'X':
            break
        print(MENU)
        choice = input("Choice: ")
        up_choice = choice.upper()


#formal way of calling main      
if __name__ == '__main__':
    main()
    