##############################################################################  
#  Computer Project #5a
#    
#  Algorithm  
#     Prompts for user inputs  
#     While loop to determine if correct user inputs have been input.       
#         Depending on criteria, For loop to copy lines into the output file
#         Closing of the files
#
##############################################################################

#This checks to see if the file is in the directory
while True:
    try:
        fp = open('polio.txt','r') #fp is the file we are peforming on  
        break
    except FileNotFoundError:
        print("file not found")
        input("Press enter to try again:")
    
#The user list file name to be generated
user_list = str(input("name the output file:"))

#The the destination of the file operations on fp
op = open(user_list,'w') 

#This is the input year range   
year_inp = str(input("Input a year ('all', 'ALL', or return for whole list):"))

#Simplifies the input to all lowercase for All
all_years = year_inp.lower()

#this copies the indicated lines over
while True:
    if all_years == 'all':
        for line in fp:
            op.write(line)
        break
    if (bool(year_inp) == False):
        for line in fp:    
            op.write(line)
        break
    else:
        try:
            
            #converts the year input to an integer
            year_inp = int(year_inp)
            
            #this copies the partial and full years 
            for line in fp:
                year = int(line[68:74])
                year_1 = int(line[68:69])
                year_2 = int(line[68:70])
                year_3 = int(line[68:71])
                if year_inp == year:
                    op.write(line)
                if year_inp == year_1: 
                    op.write(line)
                if year_inp ==  year_2: 
                    op.write(line)      
                if year_inp ==  year_3: 
                    op.write(line)      
            break
        
        #an expected error from putting in an invalid input (characters)
        except ValueError:
            print("Please input a year" )
            year_inp = (input("Try again:"))
              
#closing the files          
op.close()        
fp.close()